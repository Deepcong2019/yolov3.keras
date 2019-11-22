import xml.etree.ElementTree as ET
from os import getcwd

sets=[('2017', 'train')]

classes  = ['person','bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 
              'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 
              'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 
              'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 
              'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 
              'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange',
              'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table',
              'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 
              'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']


def convert_annotation(year, image_id, list_file):
    in_file = open('/home/cong/ssd-Tensorflow/datasets/coco2017/%s%s/Annotations/%s.xml'%(image_set,year, image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

#wd = getcwd()

for year, image_set in sets:
    image_ids = open('./coco2017/%s%s.txt'% (image_set,year)).read().strip().split()
    list_file = open('%s_%s.txt'%(image_set,year), 'w')
    for image_id in image_ids:
        list_file.write('/home/cong/ssd-Tensorflow/coco2017/%s%s/JPEGImages/%s.jpg'%(image_set, year, image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()

