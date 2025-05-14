import os
import random
import shutil
import cv2
from skimage import io
import numpy as np
from PIL import Image
filer=r"D:\yolov11\ultralytics-main\4.1.0"


def tif_jpg_transform(file_path_name, bgr_savepath_name):
    with Image.open(file_path_name) as img:
        img = img.convert('RGB')
        img.save(bgr_savepath_name, "JPEG")
        img.close()
  # 图片存储


'''for file in os.listdir(filer):
   if file[-3:]=='tif'or file[-3:]=='TIF':
        img=Image.open(filer+'\\'+file)
        img = img.convert('RGB')
        #img.save(r'D:\yolov11\temp', "JPEG")
        img.save('D:\\yolov11\\temp\\'+file,"JPEG")
        img.close()



for file in os.listdir(r'D:\yolov11\temp'):
    shutil.move(r'D:\yolov11\temp'+'\\'+file, filer+'\\'+file)
'''
'''
for file in os.listdir(filer):
    if file[-3:] == 'jpg' or file[-3:] == 'tif':
        try:
        #print(filer+file)
            image = cv2.imread(filer+'\\'+file, cv2.IMREAD_GRAYSCALE)
            cv2.imwrite(filer+'\\'+file, image)
        except:
            print('error:'+file)'''


def split_dataset(srcDir, trainDir, valDir,testDir ,split_ratio1=0.6,split_ratio2=0.3):
    """
    将数据集划分为训练集和验证集，并保存到相应的文件夹中。

    Parameters:
    - srcDir: 原始数据集文件夹路径，包含图像和标签文件。
    - trainDir: 训练集文件夹路径，包含 'images' 和 'labels' 子文件夹。
    - valDir: 验证集文件夹路径，包含 'images' 和 'labels' 子文件夹。
    - split_ratio: 数据集划分比例，默认为 0.9，表示将 90% 的数据用于训练集，10% 用于验证集。
    """
    os.makedirs(os.path.join(trainDir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(trainDir, 'labels'), exist_ok=True)
    os.makedirs(os.path.join(valDir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(valDir, 'labels'), exist_ok=True)
    os.makedirs(os.path.join(testDir, 'images'), exist_ok=True)
    os.makedirs(os.path.join(testDir, 'labels'), exist_ok=True)

    # 获取数据集中所有文件的列表
    file_list = os.listdir(srcDir)
    random.shuffle(file_list)

    # 根据划分比例计算训练集和验证集的边界索引
    split_index1 = int(len(file_list) * split_ratio1)
    split_index2 =int(len(file_list) * (split_ratio2+split_ratio1))

    train_files = file_list[:split_index1]
    val_files = file_list[split_index1:split_index2]
    test_files = file_list[split_index2:]
    print(file_list)
    # 将训练集数据移动到相应文件夹
    for file in train_files:
        if file.endswith('.jpg') or file.endswith('.tif'):
            img_src = os.path.join(srcDir, file)
            label_src = os.path.join(srcDir, file[:-4] + '.txt')
            shutil.move(img_src, os.path.join(trainDir, 'images', file))
            #print(trainDir, label_src)
            try:
                shutil.move(label_src, os.path.join(trainDir, 'labels', file[:-4] + '.txt'))
            except:
                print(file[:-4] + '.txt'+'not found')

    # 将验证集数据移动到相应文件夹
    for file in val_files:
        if file.endswith('.jpg')or file.endswith('.tif'):
            img_src = os.path.join(srcDir, file)
            label_src = os.path.join(srcDir, file[:-4] + '.txt')
            shutil.move(img_src, os.path.join(valDir, 'images', file))
            try:
                shutil.move(label_src, os.path.join(valDir, 'labels', file[:-4] + '.txt'))
            except:
                print(file[:-4] + '.txt'+'not found')
    for file in test_files:
        if file.endswith('.jpg')or file.endswith('.tif'):
            img_src = os.path.join(srcDir, file)
            label_src = os.path.join(srcDir, file[:-4] + '.txt')
            shutil.move(img_src, os.path.join(testDir, 'images', file))
            try:
                shutil.move(label_src, os.path.join(testDir, 'labels', file[:-4] + '.txt'))
            except:
                print(file[:-4] + '.txt'+'not found')

if __name__ == '__main__':
    # 输入文件夹路径
    srcDir = r"D:\yolov11\ultralytics-main\origindata\enhancedimages"
    trainDir = r'D:\yolov11\ultralytics-main\3.6.0\train'#r'D:\yolov11\ultralytics-main\graybeandataset\train'
    valDir =r'D:\yolov11\ultralytics-main\3.6.0\val' #r'D:\yolov11\ultralytics-main\graybeandataset\val'
    testDir = r'D:\yolov11\ultralytics-main\3.6.0\test'#r'D:\yolov11\ultralytics-main\graybeandataset\test'
    # 调用函数划分数据集
    split_dataset(srcDir, trainDir, valDir,testDir)