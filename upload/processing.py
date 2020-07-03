from upload.models import File
from django.core.files.storage import FileSystemStorage


# TODO: pars string to get data for file table [FINISHED]

def get_name(file):
    name = file.name
    pos = 0
    index = 0

    # in case file have '.'
    while pos != -1:
        index = pos
        pos = name.find('.', pos + 1)

    return name[0:index]


def get_url(file):
    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    uploaded_file_url = fs.url(filename)
    return uploaded_file_url


def get_type(file):
    name = file.name
    pos = 0
    index = 0

    # in case file have '.'
    while pos != -1:
        index = pos
        pos = name.find('.', pos + 1)

    return name[index:]
