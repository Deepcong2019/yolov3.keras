1、在https://github.com/qqwweee/keras-yolo3 ，和https://github.com/Cartucho/mAP 的基础上稍作修改，实现yolov3的训练、验证、测试（基于coco2017的训练集train2017（总共118287张图片，含有目标的图片共117266张，共860001个目标框。），验证集val2017（总共5000张图片，其中4952张含有目标，共有36781个目标框。））。

2、coco数据集目标检测含有80个目标种类：
 names_list = ['person','bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 
              'truck', 'boat', 'trafficlight', 'firehydrant', 'stopsign', 'parkingmeter', 
              'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 
              'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 
              'sportsball', 'kite', 'baseballbat', 'baseballglove', 'skateboard', 'surfboard', 'tennisracket', 
              'bottle', 'wineglass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange','broccoli',
              'carrot', 'hotdog', 'pizza', 'donut', 'cake', 'chair', 'sofa','pottedplant','bed','diningtable','toilet','tvmonitor',
              'laptop', 'mouse', 'remote', 'keyboard', 'cellphone', 'microwave', 'oven', 'toaster', 'sink', 
              'refrigerator','book','clock','vase', 'scissors', 'teddybear', 'hairdrier', 'toothbrush']
              
              
具体操作步骤：
            
