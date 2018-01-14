# skLearnHandwrittenDigitRecognition

This program will read previous data stored in a file "data.csv" to train two sklearn classifiers and will decide on the value that both of them decide on, otherwise the prediction with a lower value, and will output the prediction.

The training happens everytime the program is run, using the previous data, therefore it is not expected for the program to start working through it's first run or to improve over time using the same build of the program since it is designed to save the data each time it is being closed, using the titlebar close button or simply pushing the escape button on the keyboard, the program will be closed and the data will be stored for future usage of training.

Since the screen created by pygame is 280x280pix, it is shorten to 28x28 as the conventional MNIST database and is flatten. Although it is clear that this approach will ignore the placement of the pixels with respect to each other, which can be fixed using convolutional readings, for this program it is only intended to implement simple ideas for the sake of using them as steps forward. 
