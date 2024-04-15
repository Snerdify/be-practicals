! pip install tensorflow_hub

import tensorflow_hub as hub
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import cv2

model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')


def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

content_image = load_image('car1.jpeg')
style_image = load_image('ab3.jpeg')

stylized_image = model(tf.constant(load_image('car1.jpeg')), tf.constant(load_image('ab3.jpeg')))[0]

plt.imshow(np.squeeze(stylized_image))
plt.show()

plt.imshow(np.squeeze(stylized_image))
plt.show()