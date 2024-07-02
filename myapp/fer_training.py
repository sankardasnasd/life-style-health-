import os
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, AveragePooling2D, Dense, Activation, Dropout, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import numpy as np
import cv2

# Variables
num_classes = 7
batch_size = 100
epochs = 100

# Data Import
def read_dataset(path):
    data_list = []
    label_list = []
    my_list = os.listdir(path)
    for i, pa in enumerate(my_list):
        for root, dirs, files in os.walk(os.path.join(path, pa)):
            for f in files:
                file_path = os.path.join(root, f)
                img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
                res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
                data_list.append(res)
                label_list.append(i)
    return np.asarray(data_list, dtype=np.float32), np.asarray(label_list)

def read_dataset1(file_path):
    data_list = []
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
    data_list.append(res)
    return np.asarray(data_list, dtype=np.float32)

# Load dataset
x_dataset, y_dataset = read_dataset(r"C:\Users\JITHU\Desktop\FERDATASET\train")
X_train, X_test, y_train, y_test = train_test_split(x_dataset, y_dataset, test_size=0.2, random_state=0)

y_train = tf.keras.utils.to_categorical(y_train, num_classes)
y_test = tf.keras.utils.to_categorical(y_test, num_classes)

x_train = np.array(X_train, 'float32') / 255
x_test = np.array(X_test, 'float32') / 255
x_train = x_train.reshape(x_train.shape[0], 48, 48, 1)
x_test = x_test.reshape(x_test.shape[0], 48, 48, 1)

print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# Construct CNN structure
model = Sequential()
model.add(Conv2D(64, (5, 5), activation='relu', input_shape=(48, 48, 1)))
model.add(MaxPooling2D(pool_size=(5, 5), strides=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))
model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

# Compile model
model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(), metrics=['accuracy'])

# Train model
gen = ImageDataGenerator()
train_generator = gen.flow(x_train, y_train, batch_size=batch_size)

if not os.path.exists("model1.h5"):
    model.fit(train_generator, steps_per_epoch=len(x_train) // batch_size, epochs=epochs)
    model.save("model1.h5")
else:
    model = load_model("model1.h5")

# Evaluate model
yp = np.argmax(model.predict(x_test), axis=-1)
y_test_labels = np.argmax(y_test, axis=-1)
cf = confusion_matrix(y_test_labels, yp)
print(cf)

# Predict function
def predict(fn):
    dataset = read_dataset1(fn)
    dataset = dataset.reshape(dataset.shape[0], 48, 48, 1)
    mo = load_model("model1.h5")
    yhat_classes = np.argmax(mo.predict(dataset), axis=-1)
    return yhat_classes

# Example prediction (uncomment and provide a valid file path to test)
# print(predict(r"C:\path\to\your\image.jpg"))

#
#     print(yhat_classes)

#predict(r"D:\vehicle classification with deep learning\src\semi-semitrailer-truck-tractor-highway.jpg")