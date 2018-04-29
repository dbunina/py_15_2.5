# Run from any folder to convert all images in it to new size.
# New image will be located in 'result' folder which will is created on the same level as source folder.
##
# HOW TO USE:
##
# * When python program is run in target directory:
# > C:\...\convert.py .
#
# * Using relative path (separator valid for Windows):
# > C:\...\convert.py some\dir\source
#
# * Using absolute path (separator valid for Windows):
# > C:\...\convert.py C:\some\dir\source

import os
import sys
import subprocess


def convert():
    cwd = os.getcwd()

    src_file = sys.argv[1]

    src_folder = os.path.join(cwd, src_file)
    target_folder = os.path.join(src_folder, 'result')

    if not os.path.exists(target_folder):
        print('Creating result folder: {}'.format(target_folder))
        os.makedirs(target_folder)

    for file in os.listdir(src_folder):
        src_file = os.path.join(src_folder, file)
        if os.path.isfile(src_file):
            target_file = os.path.join(target_folder, file)
            print('Converting file {}'.format(src_file))

            subprocess.call('magick {source_file} -resize 200 {target_file}'
                            .format(source_file=src_file, target_file=target_file))
    print('Done')


convert()
