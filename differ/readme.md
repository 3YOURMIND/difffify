# diff-generator

A Django REST based API to compare a list of filepaths against two different commits.

Commits can be specified in the form of branches, tags or specific commit hashes.

### Prerequisites

Ensure you have pip and sqlite installed on your machine

### Installation

```bash
git clone git@bitbucket.org:3yourmind/diff_generator.git
cd diff_generator
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser # Follow instructions
python manage.py runserver
```

add a `settings_local.py` files in `diff_generator/` and add `REPO_PATH=path/to/repo` replacing the path with your 
own relative path to a repo root.

### Usage

Create some FilePath objects in the admin panel `localhost:8000/admin` using the superuser you created - these will be the filepaths 
you wish the diff command to display an output for when comparing between commits.

### Deployment with Docker
`docker build -t diff_generator .`
`docker run -it -e DJANGO_DEBUG=<0|1> -v <REPO_PATH>:/app/repo -p 80:8000 diff_generator`
The source can also be mounted into `/app/src` to avoid rebuilding the image on every code change.
