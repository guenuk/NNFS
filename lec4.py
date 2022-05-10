#LEC4

#batch size : 32 is common
#dot product 를 matrix 대 matrix 로 하게될경우 -- matrix의 [0][0] * matrix2[0][0] + matrix[0][1] * matrix2[1][0] .... , shape error 가 많이남
#matrix의 row 와 column 을 바꿔주는것 -> transpose

import numpy as np
# inputs = [[1,2,3,2.5],
#           [2.0,5.0,-1.0,2.0],
#           [-1.5,2.7,3.3,-0.8]]

# weights = [[0.2,0.8,-0.5, 1.0],
#            [0.5,-0.91,0.26,-0.5],
#            [-0.26,-0.27,0.17,0.87]]
#
# biases = [2,3,0.5]
#
# weights2 = [[0.1,-0.14,0.5],
#             [-0.5,0.12,-0.33],
#             [-0.44,0.73,-0.13]]
#
# biases2 = [-1,2,-0.5]
#
# layer1_output = np.dot(inputs, np.array(weights).T) + biases
#
# layer2_output = np.dot(layer1_output, np.array(weights2).T) + biases2
#
# print(layer2_output)

X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]
np.random.seed(0)


## bias 가 0으로 시작 될 경우, dead network 가 될 수 있음

class Layer_Dense:

    def __init__(self,n_inputs, n_neurons):
        self.weights = 0.10*np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1,n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) +self.biases

layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,2)

print(layer1.weights)
print(layer1.biases)


layer1.forward(X)
print(layer1.output)



