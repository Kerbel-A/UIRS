#https://www.codewars.com//kata/520446778469526ec0000001
def same_structure_as(original,other):
    if type(original)!=type(other):
        return False
    if type(original)==list and len(original)!=len(other):
        return False
    if type(original)==type(other)==int:
        return True
    for first, second in zip(original,other):
        if type(first)==list and type(second)!=list:
            return False
        if type(first)==list:
            if len(first)!=len(second):
                return False
            return same_structure_as(first, second)
    return True