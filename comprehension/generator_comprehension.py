'''
The only difference is that they don’t
allocate memory for the whole list but generate one item at a time, thus more memory
efficient
'''
multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)
print(next(multiples_gen))
print(next(multiples_gen))