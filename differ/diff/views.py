import os
import git
from git import GitCommandError

from django.conf import settings
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import RetrieveAPIView

from filepath.models import FilePath


class GetDiffView(RetrieveAPIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.repo = git.Repo(settings.REPO_PATH)

    @staticmethod
    def get_paths():
        return [
            os.path.join(settings.REPO_PATH, filepath.path)
            for filepath in FilePath.objects.all()
        ]

    def get_versions(self):
        from_commit = self.get_tree(self.repo,
                                    self.request.GET['from-version'])
        to_commit = self.get_tree(self.repo, self.request.GET['to-version'])
        return from_commit, to_commit

    def get(self, request, *args, **kwargs):
        if not FilePath.objects.exists():
            return JsonResponse({'diff': ''})

        try:
            # TODO: restore this after access control to repo has been sorted out
            # if not self.repo.remotes:
            #     raise ValueError('Repository has no remote.')
            # self.repo.remotes[0].pull()
            diff = self.repo.git.diff(*self.get_versions(), self.get_paths())
        except (ValueError, GitCommandError) as e:
            return JsonResponse({
                'diff': None,
                'error': {
                    'diffCommand': ' '.join(e.command),
                    'errorMessage': e.stderr
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            return JsonResponse({
                'diff': None,
                'error': {
                    'invalidRevision': str(e.args[0]),
                    'errorMessage': 'Invalid revision supplied'
                }
            }, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'diff': diff})

    @staticmethod
    def get_tree(repo, query):
        tag_string = f'refs/tags/{query}'
        branch_string = f'refs/heads/{query}'

        if tag_string in repo.tags:
            return repo.tag(tag_string).commit
        elif branch_string in repo.branches:
            return repo.branches(branch_string).commit
        else:
            try:
                return repo.commit(query)
            except (ValueError, git.BadName):
                pass
        raise ValidationError(query)
