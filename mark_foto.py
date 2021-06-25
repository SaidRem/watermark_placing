import os
import sys
from pathlib import Path
from PIL import Image

def watermarking(photos_folder, watermark):
    """Marks all fotos (.png) in the photos_folder with
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

