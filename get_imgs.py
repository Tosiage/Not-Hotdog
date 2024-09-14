import os
import urllib.request


def download_imgs(d_paths, l_paths):
    for path, local in  zip(d_paths, l_paths):
        if not os.path.exists("raw_imgs/" + local):
            os.makedirs("raw_imgs/" + local)
            urllib.request.urlretrieve(path, "raw_imgs/" + local + "/" + local + ".tar")

######## start ###########

download_paths = ['https://image-net.org/data/winter21_whole/n07697537.tar', #(hotdog) 
                 'https://image-net.org/data/winter21_whole/n03201208.tar', #(dining table)
                 'https://image-net.org/data/winter21_whole/n03461385.tar', #(grocery store)
                 'https://image-net.org/data/winter21_whole/n07697313.tar', #(cheeseburger)
                 'https://image-net.org/data/winter21_whole/n07693725.tar', #(bagel, beigel)
                 'https://image-net.org/data/winter21_whole/n07873807.tar', #(pizza, pizza pie)
                 'https://image-net.org/data/winter21_whole/n07615774.tar', #(ice cream, icecream)
                 'https://image-net.org/data/winter21_whole/n07880968.tar', #(burrito)
                 'https://image-net.org/data/winter21_whole/n07720875.tar', #(bell pepper, capsicum)
                 'https://image-net.org/data/winter21_whole/n02823750.tar', #(beer bottle)
                 'https://image-net.org/data/winter21_whole/n04584207.tar', #(wig)
                 'https://image-net.org/data/winter21_whole/n02939185.tar', #(caldron, cauldron)
                 'https://image-net.org/data/winter21_whole/n03775546.tar'] #(mixing bowl)

local_paths = ['hotdog', 'dining_table', 'grocery_store', 'cheeseburger', 'bagel', 'pizza', 'icecream', 'burrito', 'bellpepper', 'bottle', 'wig', 'cauldron', 'bowl']

download_imgs(download_paths, local_paths)