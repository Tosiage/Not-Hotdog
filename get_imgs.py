import os
import urllib.request


def download_imgs(d_paths, l_paths):
    for path, local in  zip(d_paths, l_paths):
        if not os.path.exists(local):
            os.makedirs(local)
        urllib.request.urlretrieve(path)

######## start ###########

download_paths = ['https://image-net.org/data/winter21_whole/n07697537.tar', #hotdog 
                 'https://image-net.org/data/winter21_whole/n03201208.tar', #dining table
                 'https://image-net.org/data/winter21_whole/n03461385.tar'] #grocery store

local_paths = ['hotdog', 'dining_table', 'grocery_store']

download_imgs(download_paths, local_paths)