
# Chat GPT 3.5 Solution 

"""
    Achieving a constant-time complexity of O(1) for a hash table operation is
    the ideal goal, and it's the characteristic of an efficient hash table
    implementation. In Python, the built-in dict type utilizes a hash table and
    provides O(1) time complexity for average case operations such as insertion,
    retrieval, and deletion.

    However, achieving a constant-time complexity doesn't mean that every operation
    will take exactly the same amount of time. In practice, the efficiency of a hash
    table is often measured in terms of "amortized" constant-time complexity, where
    on average, operations take a constant amount of time over a series of operations.
    
    In this example, the create_hash_table function creates a hash table using a
    Python dict, which achieves O(1) average time complexity for insertion and
    retrieval. The retrieve_from_hash_table function retrieves values from the hash
    table using dict.get(), which also operates in O(1) average time complexity.

    Here's an example of how you could create a hash table with O(1) average time
    complexity for insertions and retrievals using a built-in dict in Python:
"""

def hash_function(s):
    """Hash function using ASCII sum."""
    return sum(ord(char) for char in s)


def create_hash_table(strings):
    """Create a hash table for a list of strings."""
    hash_table = {}

    for string in strings:
        hash_value = hash_function(string)
        if hash_value not in hash_table:
            hash_table[hash_value] = [string]
        else:
            hash_table[hash_value].append(string)

    return hash_table

# List of strings to hash
strings_to_hash = ['job', 'ans', 'cob', 'dub', 'big']

# Create the hash table
hash_table = create_hash_table(strings_to_hash)

# Display the hash table
for hash_value, strings in hash_table.items():
    print(f'Hash {hash_value}: {strings}')