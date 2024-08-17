bicycles = ['trekingowy', 'górski', 'miejski', 'szosowy', 'mtb']

# print(bicycles)

# print(bicycles[0])
# print(bicycles[0].title())
# print(bicycles[3])

# print(bicycles[-1])

bicycles[-1] = 'new MTB'
print(bicycles)

bicycles.append('składak')
print(bicycles)

bicycles.insert(1, 'elektryczny')
print(bicycles)

# del bicycles[-2]
# print(bicycles)

# deleted_bike = bicycles.pop()
# print(bicycles)
# print(deleted_bike)

# deleted_bike = bicycles.pop(2)
# print(bicycles)
# print(deleted_bike)

# bicycles.remove('miejski')
# print(bicycles)

# bicycles.sort()
# print(bicycles)
# bicycles.sort(reverse=True)
# print(bicycles)

print(sorted(bicycles))
print(bicycles)

bicycles.reverse()
print(bicycles)