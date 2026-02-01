import random
import os

if __name__ == '__main__':
    length = 1000000
    with open(os.path.join(os.path.dirname(__file__), "testcases/test1.txt"), "w") as f:
        A = [0.0]*length
        for i in range(length):
            A[i] = random.uniform(1, 1000000000)
        A.sort()
        for i in range(length):
            f.write(str(A[i]))
            if i != length: f.write(" ")
            else: f.write("\n")
    with open(os.path.join(os.path.dirname(__file__), "testcases/test2.txt"), "w") as f:
        A = [0]*length
        for i in range(length):
            A[i] = random.randint(1, 1000000000)
        A.sort(reverse=True)
        for i in range(length):
            f.write(str(A[i]))
            if i != length: f.write(" ")
            else: f.write("\n")
    for num in range(3, 7):
        with open(os.path.join(os.path.dirname(__file__), "testcases/test" + str(num) + ".txt"), "w") as f:
            for i in range(length):
                f.write(str(random.uniform(1, 1000000000)))
                if i != length: f.write(" ")
                else: f.write("\n")
    for num in range(7, 11):
        with open(os.path.join(os.path.dirname(__file__), "testcases/test" + str(num) + ".txt"), "w") as f:
            for i in range(length):
                f.write(str(random.randint(1, 1000000000)))
                if i != length-1: f.write(" ")
                else: f.write("\n")
