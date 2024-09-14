import os
import cv2
import shutil
import random

def select_random_nothotdog(path, dst_path):
    nothotdog_path = path + "/not-hotdog/"
    dst_nothotdog_path = dst_path + "/not-hotdog/"
    img_folders = os.listdir(nothotdog_path)
    print(img_folders)
    if not os.path.exists(dst_nothotdog_path):
        os.makedirs(dst_nothotdog_path)

    picture_list = []
    while len(picture_list) < 1257:
        folder = random.choice(img_folders)
        img = random.choice(os.listdir(nothotdog_path + folder + "/"))
        img_path = nothotdog_path + folder + "/" + img
        picture_list.append(img_path)
        picture_list = list(dict.fromkeys(picture_list)) #remove duplicates
    ctr = 0
    for file in picture_list:
        shutil.copy(file, dst_nothotdog_path + str(ctr) + ".JPEG")
        ctr = ctr+1
   



def copy_hotdog(path, dst_path):
    imgs = os.listdir(path + "/hotdog/")
    if not os.path.exists(dst_path + "/hotdog/"):
        os.makedirs(dst_path + "/hotdog/")
        for file in imgs:
            shutil.copy(path + "/hotdog/" + file, dst_path + "/hotdog/" + file)

##### start ######

raw_imgs = "raw_imgs"
classes_path = "classes"

copy_hotdog(raw_imgs, classes_path)
select_random_nothotdog(raw_imgs, classes_path)

