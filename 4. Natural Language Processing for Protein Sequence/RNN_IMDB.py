# -*- coding: UTF-8 -*-
# Recurrent Neural Network
# Inyong Hwang
# Dataset: IMDB Dataset
# Model:
# 1. Simple RNN
# 2. Bidirectional Simple RNN
# 3. Long Short Term Memory
# 4. Bidirectional Long Short Term Memory
# 5. Gated Recurrent Unit
# 6. Bidirectional Gated Recurrent Unit

from keras.preprocessing import sequence
from keras.datasets import imdb
from keras import layers, models

# Dataset: IMDB Dataset
class Dataset_imdb:
    def __init__(self, max_feature=20000, maxlen=80):
        (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_feature)
        x_train = sequence.pad_sequences(x_train, maxlen=maxlen)
        x_test = sequence.pad_sequences(x_test, maxlen=maxlen)
        self.x_train, self.y_train = x_train, y_train
        self.x_test, self.y_test = x_test, y_test

# 1. Simple RNN
class RNN_Simple(models.Model):
    def __init__(self, max_feature, maxlen):
        l_input = layers.Input((maxlen,))
        l_embed = layers.Embedding(max_feature, 128)(l_input)
        l_rnn = layers.SimpleRNN(128, dropout=0.2, recurrent_dropout=0.2)(l_embed)
        l_output = layers.Dense(1, activation='sigmoid')(l_rnn)
        super().__init__(l_input, l_output)
        self.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 2. Bidirectional Simple RNN
class RNN_BiSimple(models.Model):
    def __init__(self, max_feature, maxlen):
        l_input = layers.Input((maxlen,))
        l_embed = layers.Embedding(max_feature, 128)(l_input)
        l_birnn = layers.Bidirectional(layers.SimpleRNN(128, dropout=0.2, recurrent_dropout=0.2))(l_embed)
        l_output = layers.Dense(1, activation='sigmoid')(l_birnn)
        super().__init__(l_input, l_output)
        self.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 3. Long Short Term Memory
class RNN_LSTM(models.Model):
    def __init__(self, max_feature, maxlen):
        l_input = layers.Input((maxlen,))
        l_embed = layers.Embedding(max_feature, 128)(l_input)
        l_lstm = layers.LSTM(128, dropout=0.2, recurrent_dropout=0.2)(l_embed)
        l_output = layers.Dense(1, activation='sigmoid')(l_lstm)
        super().__init__(l_input, l_output)
        self.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 4. Bidirectional Long Short Term Memory
class RNN_BiLSTM(models.Model):
    def __init__(self, max_feature, maxlen):
        l_input = layers.Input((maxlen,))
        l_embed = layers.Embedding(max_feature, 128)(l_input)
        l_bilstm = layers.Bidirectional(layers.LSTM(128, dropout=0.2, recurrent_dropout=0.2))(l_embed)
        l_output = layers.Dense(1, activation='sigmoid')(l_bilstm)
        super().__init__(l_input, l_output)
        self.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 5. Gated Recurrent Unit
class RNN_GRU(models.Model):
    def __init__(self, max_feature, maxlen):
        l_input = layers.Input((maxlen,))
        l_embed = layers.Embedding(max_feature, 128)(l_input)
        l_gru = layers.GRU(128, dropout=0.2, recurrent_dropout=0.2)(l_embed)
        l_output = layers.Dense(1, activation='sigmoid')(l_gru)
        super().__init__(l_input, l_output)
        self.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# 6. Bidirectional Gated Recurrent Unit
class RNN_BiGRU(models.Model):
    def __init__(self, max_feature, maxlen):
        l_input = layers.Input((maxlen,))
        l_embed = layers.Embedding(max_feature, 128)(l_input)
        l_bigru = layers.Bidirectional(layers.GRU(128, dropout=0.2, recurrent_dropout=0.2))(l_embed)
        l_output = layers.Dense(1, activation='sigmoid')(l_bigru)
        super().__init__(l_input, l_output)
        self.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

class Machine:
    def __init__(self, max_feature=20000, maxlen=80):
        #self.model = RNN_Simple(max_feature, maxlen)
        #self.model = RNN_BiSimple(max_feature, maxlen)
        #self.model = RNN_LSTM(max_feature, maxlen)
        #self.model = RNN_BiLSTM(max_feature, maxlen)
        #self.model = RNN_GRU(max_feature, maxlen)
        self.model = RNN_BiGRU(max_feature, maxlen)
        self.data = Dataset_imdb(max_feature, maxlen)

    def run(self, epochs=3, batch_size=32):
        data = self.data
        model = self.model
        print("Training stage")
        print("==============")
        model.fit(data.x_train, data.y_train, batch_size=batch_size, epochs=epochs, validation_data=(data.x_test, data.y_test))
        score, acc = model.evaluate(data.x_test, data.y_test, batch_size=batch_size)
        print("Test performance: accuracy={0}, loss={1}".format(acc, score))

def main():
    m = Machine()
    m.run()

if __name__ == '__main__':
    main()