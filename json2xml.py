#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 10:13:48 2019

@author: cong
"""
"""
#read json
import json
json_file = '/media/cong/娱乐/coco2017/annotations/image_info_test2017.json'
val=json.load(open(json_file, 'r'))
#
##
bb=[]
a=val['annotations']
for i in a:
    b=i['category_id']
    bb.append(b)
"""
#coding:utf-8
'''
Read annotations list
for ant in annotations_list:
    if cat in cats:
        get imname
        if imnum.jpg in impath:
            add object to imnum.xml
        else:
            copy imname.jpg as imnum.jpg to impath
            make imnum.xml
            add object to imnum.xml
TO DO: make txt files as well as xml
'''
import os
import json
import cv2
from lxml import etree
import xml.etree.cElementTree as ET
import time



id_list = [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28,31, 32, 33,
           34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50,
           51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67,
           70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84,85, 86, 87, 88, 89, 90]

names_list = ['person','bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 
              'truck', 'boat', 'trafficlight', 'firehydrant', 'stopsign', 'parkingmeter', 
              'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 
              'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 
              'sportsball', 'kite', 'baseballbat', 'baseballglove', 'skateboard', 'surfboard', 'tennisracket', 
              'bottle', 'wineglass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange',
              'broccoli', 'carrot', 'hotdog', 'pizza', 'donut', 'cake', 'chair', 'sofa', 'pottedplant', 'bed', 'diningtable',
              'toilet', 'tvmonitor', 'laptop', 'mouse', 'remote', 'keyboard', 'cellphone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 
              'book', 'clock', 'vase', 'scissors', 'teddybear', 'hairdrier', 'toothbrush']




im_ext = 'jpg'
COCO_images = '/media/cong/娱乐/coco2017/val2017/'
Json_addr = '/media/cong/娱乐/coco2017/annotations/instances_val2017.json'
im_num = 0
ob_count = 0
im_pairs = dict()

main_dir = 'mAP/input'

if not os.path.isdir(main_dir):
    os.mkdir(main_dir)


xml_dir = os.path.join(main_dir, 'ground-truth')   
if not os.path.isdir(xml_dir):
    os.mkdir(xml_dir)

im_dir = os.path.join(main_dir, 'images-optional')   
if not os.path.isdir(im_dir):
    os.mkdir(im_dir)


print('Reading JSON ...')

with open(Json_addr) as json_data:
    annotation_list = json.load(json_data)

start_time = time.time()
print('--- Start Operation ---', start_time)

for i in range(0, len(annotation_list["annotations"])):
    category_id = annotation_list["annotations"][i]["category_id"]

    if category_id in id_list:
        # print('HIT -->', im_num)
        cat_name = names_list[id_list.index(category_id)]
        im_id = (str(annotation_list["annotations"][i]["image_id"]))
        xmin = int(annotation_list["annotations"][i]["bbox"][0])
        ymin = int(annotation_list["annotations"][i]["bbox"][1])
        xmax = int(xmin+annotation_list["annotations"][i]["bbox"][2])
        ymax = int(ymin+annotation_list["annotations"][i]["bbox"][3])

        z = '0'
        for sf in range((len(im_id)), 11):   # imname 12 basamaklı olması için
            z = z + "0"
        im_name = z + im_id

        if os.path.exists(os.path.join(im_dir, str(im_pairs.get(im_name, 'None')) + '.' + im_ext)):
            # ---add object to imnum.xml---

            # read the xml root
            tree = ET.parse(os.path.join(xml_dir, str(im_pairs[im_name]) + '.xml'))
            root = tree.getroot()

            # Convert root to etree

            xml_str = ET.tostring(root)
            troot = etree.fromstring(xml_str)  # etree object

            # create new object element
            ob = etree.Element('object')
            etree.SubElement(ob, 'name').text = cat_name
            etree.SubElement(ob, 'pose').text = 'Unspecified'
            etree.SubElement(ob, 'truncated').text = '0'
            etree.SubElement(ob, 'difficult').text = '0'

            bbox = etree.SubElement(ob, 'bndbox')
            etree.SubElement(bbox, 'xmin').text = str(xmin)
            etree.SubElement(bbox, 'ymin').text = str(ymin)
            etree.SubElement(bbox, 'xmax').text = str(xmax)
            etree.SubElement(bbox, 'ymax').text = str(ymax)

            # prettify the object
            xml_str = etree.tostring(ob, pretty_print=True)
            ob_pretty = etree.fromstring(xml_str)

            # append etree object to etree root(troot)
            troot.append(ob_pretty)

            # overwrite the old xml
            xml_str = etree.tostring(troot, pretty_print=True)

            with open(os.path.join(xml_dir, str(im_pairs[im_name]) + '.xml'), 'wb') as output:
                output.write(xml_str)

            print('--- Added {} to '.format(cat_name), str(im_pairs[im_name]) + '.xml' ' ---')

        else:

            # Copy image as im_num.jpg
            with open(os.path.join(COCO_images, im_name + '.' + im_ext), 'rb') as rf:
                with open(os.path.join(im_dir, str(im_num) + '.' + im_ext), 'wb') as wf:
                    for line in rf:
                        wf.write(line)
            # make imnum.xml

            # -get imsize(widht, height, depth)

            # Resimlerin olduğu klasör
            im_cv2 = cv2.imread(os.path.join(COCO_images, im_name + '.' + im_ext))
            height, width, depth = im_cv2.shape
            if depth==2:
                print(depth)

            # Form the file

            annotation = ET.Element('annotation')
            ET.SubElement(annotation, 'folder').text = im_dir
            ET.SubElement(annotation, 'filename').text = str(im_num) + '.' + im_ext
            ET.SubElement(annotation, 'segmented').text = '0'
            size = ET.SubElement(annotation, 'size')
            ET.SubElement(size, 'width').text = str(width)
            ET.SubElement(size, 'height').text = str(height)
            ET.SubElement(size, 'depth').text = str(depth)

            ob = ET.SubElement(annotation, 'object')
            ET.SubElement(ob, 'name').text = cat_name
            ET.SubElement(ob, 'pose').text = 'Unspecified'
            ET.SubElement(ob, 'truncated').text = '0'
            ET.SubElement(ob, 'difficult').text = '0'

            bbox = ET.SubElement(ob, 'bndbox')
            ET.SubElement(bbox, 'xmin').text = str(xmin)
            ET.SubElement(bbox, 'ymin').text = str(ymin)
            ET.SubElement(bbox, 'xmax').text = str(xmax)
            ET.SubElement(bbox, 'ymax').text = str(ymax)

            # Save the file

            xml_str = ET.tostring(annotation)
            root = etree.fromstring(xml_str)
            xml_str = etree.tostring(root, pretty_print=True)  # Entire content of the xml

            save_path = os.path.join(xml_dir, str(im_num) + '.' + 'xml')  # Create save path with imnum.xml

            with open(save_path, 'wb') as temp_xml:
                temp_xml.write(xml_str)
            # keep record of which xml is paired with which image from coco_Set
            im_pairs[im_name] = im_num

            print('Copied imfile--> {} --- Object count--> {}'.format(str(im_num) + '.' + im_ext, ob_count))

            im_num += 1
        ob_count += 1
print('Finished with {} objects in {} images in {} seconds'.format(ob_count, im_num, time.time() - start_time))
