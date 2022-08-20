# -*- coding: utf-8 -*-
import cv2
import glob
import logging
import os
import sys

logging.basicConfig(format="%(asctime)s.%(msecs)03d %(levelname)s  %(module)s-%(funcName)s: %(message)s")


class LicensePlateDetector:
    def __init__(self, model_path="./haar_cascade_model.xml"):
        self.face_cascade = cv2.CascadeClassifier(model_path)
        logging.getLogger().setLevel(logging.INFO)
        logging.info(
            "Class \"LicensePlateDetector\" has bin initialized succesfully")

    def detect(self, image_path, save_to="./result_images/"):
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug(f"Working with the image - {image_path}")
        # process the image to better locate the license plate
        image = cv2.imread(image_path, 1)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray,
                                              scaleFactor=1.1,
                                              minNeighbors=5,
                                              minSize=(10, 10))

        # get the points from the previously 
        # constructed mask and form the frames
        for (x, y, w, h) in faces:
                BLUE = (255, 255, 0)
                cv2.rectangle(image, (x, y), (x+w, y+h), BLUE, 2)

        # save an image
        if os.path.exists(save_to):
                cv2.imwrite(os.path.join(save_to, image_path.split("/")[-1]), image)
        else:
                os.mkdir(save_to)
                cv2.imwrite(os.path.join(save_to, image_path.split("/")[-1]), image)
        logging.getLogger().setLevel(logging.INFO)
        logging.info("Success!")


if __name__ == "__main__":
    dirin = "./test_images/" # path to dir with images
    dirout = "./result_images/" # path where the processed images are saved
    lpd = LicensePlateDetector()
    for img in glob.glob(dirin+"*.*"):
        lpd.detect(image_path=img, save_to=dirout)

