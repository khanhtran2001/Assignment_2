Assignment_2: 04/05/2021
# ASSIGNMENT 2: IMAGE AUGMENTATION
# Nhiệm vụ
1. Tìm hiểu về image augmentation
2. Các hàm để augment trong python (opencv, keras, pytorch, augmentor, albumentations, ...) chạy thử và show lại kết quả vào Readme
3. Code 1 chương trình augment 1 tập data tùy chọn
# Nộp
Thời gian: 23h59 thứ 4 ngày 12/05/2021
1. Code
2. Folder data ban đầu và sau khi augment
3. Readme về các hàm augment

# Augmentation using skimage
Tran Huy Khanh
0. Library for augmenting
'''
from skimage import transform
from skimage.transform import rotate, AffineTransform,warp
from skimage.util import random_noise
from skimage.filters import gaussian
from scipy import ndimage
'''
1. Rotation
'''
rotating = rotate(temp, angle=30)
'''
2. Bluring
'''
blured_image = ndimage.uniform_filter(img, size=3)
'''
3. Colorinversion
'''
color_inversion = util.invert(img)
'''
4. Noising
'''
noisy_image = random_noise(img, var=0.1**.01)
noise_fig = plot_side(img,noisy_image , 'Original', 'Noise_image')
'''
5. Shearing
'''
sheared = transform.warp(img, tf, order=1, preserve_range=True, mode='wrap')
'''
6. Warping
'''
transform = AffineTransform(translation=(-200,0)) 
'''
7. Greyscaling
'''
gray_scale_image = rgb2gray(img)
'''