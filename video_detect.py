#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:57:24 2019

@author: cong
"""
import numpy as np
import cv2
from yolo import YOLO, detect_video
from PIL import Image
import yolo



output_path = './'

vid = cv2.VideoCapture('0.mp4')
#FourCC全称Four-Character Codes，代表四字符代码 (four character code), 它是一个32位的标示符，
#其实就是typedef unsigned int FOURCC;是一种独立标示视频数据流格式的四字符代码。
#因此cv2.VideoWriter_fourcc()函数的作用是输入四个字符代码即可得到对应的视频编码器。
video_FourCC = cv2.VideoWriter_fourcc(*'MP42')


video_fps       = vid.get(cv2.CAP_PROP_FPS)
video_size      = (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)),int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT)))

out = cv2.VideoWriter(output_path, video_FourCC, video_fps, video_size)

while True:
    return_value, frame = vid.read()

    image = Image.fromarray(frame)
    
    image = yolo.detect_image(image)
    
#    result = np.asarray(image)
#    curr_time = timer()
#    exec_time = curr_time - prev_time
#    prev_time = curr_time
#    accum_time = accum_time + exec_time
#    curr_fps = curr_fps + 1
#    if accum_time > 1:
#        accum_time = accum_time - 1
#        fps = "FPS: " + str(curr_fps)
#        curr_fps = 0
#    cv2.putText(result, text=fps, org=(3, 15), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
#                fontScale=0.50, color=(255, 0, 0), thickness=2)
#    cv2.namedWindow("result", cv2.WINDOW_NORMAL)
#    cv2.imshow("result", result)
#    if isOutput:
#        out.write(result)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
