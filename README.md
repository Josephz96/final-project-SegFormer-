## 运用SegFormer对行车记录仪视频进行语义分割并可视化
---

## 目录
1. [所需环境](#所需环境)
2. [文件下载](#文件下载)
3. [将MP4视频转换为序列帧图片](#将MP4视频转换为序列帧图片)
4. [对序列帧图片进行推断](#对序列帧图片进行推断)
5. [合成经过语义分割后的行车记录仪视频](#合成经过语义分割后的行车记录仪视频)
6. [参考资料](#Reference)


## 所需环境
CUDA == 10.1 
pytorch == 1.7.1
torchvision == 0.8.2
timm == 0.3.2
mmcv-full == 1.2.7
opencv-python == 4.5.1.48

## 文件下载
经过CityScapes训练的权值文件segformer.b5.1024x1024.city.160k.pth从如下链接中下载
链接：https://drive.google.com/drive/folders/1GAku0G0iR9DsBxCbfENWMJ27c5lYUeQA
下载后的文件放在\SegFormer\local_configs\segformer\B5 文件夹下

## 将MP4视频转换为序列帧图片
1. 视频准备
准备好需要可视化的MP4格式的行车记录仪视频   
  
2. 视频转序列帧图片  
修改sourceFileName='要提取视频的文件名'，修改frameFrequency='提取视频的频率'，本作业中该值取4。修改完成后运行videophoto.py文件即可开始视频转序列帧图片

3. 查看结果  
程序运行结束后，会生成与提取的视频同名的文件夹，序列帧图片已经按编号顺序在该文件夹中生成。   
 
 
## 对序列帧图片进行推断
1. 修改iamge_demo.py文件
打开 \SegFormer\demo\image_demo.py文件，根据需求调整fps的值，本作业中fps=10。将该文件的第51-62行取消注释，同时将第64-67行进行注释。

2. 开始推断
修改完成后运行代码：
python demo/image_demo.py /home/nfzhang/finalassihnment/problem1new/SegFormer/demo/demosave local_configs/segformer/B5/segformer.b5.1024x1024.city.160k.py segformer.b5.1024x1024.city.160k.pth --device cuda:0 --palette cityscapes
（根据实际文件位置进行相应调整）
运行结束后，经过语义分割的图片将被存放在demo文件夹下的demosave文件夹中

## 合成经过语义分割后的行车记录仪视频
1. 修改image_demo.py文件
打开 \SegFormer\demo\image_demo.py文件，将该文件的第51-62行进行注释，同时将第64-67行取消注释。第66行代码的size设置根据序列帧图片的实际大小进行调整。本作业中使用的视频转换为的序列帧图片大小为1920*1080。

2. 合成视频
修改完成后运行代码：
python demo/image_demo.py /home/nfzhang/finalassihnment/problem1new/SegFormer/demo/demosave local_configs/segformer/B5/segformer.b5.1024x1024.city.160k.py segformer.b5.1024x1024.city.160k.pth --device cuda:0 --palette cityscapes
（根据实际文件位置进行相应调整）
运行结束后，合成的视频将生成在根目录下。

## Reference
https://github.com/NVlabs/SegFormer
https://github.com/open-mmlab/mmsegmentation/tree/master/configs/segformer