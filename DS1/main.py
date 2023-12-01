import numpy as np

rng = np.random.default_rng()

a1 = np.linspace(1, 10, num=10)
print(a1)

a2 = np.zeros((3, 3), dtype=int)
print(a2)

a3 = rng.integers(1,10, size=(5, 5)) 
print(a3)

a4 = np.random.random((4, 4))
print(a4)

a5_1 = rng.integers(1,10, size=(5))
a5_2 = rng.integers(1,10, size=(5))
print(a5_1, a5_2)
print(' + ',a5_1 + a5_2)
print(' - ',a5_1 - a5_2)
print(' * ',a5_1 * a5_2)

a6 = rng.integers(1,10, size=(7)) + rng.integers(1,10, size=(7))
print(a6)

a7_1 = rng.integers(1,10, size=(2, 2))
a7_2 = rng.integers(1,10, size=(2, 3))
print(a7_1.dot(a7_2))

a8 = rng.integers(1,10, size=(3, 3))
a8 = np.linalg.inv(a8)
print(a8)

a9 = a4.T
print(a9)

a10_1 = rng.integers(1,10, size=(3, 4))
a10_2 = rng.integers(1,10, size=(4))
print(a10_1 * a10_2)

a11_1 = np.random.random((2, 3))
a11_2 = np.random.random(3)
print(a11_1 * a11_2)

a12_1 = rng.integers(1,10, size=(2, 2))
a12_2 = rng.integers(1,10, size=(2, 2))
print(a12_1 * a12_2)

a13_1 = rng.integers(1,10, size=(2, 2))
a13_2 = rng.integers(1,10, size=(2, 2))
print(a13_1 + a13_2)

a14 = rng.integers(1,100, size=(5, 5))
print(a14.sum())

a15_1 = rng.integers(1,10, size=(4, 4))
a15_2 = rng.integers(1,10, size=(4, 4))
print(a15_1 - a15_2)

a16 = np.random.random((3, 3))
print(a16)
a16_1= np.array([[a16[0].sum()],[a16[1].sum()],[a16[2].sum()]])
print(a16_1)

a17_1 = rng.integers(1,10, size=(3, 4))
a17_2 = np.zeros((3, 4), dtype=int)
print(a17_1)
for i in range(0, a17_1.shape[0]):
    for x in range(0, a17_1.shape[1]):
        a17_2[i, x] = a17_1[i, x] * a17_1[i, x]
print(a17_2)

a18 = rng.integers(1,50, size=(4))
print(a18)
a18_2 = np.sqrt(a18)
print(a18_2)