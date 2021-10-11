import neuralnetwork as nn
import numpy as np
import time as t

start_time = t.time()

with np.load('mnist.npz') as data:
	training_images = data['training_images']
	training_labels = data['training_labels']

layer_sizes = (784, 20, 20, 10)

net = nn.NeuralNetwork(layer_sizes)
net.print_accuracy(training_images, training_labels)

elapsed_time = t.time() - start_time
print(f"{round(elapsed_time, 3)} s")

