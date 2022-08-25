import os
import random
import numpy

label_path = '/home/rhq/xiangmu/YOLOP/data/train/json'
image_path = '/home/rhq/xiangmu/YOLOP/data/train/images'

image_lists = os.listdir(image_path)
label_lists = os.listdir(label_path)

suffixs = ['jpg', 'json']
images = []
labels = []
for image in image_lists:
    filename, suffix = image.rsplit('.', 1)
    if suffix in suffixs:
        images.append(filename)
    continue
for label in label_lists:
    filename, suffix = label.rsplit('.', 1)
    if suffix in suffixs:
        labels.append(filename)
    continue
print('image:', len(images))
print(f"label {len(labels)}")

'''images2 = numpy.random.choice(images, size=67266, replace=False)
for image in images2:
    image_name = image + '.jpg'
    file_path = os.path.join('/home/rhq/xiangmu/coco/images/train2017', image_name)
    os.system(f"rm {file_path}")'''

for label in labels:
    if label not in images:
        label_name = label+'.json'
        file_path = os.path.join('/home/rhq/xiangmu/YOLOP/data/train/json', label_name)
        os.remove(file_path)
        # os.system(f"rm {file_path}")

