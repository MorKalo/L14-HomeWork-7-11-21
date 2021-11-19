#create isDictKeysAlpha function which gets a dictionary as a parameter- returns true if all the keys are alpha
# (hint: use isaplhpa)

def isDictKeysAllAlpha(d:dict):
    for k in d.keys():
        if not str(k).isalpha():
            return False
    return True

