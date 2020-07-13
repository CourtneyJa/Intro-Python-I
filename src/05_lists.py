# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]

print("append works: " , x.append(4))

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print("extend works: ", x.extend(y))

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print("remove 8", x.remove(8))

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5,99)
print("insert works", x)

# Print the length of list x
# YOUR CODE HERE
print("length works", len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
print("sum works", sum(x*1000))