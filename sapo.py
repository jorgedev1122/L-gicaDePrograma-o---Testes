# N = 1 -> [1] = 1
# N = 2 -> [1, 1], [2] = 2  
# N = 3 -> [1, 1, 1], [1, 2], [2, 1] = 3
# N = 4 -> [1, 1, 1, 1], [2, 1, 1], [1, 2, 1], [1, 1, 2], [2, 2] = 5
# N = 5 -> [1, 1, 1, 1, 1], [2, 1, 1, 1], [1, 2, 1, 1], [1, 1, 2, 1], [1, 1, 1, 2], [2, 2, 1], [2, 1, 2], [1, 2, 2] = 8

def fibonacci(num_pedras):
    if num_pedras <= 1:
        return 1
    return fibonacci(num_pedras - 1) + fibonacci(num_pedras - 2)

print(fibonacci(5))