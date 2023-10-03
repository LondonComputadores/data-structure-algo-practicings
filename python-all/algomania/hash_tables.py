"""
    Hash Tables calculates the ASCII code number for each word's letter then adding
    them up then return the module (%) of the sum of the ASCII codes in each word by
    the length of the array/list + 1, for example:

    items_list = ['job', 'ans', 'cob', 'dub', 'big'] # The length is 5 + 1 == 6
    
    Then: 

    job = j=106 | o=111 | b=098 -> index[11]
    mia = m=109 | i=105 | a=097 -> index[07]

    let's use job's values 106 + 111 + 98 = 315 % 6 = 3

    So the 'job' should be place at the 3º index in a new list/array

    For the ASCII codes calculations for each word is use a ASCII function as below:
"""

# Function to calculate the hashes and return the index where it should be placed at

items = ['job', 'ans', 'cob', 'dub', 'big']

def calc_hash(item, item_count):
    hash = 0
    for c in item:
        hash += ord(c) # Time complexity O(1)
    return hash % item_count

print(calc_hash(items[0], 6))

# Output: 3