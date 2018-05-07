import numpy as np

class SimpleNN():

    def Sigmoid(self, x):
        return 1.0 / (1.0 + np.exp(-x))

    def calcOutput(self, W, x):
        y = np.matmul(W, x)
        y = self.Sigmoid(y)
        return y

    def calcError(self, d, y):
        e = d - y
        delta = y * (1-y) * e
        return delta

    def DeltaSGD(self, W, X, D, alpha):
        for k in range(4):
            x = X[k, :].T
            d = D[k]

            y = self.calcOutput(W, x)
            delta = self.calcError(d, y)

            dW  = alpha * delta * x
            W = W + dW
        return W

# test
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

D = np.array([[0],
              [0],
              [1],
              [1]])

simple_nn = SimpleNN()

W = 2 * np.random.random((1, 3)) - 1
alpha = 0.9
N = 4

for epoch in range(10000):
    W = simple_nn.DeltaSGD(W, X, D, alpha)

for k in range(N):
    x = X[k, :].T
    v = np.matmul(W, x)
    y = simple_nn.Sigmoid(v)
    print(y)
