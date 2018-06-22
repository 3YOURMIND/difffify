from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView

from filepath.models import FilePath
from filepath.serializers import FilePathSerializer


class ListCreateFilePathView(ListCreateAPIView):
    serializer_class = FilePathSerializer
    queryset = FilePath.objects.all()


class UpdateDeleteFilePathView(RetrieveUpdateDestroyAPIView):
    serializer_class = FilePathSerializer

    def get_object(self):
        return FilePath.objects.get(id=self.kwargs['file_id'])
