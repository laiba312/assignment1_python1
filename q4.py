# Substring Search

# Task: Given the string s, use string methods to:
# Find the index of "fox": get the starting index of the substring "fox". If "fox" is not found, it should return -1.
# Count occurrences of "the": Use the string's built-in method to count how many times the substring "the" appears in the string.
# s:str ="the quick brown fox jumps over the lazy dog"
# Expected Output:
# index of 'fox' is 16
# 'the' appears 2 times




# Given string
s:str ="the quick brown fox jumps over the lazy dog"

# Find the index of "fox"
index_fox = s.find("fox")

# Count occurrences of "the"
count_the = s.count("the")

# Printing the results
print(f"index of 'fox' is {index_fox}")
print(f"'the' appears {count_the} times")
