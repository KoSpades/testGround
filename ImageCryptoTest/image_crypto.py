import io
from cryptography.fernet import Fernet
import PIL.Image as Image
import numpy as np

from keras.preprocessing.image import ImageDataGenerator

# generate symmetric key
sym_key = Fernet.generate_key()
sym_key = Fernet(sym_key)

# Create the encrypted bytes
with open("ImageCryptoTest/0a0f91dc-6015-4342-b809-d19610854a21.png", "rb") as f:
    data = f.read()
    enc_data = sym_key.encrypt(data)

# Create the decrypted bytes
dec_data = sym_key.decrypt(enc_data)

# Convert bytes back to an image
image_one = Image.open(io.BytesIO(dec_data))
image_two = Image.open(io.BytesIO(dec_data))
image_three = Image.open(io.BytesIO(dec_data))

print(image_one.format)  # format of the image
print(image_one.size)  # size of the image
print(image_one.mode)  # "L": means greyscale

train_data = [np.array(image_one), np.array(image_two), np.array(image_three)]
train_label = [0, 1, 1]

train_data = np.array(train_data).reshape(3, 1024, 1024, 1)

# print(train_data.shape)

train_datagen = ImageDataGenerator(rescale=1./255.,
                                   rotation_range=40,
                                   width_shift_range=0.2,
                                   height_shift_range=0.2,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True,
                                   vertical_flip=True,
                                   validation_split=0.1,)

train_generator = train_datagen.flow(train_data,
                                     train_label,
                                     batch_size=64,)


