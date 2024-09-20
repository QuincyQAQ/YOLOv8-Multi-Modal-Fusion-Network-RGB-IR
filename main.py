from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO(r"ultralytics/cfg/models/v8/zhongjianronghe.yaml")
    model.train(data=r"ultralytics/cfg/datasets/mydata.yaml")  # 训练

    # model = YOLO(r"多模态预训练权重.pt")
    # model.val(data=r"ultralytics/cfg/datasets/mydata.yaml",batch=1)  # 验证
    # model.predict(source=r"datasets/LLVIP700/images/val", save=True)  # 检测
