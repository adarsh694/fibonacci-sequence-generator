#FIBONACCI SEQUENCE GENERATOR 
#The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
import matplotlib.pyplot as plt

def fib(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence 
y = fib(20)
x = list(range(1,20+1))

# Plotting the Fibonacci sequence
plt.plot(x, y)
plt.title('Fibonacci Sequence')
plt.xlabel("position")
plt.ylabel("value")

plt.show()
plt.pause(0)
plt.show(block=True)
plt.yscale('log')  # Set y-axis to logarithmic scale for better visualization of large values
plt.plot(x, y , marker='o')



