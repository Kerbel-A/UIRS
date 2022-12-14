#https://www.codewars.com//kata/51fc12de24a9d8cb0e000001
def valid_ISBN10(isbn): 
    valid_chars = '0123456789X'    
    if len(isbn) != 10: return False
    if 'X' in isbn[:9]: return False
    total = 0
    for index, char in enumerate(isbn):
        if char not in valid_chars:
            return False
        total += valid_chars.find(char) * (index+1)
    return total % 11 == 0
