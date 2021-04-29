#!/usr/bin/env python3
""" Makes a post request for every jpeg image in a directory.

    This script is used for google's IT_automation class. The directory
    contains images for every fruit that will be displayed in customers website.
"""
import requests
import os


def post_images():
    """ This funtion makes a post request for every jpeg image in a directory.
    Args:
        None

    Returns:
        None
    """
    url = "http://localhost/upload/"
    image_directory = os.path.expanduser('~') + '/Documents/google_class/project_8/supplier-data/images'
    for root,dirs,files in os.walk(image_directory):
        files = [f for f in files if notf[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for file in files:
            if '.jpeg' in file:
                image_path = os.path.join(root, file)
                with open(image_path, 'rb') as opened:
                    request = requests.post(url, files={'file': opened})


def main():
    post_images()


if __name__ == "__main__":
    main()
