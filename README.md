* 本仓库在https://github.com/qqwweee/keras-yolo3 和 https://github.com/Cartucho/mAP 的基础上稍作修改，实现yolov3的训练、验证、测试。（基于coco2017的训练集train2017（总共118287张图片，含有目标的图片共117266张，共860001个目标框），验证集val2017（总共5000张图片，其中4952张含有目标，共有36781个目标框））。

* coco数据集目标检测含有80个目标种类：

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
           
# 具体操作步骤：

## 一、执行训练操作步骤

### 1、下载数据集

   * coco数据集下载地址：https://pan.baidu.com/s/1bkZqLk_uB0-KeNdFndfwMA 密码:l1yl
   * voc数据集下载地址： https://pan.baidu.com/s/1SKZcQDUdKTDx95mfFugD3Q  密码:hr9e
   * 以coco数据集为例存放路径为：<br>
   |--coco<br>
   |　　|--train2017<br>
   |　　|-- val2017<br>
   |　　|-- annotations<br>
   |　　　　|-- instances_train2017.json<br>
   |　　　　|--instances_val2017.json
   
### 2、 生成训练所要的train.txt

   * 运行 python coco_annotation.py，生成train.txt
   
### 3、生成适合数据集的anchors

   * 运行 python kmeans.py，生成适合数据集的anchors，保存在model_data/yolo_anchors.txt中
   
### 4、下载预训练模型

   * wget https://pjreddie.com/media/files/yolov3.weights 
      
### 5、将模型转化为keras的h5模型格式

   * 运行 python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
   * 或者直接跳跃步骤4和5，直接从百度网盘下载h5模型：链接：https://pan.baidu.com/s/1Ok-8gSGvhzRdjXNL_W0ZGw 密码：x7qn
   
### 6、执行训练

   * 运行 python train.py，进行训练
   
## 二、计算mAP操作步骤（以val2017为例） 

### 1、json转xml格式

   * 运行 python json2xml.py
   * 运行之后，生成的图片存入mAP/input/images-optional，共4952张，生成的xml存入mAP/input/ground-truth
   
### 2、xml格式转为txt

   * 运行 python mAP/scripts/extra/convert_gt_xml.py，将xml转为txt。
　 * 形如<class_name> <left> <top> <right> <bottom>
      
### 3、对mAP/input/images-optional中的图片进行检测

   * 检测结果的txt文本存入mAP/input/detection-results，图片上直接标注结果存入mAP/input/image_detect_results。
  
### 4、计算mAP

   * 运行 python mAP/main.py，计算模型在验证集val2017的mAP。
   
 ## 三、对单张图片或者视频进行检测
 
 ### 1、对单张图片进行检测
   
   * 运行 python yolo_video.py --image，对单张图片进行检测。
 ### 2、对视频进行检测
   * 运行 python yolo_video.py --input xxx.mp4 --output yyy.mp4
