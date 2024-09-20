# YOLOv8-Multi-Modal-Fusion-Network-RGB-IR-
## 一、参数说明
在YOLOv8源码的基础上，此代码新增参数如下：  
改为3即变为原YOLOv8模型,6则为RGB+红外,只能3或6其他通道数会报错，两个文件修改要保持一致
1. 训练配置文件：ultralytics/cfg/default.yaml
```
ch: 6 # 6 or 3
```
2. 模型配置文件：ultralytics/cfg/models/v8/yolov8.yaml
```
ch: 6 # 6 or 3
```

## 二、数据集准备
数据集文件夹需严格按下面命名：
```
|-datasets
    |-LLVIP700
        |-images
        |-image  # 额外的图片文件夹，放红外图
        |-labels
```
代码基于YOLOv8官方代码实现，除以上新增参数，训练、改模型等任何操作均与YOLOv8官方代码完全一致
## 三、训练/验证/检测
运行main.py即可  
提供了一个在LLVIP数据集上训练好的多模态预训练权重.pt  
提供了700张LLVIP数据集用来测试跑通
