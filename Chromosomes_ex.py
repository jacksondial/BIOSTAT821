import random

NUM_CHROMO = 23
num_samples = 30

chromosomes = random.choices(range(1, NUM_CHROMO + 1), k=num_samples)
print(chromosomes)

###

# query = 15
# for chromosome in chromosomes:  # N times
#     if chromosome == query:  # O(1)
#         print(f"Found {query}!")  # O(1)
#         break
# print(f"Did not find {query}")  # O(1)

# N * (1 + 1) + 1 = O(N)

# Write a function to deduplicate


# def dedup(chromosomes):
#     nondups = []
#     for chromosome in chromosomes:
#         for noted in nondups:
#             if chromosome == noted:
#                 break
#         nondups.append(chromosome)

# N * (N * (1 + 1)) -> O(N**2)

# Now use a dictionary to make this algorithm faster
