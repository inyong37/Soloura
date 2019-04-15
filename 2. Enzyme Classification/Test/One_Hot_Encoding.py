from keras.utils import to_categorical
y = to_categorical(y, num_classes=7) # keras count from 0 ~

from keras.utils import np_utils
y = np_utils.to_categorical(y, 7)