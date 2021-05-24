import pytest
from PIL import Image
from unittest import mock
from changeImage import resize_image

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
    im_resized = im.resize((200,200))

    test_im_resized = resize_image(im, 200, 200)

    assert test_im_resized.size == im_resized.size