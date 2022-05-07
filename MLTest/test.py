import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import PIL.Image
import os
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator, img_to_array
from keras.preprocessing import image
from tqdm import tqdm

import warnings
warnings.filterwarnings("ignore")

train_df = pd.read_csv('/Users/kos/Desktop/test data/ChestRay/Chest_xray_Corona_Metadata.csv')
train_df.dropna(how='all')
train_df.fillna('unknown', inplace=True)
train_data = train_df[train_df['Dataset_type'] == 'TRAIN']
test_data = train_df[train_df['Dataset_type'] == 'TEST']
assert train_data.shape[0] + test_data.shape[0] == train_df.shape[0]
print(f"Shape of train data : {train_data.shape}")
print(f"Shape of test data : {test_data.shape}")

test_img_dir = '/Users/kos/Desktop/test data/ChestRay/Coronahack-Chest-XRay-Dataset' \
               '/Coronahack-Chest-XRay-Dataset/test'
train_img_dir = '/Users/kos/Desktop/test data/ChestRay/Coronahack-Chest-XRay-Dataset' \
                '/Coronahack-Chest-XRay-Dataset/train'

sample_train_images = list(os.walk(train_img_dir))[0][2][:8]
sample_train_images = list(map(lambda x: os.path.join(train_img_dir, x), sample_train_images))

sample_test_images = list(os.walk(test_img_dir))[0][2][:8]
sample_test_images = list(map(lambda x: os.path.join(test_img_dir, x), sample_test_images))

# remove Pnuemonia with unknown value
final_train_data = train_data[(train_data['Label'] == 'Normal') |
                              ((train_data['Label'] == 'Pnemonia') &
                               (train_data['Label_2_Virus_category'] == 'COVID-19'))]

# add a target and class feature
final_train_data['class'] = final_train_data.Label.apply(lambda x: 'negative' if x == 'Normal' else 'positive')
test_data['class'] = test_data.Label.apply(lambda x: 'negative' if x == 'Normal' else 'positive')

final_train_data['target'] = final_train_data.Label.apply(lambda x: 0 if x=='Normal' else 1)
test_data['target'] = test_data.Label.apply(lambda x: 0 if x == 'Normal' else 1)
# get the important features
final_train_data = final_train_data[['X_ray_image_name', 'class', 'target', 'Label_2_Virus_category']]
final_test_data = test_data[['X_ray_image_name', 'class', 'target']]

datagen = ImageDataGenerator(
  shear_range=0.2,
  zoom_range=0.2,
)

def read_img(filename, size, path):
    img = image.load_img(os.path.join(path, filename), target_size=size)
    img = img_to_array(img) / 255
    return img


corona_df = final_train_data[final_train_data['Label_2_Virus_category'] == 'COVID-19']
with_corona_augmented = []

# create a function for augmentation
def augment(name):
    img = read_img(name, (255,255), train_img_dir)
    i = 0
    for batch in tqdm(datagen.flow(tf.expand_dims(img, 0), batch_size=32)):
        with_corona_augmented.append(tf.squeeze(batch).numpy())
        if i == 20:
            break
        i = i + 1


# apply the function
print(corona_df['X_ray_image_name'].apply(augment))

train_arrays = []
final_train_data['X_ray_image_name'].apply(lambda x: train_arrays.append(read_img(x, (255, 255), train_img_dir)))
test_arrays = []
final_test_data['X_ray_image_name'].apply(lambda x: test_arrays.append(read_img(x, (255, 255), test_img_dir)))

# concatenate the training data labels and the labels for augmented images
y_train = np.concatenate((np.int64(final_train_data['target'].values),
                          np.ones(len(with_corona_augmented), dtype=np.int64)))

# From this point we temporarily move to notebook (right before Converting Data to tensors)
