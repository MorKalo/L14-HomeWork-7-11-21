#create newDict function which gets two lis1 and list2 as parameter- returns a dictionary which consist
# of the two lists:
# list1 will be the keys and list2 will be the values. if the lists are not in the same length or list1 contains
# duplication returns None

def newDict(lst1_keys, lst2_values):
    if len(lst1_keys) != len(lst2_values):
        return None
    if len(lst1_keys) != len(set(lst2_values)):
        return None
    d={}
    for i in range (len(lst1_keys)):
        d[lst1_keys[i]]=lst2_values[i]
    return d

print(newDict(['aa', 'b', 'c'], [4,5,6]))


