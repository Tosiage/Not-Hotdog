# it’s a hot dog, and a not hot dog, it’s technology

For the Hotdog-Not-Hotdog-Classifier from the series Silicon Valley, these steps were performed:

## 1. Download images from ImageNet

get_imgs.py downloads 13 synsets from ImageNet. 

**Hotdog Class**
- the actual hotdog class
- 1257 elements
  
**Not-Hotdog Classes (food related)**
- Cheeseburger: Similar fast food, but clearly distinguishable from a hotdog
- Bagel: Circular bread items that can sometimes resemble a hotdog bun, especially in small images
- Pizza: Another popular fast food
- Ice Cream: A dessert food class that is visually distinct from a hotdog but still part of food datasets
- Burrito: Similar shape but typically wrapped differently than a hotdog
- Bell Pepper: A non-fast food item that has a long shape but is easily distinguishable
- Grocery Store: A lot of different food items together
  
**Not-Hotdog Classes (not food related)**
- Beer Bottle: Cylindrical shape but unrelated to food
- Mixing Bowl: Kitchen-related but not food
- Dinner Table: Table that food gets placed on
- Cauldron: Different types of bowls
- Wig: Something completely unrelated to food

## 2. Preprocessing

Following preprocessing steps were done in preproc.py:

1. Select 1257 random images from Not-Hotdog classes
2. Resizing
3. Normalization
5. Ensure Proper Image Shape
6. Data Batching
7. Label Encoding

## 3. Model creation

I used a pre-trained model in the first run.

## 4. Transfer Learning

Because my dataset is quite small, I used transfer learning on the pre-trained model.
