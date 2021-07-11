import os
import sys
import re
from pathlib import Path
from PIL import Image

def png_marking(photos_folder, watermark):
    """Marks fotos (only png) in the photos_folder with
    watermark.
    :param photos_folder: Abs path to a folder with photos for watermarking.
    :param watermark: Abs path to the watermark image file.
    """
    os.makedirs('watermarked', exist_ok=True)
    photos = list(filter(lambda x: x.endswith('.png'), os.listdir(photos_folder)))
    for photo in photos:
        with Image.open(Path(photos_folder, photo)) as img, Image.open(Path(watermark)).convert('L') as wat:
            width, height = img.size
            wat_width, wat_height = wat.size
            img.paste(wat, (int((width/2)-(wat_width/2)), int((height/2)+(wat_height/2))), wat)
            img.save(Path('watermarked', f'{Path(photo).stem}_mrkd.png'))
    return f'Photos watermarked => {", ".join(photos)}'

def all_marking(photos_folder, watermark):
    """Marks all fotos (png, jpg, jpeg, gif) in the photos_folder with
    watermark.
    :param photos_folder: Abs path to a folder with photos for watermarking.
    :param watermark: Abs path to the watermark image file.
    """
    pat = re.compile(r'^.*\.((png)|(jpg)|(jpeg)|(gif))$')
    os.makedirs('watermarked', exist_ok=True)
    photos = list(filter(lambda x: pat.match(x), os.listdir(photos_folder)))
    for photo in photos:
        with Image.open(Path(photos_folder, photo)) as img, Image.open(Path(watermark)).convert('L') as wat:
            width, height = img.size
            wat_width, wat_height = wat.size
            img.paste(wat, (int((width/2)-(wat_width/2)), int((height/2)+(wat_height/2))), wat)
            img.save(Path('watermarked', f'{Path(photo).stem}_mrkd.png'))
    return f'Photos watermarked => {", ".join(photos)}'

def add_logo(photo, logo):
    """
    Mark photo with logo.
    :param photo: Path to photo for marking.
    :param logo: Path to logo.
    """
    im = Image.open(photo)
    logo_im = Image.open(logo)
    im_width, im_height = im.size
    logo_width, logo_height = logo_im.size
    if (logo_width*10 > im_width) or (logo_height*10 > im_height):
        logo_width = logo_width//10
        logo_height = logo_height//10
    im.paste(logo_im, (im_width-logo_width, im_height-logo_height), logo_im)
    im.save(f'{Path(photo).stem}_lg.png')
    return "Logo added successfully."
