# 📈 Fibonacci Sequence Generator

A Python project that generates the Fibonacci sequence and visualizes it as a graph using Matplotlib.

---

## 🔢 What is the Fibonacci Sequence?

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones:

**0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...**

Formally defined as:
```
F(n) = F(n-1) + F(n-2)
where F(0) = 0 and F(1) = 1
```

---

## 📊 Features

- Generates any number of Fibonacci terms
- Visualizes the sequence as a line graph
- Displays grid lines for better readability
- Labeled axes and title for clarity
- Supports log scale for large sequences (e.g. 100 terms)

---

## 🛠️ Requirements

- Python 3.x
- matplotlib

Install the required library using:
```
pip install matplotlib
```

---

## 🚀 How to Run

1. Clone this repository:
```
git clone https://github.com/your-username/fibonacci-generator.git
```

2. Navigate into the project folder:
```
cd fibonacci-generator
```

3. Run the script:
```
python fibonacci.py
```

A graph window will pop up showing the Fibonacci sequence. Close the window to exit.

---

## 📁 Project Structure

```
fibonacci-generator/
│
├── fibonacci.py      # Main script
└── README.md         # Project documentation
```

---

## 📷 Sample Output

The graph plots the **position** of each Fibonacci number on the X-axis and its **value** on the Y-axis. For large sequences (50-100 terms), a log scale is applied to keep the graph readable since Fibonacci numbers grow exponentially.

---

## 🧠 How It Works

The core function generates the sequence:

```python
def fib(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
```

The X and Y data is then prepared and plotted:

```python
y = fib(100)
x = list(range(1, 100 + 1))

plt.plot(x, y, marker='o', color='green', linewidth=2)
plt.title("Fibonacci Sequence")
plt.xlabel("Position")
plt.ylabel("Value")
plt.grid(True)
plt.yscale('log')
plt.show(block=True)
```

---

## 👩‍💻 Author

Made by **adarsh** as part of a Math Project exploring the Fibonacci sequence and data visualization with Python.

---

## 📜 License

This project is open source and free to use.
