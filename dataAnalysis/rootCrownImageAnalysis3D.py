'''
Created on Sep 20, 2018

@author: njiang
'''

import os, argparse
import numpy as np
import cv2 as cv


def image2Points(img, sliceID = 0):
    indices = np.nonzero(img)
    if not indices.size == 0:
        num = indices.shape[1]
        pts = np.zeros((num, 3))
        pts[:, 0] = indices[0]
        pts[:, 1] = indices[1]
        pts[:, 2] = sliceID
        return pts, num

def options():
    
    parser = argparse.ArgumentParser(description='Root Crown Image Analysis',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('-i', "--input_folder", help="directory of image slices", required=True)
    parser.add_argument('-s', "--sampling", help="resolution parameter", required=True)
    parser.add_argument('-t', "--thickness", help="slice thickness in mm", required=True)
    
    args = parser.parse_args()

    return args

args = options()
original_folder = args.input_folder
scale = float(args.scale)*float(args.thickness)

list_dirs = os.walk(original_folder)
for root, dirs, files in list_dirs:
    for subfolder in dirs:       
        for s_root, s_dirs, s_files in os.walk(os.path.join(original_folder, subfolder)):
            s_files.sort(key=lambda x: (-x.count('/'), x), reverse = False)
            z = 0
            for img_name in s_files:
                if os.path.splitext(img_name)[1] == '.png':
                    img = cv.imread(os.path.join(original_folder, subfolder, img_name), cv.IMREAD_GRAYSCALE)
                    pts, num = image2Points(img, z)
                    
                    
