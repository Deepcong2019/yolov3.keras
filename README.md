1、本仓库在https://github.com/qqwweee/keras-yolo3 ，和https://github.com/Cartucho/mAP 的基础上稍作修改，实现yolov3的训练、验证、测试（基于
   coco2017的训练集train2017（总共118287张图片，含有目标的图片共117266张，共860001个目标框。），验证集val2017（总共5000张图片，其中4952张含有目       标，共有36781个目标框））。

2、coco数据集目标检测含有80个目标种类：

     names_list = ['person','bicycle', 'car', 'motorbike', 'aeroplane', 'bus', 'train', 
                   'truck', 'boat', 'trafficlight', 'firehydrant', 'stopsign', 'parkingmeter', 
                   'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 
                   'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 
                   'sportsball', 'kite', 'baseballbat', 'baseballglove', 'skateboard', 'surfboard', 'tennisracket', 
                   'bottle', 'wineglass', 'cup', 'fork', 'knife', 'spoon', 'bowl',   'banana','apple','sandwich',
                   'orange','broccoli','carrot','hotdog','pizza','donut','cake','chair','sofa','pottedplant','bed',
                   'diningtable','toilet','tvmonitor','laptop', 'mouse', 'remote', 'keyboard', 'cellphone', 'microwave', 
                   'oven', 'toaster', 'sink', 'refrigerator','book','clock','vase', 'scissors', 'teddybear', 
                   'hairdrier', 'toothbrush']
              
      id_list = [1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 13, 14, 15, 16,
                 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28,31, 32, 33,
                 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50,
                 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 67,
                 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 84,85, 86, 87, 88, 89, 90]
           
3、具体操作步骤：

#下载数据集：

coco数据集下载地址：https://pan.baidu.com/s/1bkZqLk_uB0-KeNdFndfwMA 密码:l1yl

voc数据集下载地址： https://pan.baidu.com/s/1SKZcQDUdKTDx95mfFugD3Q  密码:hr9e
            
