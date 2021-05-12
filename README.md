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

```
from skimage import transform
from skimage.transform import rotate, AffineTransform,warp
from skimage.util import random_noise
from skimage.filters import gaussian
from scipy import ndimage
```
![Screenshot (15)](https://user-images.githubusercontent.com/81819743/117994491-cb152d00-b36a-11eb-89f6-8b30e0b7dc2a.png)
1. Rotation

```
skimage.transform.rotate(image, angle, resize=False, center=None, order=None, mode='constant', cval=0, clip=True, preserve_range=False)
```
example

```
rotating = rotate(temp, angle=30)
```
![Screenshot (17)](https://user-images.githubusercontent.com/81819743/117995024-2fd08780-b36b-11eb-8b0e-975108aed276.png)



2. Bluring

```
scipy.ndimage.uniform_filter(input, size=3, output=None, mode='reflect', cval=0.0, origin=0)[source]
```
example
```
blured_image = ndimage.uniform_filter(img, size=3)
```
![Screenshot (24)](https://user-images.githubusercontent.com/81819743/117994761-f730ae00-b36a-11eb-8545-7f5e81adc6fa.png)



3. Colorinversion

```
skimage.util.invert(image, signed_float=False)
```

example

```
color_inversion = util.invert(img)
```
![Screenshot (25)](https://user-images.githubusercontent.com/81819743/117995451-876ef300-b36b-11eb-9115-333c104e85df.png)


4. Noising

```
skimage.util.random_noise(image, mode='gaussian', seed=None, clip=True, **kwargs)
```

example

```
noisy_image = random_noise(img, var=0.1**.01)
```

![Screenshot (27)](https://user-images.githubusercontent.com/81819743/117995543-9ce41d00-b36b-11eb-9a12-6ffc20f7f169.png)


5. Shearing

```
skimage.transform.warp(image, inverse_map, map_args={}, output_shape=None, order=None, mode='constant', cval=0.0, clip=True, preserve_range=False)
```
example

```
sheared = transform.warp(img, tf, order=1, preserve_range=True, mode='wrap')
```
![Screenshot (28)](https://user-images.githubusercontent.com/81819743/117995642-af5e5680-b36b-11eb-9553-b99e3f52312a.png)

6. Warping

```
skimage.transform.warp(image, inverse_map, map_args={}, output_shape=None, order=None, mode='constant', cval=0.0, clip=True, preserve_range=False)
```

example

```
transform = AffineTransform(translation=(-200,0)) 
```

![Screenshot (30)](https://user-images.githubusercontent.com/81819743/117995716-bedd9f80-b36b-11eb-8f6a-0a39a3de6962.png)

7. Greyscaling

```
skimage.color.rgb2gray(img)
```

example

```
gray_scale_image = rgb2gray(img)
```

![Screenshot (26)](https://user-images.githubusercontent.com/81819743/117995775-cbfa8e80-b36b-11eb-85bb-fb748eba0f28.png)



