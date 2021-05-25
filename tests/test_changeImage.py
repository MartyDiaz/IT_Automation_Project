import pytest
from PIL import Image
import os
from unittest import mock
from changeImage import resize_image, save_image_jpeg

'''
@mock.patch("changeImage.Image.resize")
@mock.patch("changeImage.Image")
def test_resize_image(mock_Image, mock_Image_resize):
    resize_width= 10
    resize_height = 10
    resize_image(mock_Image, resize_width, resize_height)
    mock_Image_resize.assert_called_with((resize_width, resize_height))
'''


def test_resize_image():
    im = Image.new("L", (100, 100))
    im_resized = im.resize((200, 200))
    test_im_resized = resize_image(im, 200, 200)
    assert test_im_resized.size == im_resized.size


def test_save_image_jpeg(tmpdir):
    image_path = os.path.expanduser('~') + '/Documents' \
                                           '/google_class' \
                                           '/project_8' \
                                           '/tests' \
                                           '/images' \
                                           '/001.tiff'
    image_file_name = '001.tiff'
    with Image.open(image_path) as im:
        save_image_jpeg(im, image_file_name, tmpdir)
    test_file = os.path.join(tmpdir, '001.jpeg')
    assert os.path.isfile(test_file)
