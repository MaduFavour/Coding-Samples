# Coding-Samples
These samples include:
**Synethesia TurtleBot**

This Python code analyzes audio data using Fast Fourier Transform (FFT) to determine the frequency of the sound being played within a given time frame. Based on the frequency range, the code creates a circle, triangle, or square using the Matplotlib library, which is displayed on the screen. The program repeatedly records and analyzes audio data until the user inputs 'q' to quit the program. This code is useful for applications that involve sound processing and analysis, such as speech recognition or music analysis.

The Synesthesia TurtleBot is a project that uses sound frequencies to create shapes using a TurtleBot robot. The project was developed as part of an undergraduate research project and demonstrates proficiency in both robotics assembly and coding.

Requirements
To run this project, you will need:

Python 3.x
PyAudio library
NumPy library
Matplotlib library
Installation
To install the necessary libraries, you can use pip:


pip install pyaudio numpy matplotlib
Usage
To run the project, simply run the synesthesia_turtlebot.py file:


python synesthesia_turtlebot.py
The program will record audio input for a specified time frame and use the frequency of the input to create shapes on the TurtleBot. The shapes are displayed on a graph using Matplotlib.




** Crowd Modelling Train Neural Network**

This code trains a spatio-temporal graph convolutional neural network (ST-GCNN) on pedestrian trajectory prediction. The network is trained to predict the future trajectories of pedestrians based on their previous movements, observed trajectories, and social interactions with other pedestrians in a given scene. The code defines the model architecture, loads the dataset, sets the training parameters, and trains the model for a specified number of epochs while recording the training and validation loss. The model is saved at the end of the training process

Dependencies
Python 3.9
PyTorch 1.7.1
NetworkX 2.5.1
NumPy 1.19.5
Matplotlib 3.2.2
Pickle 4.0
argparse
Usage
To train the model, run the main.py file with the following command:

python main.py

Several parameters can be set in the argparse section of the code, such as the number of ST-GCNN layers, the number of TXPCNN layers, the learning rate, the batch size, and the number of epochs.

The model will be saved to a checkpoint directory, and the metrics of the training and validation losses will be saved to a metrics.pkl file.

Citation
If you use this code for your research, please consider citing the following paper:

@article{mohamed2020social,
  title={Social-STGCNN: A Social Spatio-Temporal Graph Convolutional Neural Network for Human Trajectory Prediction},
  author={Mohamed, Ahmed and Qian, Kun and Wu, Jian and Zhang, Chunyuan and Chen, Xiao and Shen, Jianbing},
  journal={arXiv preprint arXiv:2012.02386},
  year={2020}
}










