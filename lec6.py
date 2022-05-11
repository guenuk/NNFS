import math
layer_outputs = [4.8, 1.21, 2.385]
#determine how wrong is the model
layer_outputs = [4.8, 4.79, 4.25]

# E = 2.71828182846
E = math.e
exp_values = []

for output in layer_outputs:
    exp_values.append(E**output)
print(exp_values)