'''Process images with MTCNN.'''
from multiprocessing import Pool
import os
from random import randint

import cv2
from PIL import Image

from facenet_pytorch import MTCNN

IMGS = [os.path.join(
        os.path.dirname(__file__),
        'img', f) for f in os.listdir('img')[:1000]]


MAX_CHUNK = 10

def process_files(filenames):
    '''Summary of process_files.

    Args:
        filenames |list| list of images for processing.
    '''
    mtcnn = MTCNN(
        select_largest=False,
        margin=40,
        keep_all=True,
        post_process=False,
        )
    file_nums = [randint(10000, 100000) for _ in range(MAX_CHUNK)]
    save_paths = [os.path.join(
                    os.path.dirname(__file__),
                    'processed_imgs', f'image_{f}.jpg') for f in file_nums]
    mtcnn(filenames, save_path=save_paths)

if __name__ == '__main__':
    frames = []
    spam = []
    for num, img in enumerate(IMGS):
        img = cv2.imread(img)
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        spam.append(Image.fromarray(frame))
        if num % MAX_CHUNK == 0:
            frames.append(spam)
            spam.clear()

    pool = Pool()

    while len(frames):
        eggs = frames.pop()
        results = pool.imap(process_files, eggs)
