
#!/usr/bin/env python3
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os
import argparse

path = './images'
pathOut = './edited-images'


parser = argparse.ArgumentParser(description='Git-Initializer, a simple python script to initialize a git repository\n. Use without any arguments to run the script in interactive mode')
parser.add_argument('-s', '--sharpen', action='store_true', help='Sharpen Image')
parser.add_argument('-g', '--grayscale', action='store_true', help='Turn image into grayscale mode')
parser.add_argument('-c', '--contrast', action='store_true', help='Add contrast')
parser.add_argument('-d', '--dcontrast', action='store_true', help='Add contrast')
parser.add_argument('-r', '--round', action='store_true', help='Add contrast')


args = parser.parse_args()

def main_script(args):
    if(args.contrast and args.dcontrast):
        print("You can't increase and decrease contrast at the same time\n")
        exit()
    for filename in os.listdir(path):
        img = Image.open(f"{path}/{filename}")
        edit = img
        
        # Sharpen
        if (args.sharpen):
            edit = img.filter(ImageFilter.SHARPEN)

        # GrayScale Mode
        if (args.grayscale):
            edit = edit.convert('L')

        # Increase contrast
        if (args.contrast or args.dcontrast):
            if args.contrast:
                factor = 1.5
            else:
                factor = 0.8
            enhancer = ImageEnhance.Contrast(edit)
            edit = enhancer.enhance(factor)
        
        if (args.round):
            mask = Image.open('round-mask.png').convert('L')
            edit = ImageOps.fit(edit,mask.size,centering=(0.5,0.5))
            edit.putalpha(mask)

        # Export
        clean_name = os.path.splitext(filename)[0]

        edit.save(f'{pathOut}/{clean_name}_edited.png')

if (args):
    main_script(args)
else:
    print("Use -h argument for usage instructions")