# Yash Thakur (B-75)

# Define fuzzy sets
A = {'x1': 0.2, 'x2': 0.7, 'x3': 0.5}
B = {'x1': 0.6, 'x2': 0.4, 'x3': 0.8}

# Union of two fuzzy sets
def fuzzy_union(A, B):
    return {key: max(A.get(key, 0), B.get(key, 0)) for key in set(A) | set(B)}

# Intersection of two fuzzy sets
def fuzzy_intersection(A, B):
    return {key: min(A.get(key, 0), B.get(key, 0)) for key in set(A) & set(B)}

# Complement of a fuzzy set
def fuzzy_complement(A):
    return {key: 1 - value for key, value in A.items()}

# Difference (A - B) of two fuzzy sets
def fuzzy_difference(A, B):
    return {key: min(A.get(key, 0), 1 - B.get(key, 0)) for key in set(A)}

# Display fuzzy sets nicely
def display_fuzzy_set(name, fuzzy_set):
    print(f"{name} = {{", end=' ')
    for key, value in fuzzy_set.items():
        print(f"({key}, {value:.2f})", end=' ')
    print("}")

# Perform operations
union = fuzzy_union(A, B)
intersection = fuzzy_intersection(A, B)
complement_A = fuzzy_complement(A)
difference = fuzzy_difference(A, B)

# Display results
display_fuzzy_set("A", A)
display_fuzzy_set("B", B)
display_fuzzy_set("Union (A U B)", union)
display_fuzzy_set("Intersection (A ∩ B)", intersection)
display_fuzzy_set("Complement of A", complement_A)
display_fuzzy_set("Difference (A - B)", difference)
