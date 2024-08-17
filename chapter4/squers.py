squers = []

for value in range(1, 11):
    squers.append(value**2)

print(squers)

min = min(squers)
max = max(squers)
sum = sum(squers)

print(f"Min: {min}, Max: {max}, Sum: {sum}")

comprehension_squers = \
    [value**2 for value in range(1, 11)]

print(comprehension_squers)