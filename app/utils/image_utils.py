import numpy as np
import cv2

WHITE_COLOR = 255
GRAY_COLOR_BOUNDRY = 128


def invert_image(image):
    gray_scale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_scale_image = WHITE_COLOR * \
        (gray_scale_image < GRAY_COLOR_BOUNDRY).astype(np.uint8)
    return gray_scale_image


def find_rectangle(gray_scale_image):
    coordinates = cv2.findNonZero(gray_scale_image)
    return cv2.boundingRect(coordinates)


def remove_white_borders(image):
    x, y, width, height = find_rectangle(invert_image(image))
    return image[y:y+height, x:x+width]
