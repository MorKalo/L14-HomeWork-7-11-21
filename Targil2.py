#create popByValue function which gets a dictionary and a value as a parameter- pop all items with the value.
# *etgar: returns these items in a list

def popByValue(d, v):
    for k in list(d.keys()):
        if d[k]==v:
            d.pop(k)



d={'a':2 , 'b':3, 'c':2}
print(d)
popByValue(d, 3)
print(d)

