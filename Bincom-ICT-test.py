import random

# Simulate the web page data (for the purpose of this task)
web_page_data = """
GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN
"""

# Extract colors using simple string operations
colors = web_page_data.split(",")

# Calculate frequencies
color_counts = {}
for color in colors:
    if color in color_counts:
        color_counts[color] += 1
    else:
        color_counts[color] = 1

# Calculate mean color (most frequent color)
mean_color = max(color_counts, key=color_counts.get)

# Calculate the most worn color (most frequent color)
most_worn_color = max(color_counts, key=color_counts.get)

# Calculate the median color
sorted_colors = sorted(color_counts.items(), key=lambda item: item[1])
median_index = len(sorted_colors) // 2
if len(sorted_colors) % 2 == 0:
    median_color = sorted_colors[median_index - 1][0]
else:
    median_color = sorted_colors[median_index][0]

# Calculate variance
color_frequencies = list(color_counts.values())
mean_frequency = sum(color_frequencies) / len(color_frequencies)
variance = sum((x - mean_frequency) ** 2 for x in color_frequencies) / len(color_frequencies)

# Probability of red
total_colors = sum(color_counts.values())
probability_red = color_counts.get('Red', 0) / total_colors

# Recursive search algorithm
def recursive_search(lst, x, low, high):
    if high >= low:
        mid = (high + low) // 2
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            return recursive_search(lst, x, low, mid - 1)
        else:
            return recursive_search(lst, x, mid + 1, high)
    else:
        return -1

# Generate random 4-digit binary number and convert to base 10
random_binary = ''.join([str(random.randint(0, 1)) for _ in range(4)])
base_10 = int(random_binary, 2)

# Sum of first 50 Fibonacci sequence
def fibonacci_sum(n):
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total

sum_fibonacci = fibonacci_sum(50)

# Output results
print("Mean color:", mean_color)
print("Most worn color:", most_worn_color)
print("Median color:", median_color)
print("Variance of colors:", variance)
print("Probability of red:", probability_red)
print("Random binary number:", random_binary)
print("Base 10 conversion:", base_10)
print("Sum of first 50 Fibonacci sequence:", sum_fibonacci)
