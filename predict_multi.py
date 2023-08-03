from PIL import Image
from deeplab import DeeplabV3
import os
from tqdm import tqdm

deeplab = DeeplabV3()

dir_origin_path= "img"
dir_save_path = "img_out"

if not os.path.exists(dir_save_path):
    os.makedirs(dir_save_path)

a=[]
i = 0

img_names = os.listdir(dir_origin_path)
for img_name in tqdm(img_names):
    if img_name.lower().endswith(('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
        image_path = os.path.join(dir_origin_path, img_name)
        image = Image.open(image_path)
        r_image = deeplab.detect_image(image)
        if not os.path.exists(dir_save_path):
            os.makedirs(dir_save_path)
        r_image.save(os.path.join(dir_save_path, img_name))
