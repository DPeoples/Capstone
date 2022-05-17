import sys
import time
import os
# [START storage_file_upload_from_memory]
from google.cloud import storage
from google.oauth2 import service_account
import cv2 
import numpy as np
from matplotlib import pyplot as plt
import os
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder
from object_detection.utils import config_util


def get_frames(inputFile,outputFolder,step,count):

  #initializing local variables
    step = step
    frames_count = count

    currentframe = 0
    frames_captured = 0

  #creating a folder
    try:  
        # creating a folder named data 
        if not os.path.exists(outputFolder): 
            os.makedirs(outputFolder) 
    
  #if not created then raise error 
    except OSError: 
        print('Error! Could not create a directory') 
  
  #reading the video from specified path 
    cam = cv2.VideoCapture(r"C:\Users\DeAndra Peoples\TFODCourse\Tensorflow\workspace\images\test\pencilvid1.mkv") 

  #reading the number of frames at that particular second
    frame_per_second = cam.get(cv2.CAP_PROP_FPS)

    while (True):
        ret, frame = cam.read()
        if ret:
            if currentframe > (step*frame_per_second):  
                currentframe = 0
              #saving the frames (screenshots)
                name = '/frame' + str(frames_captured) + '.jpg'
                print('Creating...' + name) 
                store = outputFolder + name
                cv2.imwrite(store, frame)
                cv2.imshow('frame', frame)
                frames_captured+=1
              
              #breaking the loop when count achieved
                if frames_captured > frames_count-1:
                    ret = False
                currentframe += 1           
            if ret == False:
                break

inputf = r"C:\Users\DeAndra Peoples\TFODCourse\Tensorflow\workspace\images\test\pencilvid1.mkv"
get_frames(inputf,r'C:\Users\DeAndra Peoples\TFODCourse\Tensorflow\workspace\images\test',.3,30)
