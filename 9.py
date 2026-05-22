numbers = range(1, 11)
squares = [n**2 for n in range(2, 11, 2)]
odds = list(range(1, 11, 2))

def generate_data(n):
    return [i * 2 for i in range(n) if i > 0]

data = generate_data(100)
filtered = [x for x in data if x % 10 == 0]