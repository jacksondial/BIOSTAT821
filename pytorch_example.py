"""Pytorch."""
import numpy as np
import re
import torch

x = torch.tensor(4.0)
w = torch.tensor(5.0, requires_grad=True)
b = torch.tensor(6.0, requires_grad=True)

y = x * w + b
print(w.grad, b.grad)
y.backward()
print(w.grad, b.grad)
print(y)


def linear(x: np.ndarray, w: np.ndarray, b: np.ndarray) -> np.ndarray:
    return x @ w.T + b


N = 100
D = 1
x = np.random.rand(N, D)
w = np.random.rand(D, 1)
b = np.random.rand(1, 1)

print(linear(x, w, b))
