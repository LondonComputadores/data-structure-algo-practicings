from collections import defaultdict

dd = defaultdict(list)

dd['dogs'].append('Rufus')
dd['dogs'].append('Kathrin')
dd['dogs'].append('Mr Sniffles')

print(dd['dogs'])


# Output:
# ['Rufus', 'Kathrin', 'Mr Sniffles']