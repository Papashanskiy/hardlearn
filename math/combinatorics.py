import itertools


items = [1, 2, 3]

print('Перестановки P n')
all_permutations = list(itertools.permutations(items, 3))
print(all_permutations)

print('Размещения A n k')
all_arrangements = list(itertools.permutations(items, 2))
print(all_arrangements)

print('Сочетания C n k')
all_combinations = list(itertools.combinations(items, 2))
print(all_combinations)
