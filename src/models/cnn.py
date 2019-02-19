#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.models import Sequential


class Model1:
    """A first CNN model.

    The model is a convolutional model, adapted to the problem. The inputs
    have originally two dimensions, the timestack size. The size of the output
    is the number of points in the discretization of the domain.

    The model is composed of three convolutional layers, followed by a fully-
    connected layer (a hidden flatten layer is required to link both).

    Examples:
        This example can be run by executing the file `cnn.py`.

        >>> cnn = Model1((50, 100, 1), 200)
        >>> print(cnn.model().summary())

    """

    def __init__(self, input_shape, output_size):
        """Creation of a first CNN model.

        The model is a convolutional model, adapted to the problem. The inputs
        have originally two dimensions, the timestack size. The size of the
        output is the number of points in the discretization of the domain.

        Note:
            The model can be used as a template. The headers and the
            specifications need to be fulfilled.

        Args:
            input_shape (tuple): Input shape of the model, typically (_, _, 1).
            output_size (int): Output size of the model (discretization of the
                domain).
        """
        self.__cnn = Sequential(name="CNN")

        self.__set_model(input_shape, output_size)

    def __set_model(self, input_shape, output_size):
        """Creation of all the layers of the network.

        The model is composed of three convolutional layers, followed by a
        fully-connected layer (a hidden flatten layer is required to link both).

        Args:
            input_shape (tuple): Input shape of the model, typically (_, _, 1).
            output_size (int): Output size of the model (discretization of the
                domain).

        """
        self.__cnn.add(Conv2D(64, (2, 2), activation='relu', padding='same',
                              input_shape=input_shape))
        self.__cnn.add(MaxPooling2D((2, 2)))

        self.__cnn.add(Conv2D(128, (2, 2), activation='relu', padding='same'))
        self.__cnn.add(MaxPooling2D((2, 2)))

        # self.__cnn.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
        # self.__cnn.add(MaxPooling2D((2, 2)))

        self.__cnn.add(Flatten())
        self.__cnn.add(Dense(units=output_size))

    def model(self):
        """Model in the keras format.

        After calling this method, all the keras functions that can be applied
        on a model (compile, fit, ...) can be called on the output of this
        method.

        Returns:
            The model in the keras format.

        """
        return self.__cnn


if __name__ == "__main__":
    # this model is the classic model (output of the first auto-encoder model)
    cnn = Model1((50, 200, 1), 200)
    print(cnn.model().summary())