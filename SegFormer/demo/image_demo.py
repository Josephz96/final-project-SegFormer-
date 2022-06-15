from argparse import ArgumentParser

from mmseg.apis import inference_segmentor, init_segmentor, show_result_pyplot
from mmseg.core.evaluation import get_palette
import os
import cv2
import time

# 图片合成视频
def picvideo(path, size):
    filelist = os.listdir(path)
    filelist.sort(key=lambda x: int(x.split('.')[0]))
    total_num = len(filelist)  # 获取文件长度（文件夹下图片个数）
    '''
    fps:
    帧率：1秒钟有n张图片写进去[控制一张图片停留5秒钟，那就是帧率为1，重复播放这张图片5次] 
    如果文件夹下有50张 749*677的图片，这里设置1秒钟播放5张，那么这个视频的时长就是10秒
    '''
    fps = 10

    file_path = "/home/nfzhang/finalassihnment/problem1new/SegFormer" + str(int(time.time())) + ".avi"  # 导出路径
    fourcc = cv2.VideoWriter_fourcc('I', '4', '2', '0')  # 不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）

    video = cv2.VideoWriter(file_path, fourcc, fps, size)
    for item in filelist:
        if item.endswith('.png'):  # 判断图片后缀是否是.png
            item = path + '/' + item
            img = cv2.imread(item)  # 使用opencv读取图像，直接返回numpy.ndarray 对象，通道顺序为BGR ，注意是BGR，通道值默认范围0-255。

            video.write(img)  

    video.release()  
    # cap=cv2.VideoCapture

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('img', help='Image file')
    parser.add_argument('config', help='Config file')
    parser.add_argument('checkpoint', help='Checkpoint file')
    parser.add_argument(
        '--device', default='cuda:0', help='Device used for inference')
    parser.add_argument(
        '--palette',
        default='cityscapes',
        help='Color palette used for segmentation map')
    args = parser.parse_args()

    # build the model from a config file and a checkpoint file
    model = init_segmentor(args.config, args.checkpoint, device=args.device)

    #filelist = os.listdir('/home/nfzhang/finalassihnment/problem1new/dashcam')  # 获取文件路径
    #filelist.sort(key=lambda x: int(x.split('.')[0]))
    #total_num = len(filelist)  
    #for item in filelist:
    #    print(item)
    #    if item.endswith('.jpg') or item.endswith('.png'):
    #        newImgSavePath = os.path.join('/home/nfzhang/finalassihnment/problem1new/SegFormer/demo/demosave', item)
    #        # test a single image
    #        readImgPath = os.path.join('/home/nfzhang/finalassihnment/problem1new/dashcam', item)
    #        result = inference_segmentor(model, readImgPath)
            # show the results
    #        show_result_pyplot(model, readImgPath, result, newImgSavePath, get_palette(args.palette))

    path = '/home/nfzhang/finalassihnment/problem1new/SegFormer/demo/demosave'
    # 文件路径
    size = (1920, 1080)
    picvideo(path, size)
