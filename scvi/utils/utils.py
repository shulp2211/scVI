import os


def make_dir_if_necessary(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
