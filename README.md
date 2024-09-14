# it’s a hot dog, and a not hot dog, it’s technology

For the Hotdog-Not-Hotdog-Classifier from the series Silicon Valley, these steps were performed:

## 1. Download images from ImageNet

get_imgs.py downloads 13 synsets from ImageNet. 

**Hotdog Class**
- the actual hotdog class
  
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
