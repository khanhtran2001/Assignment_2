import cv2
import glob
from skimage.transform import AffineTransform,warp,rotate
from scipy import ndimage
from skimage import util
from skimage.color import rgb2gray
from skimage.util import random_noise

path = "C:\inputimages\*.*"
for bb,file in enumerate (glob.glob(path)):
    for i in range(8):
        img = cv2.imread(file)
        #rotate
        if i==0:
            img = rotate(img, angle=45)
            cv2.imwrite(f'C:\outputimages\ augument {bb+1}{i}.png', img*255)
        #shear
        if i==1:
            tf = AffineTransform(shear=-0.5)
            img = warp(img, tf, order=1, preserve_range=True, mode='wrap')
            cv2.imwrite(f'C:\outputimages\ augument {bb + 1}{i}.png', img)
        #warp
        if i==2:
            transform = AffineTransform(translation=(-500, 0))
            img = warp(img, transform, mode="wrap")
            cv2.imwrite(f'C:\outputimages\ augument {bb + 1}{i}.png', img*255)
        #blur
        if i==3:
            img = ndimage.uniform_filter(img, size=3)
            cv2.imwrite(f'C:\outputimages\ augument {bb + 1}{i}.png', img*255)
        #color inversion
        if i==4:
            img = util.invert(img)
            cv2.imwrite(f'C:\outputimages\ augument {bb + 1}{i}.png', img*255)
        #greyscall
        if i==5:
            img = rgb2gray(img)
            cv2.imwrite(f'C:\outputimages\ augument {bb + 1}{i}.png', img*255)
        #noising
        if i==6:
            img = random_noise(img, mode='s&p', amount=0.15)
            cv2.imwrite(f'C:\outputimages\ augument {bb + 1}{i}.png', img*255)