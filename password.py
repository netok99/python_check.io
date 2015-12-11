def checkio(data):
    upper = False
    lower = False
    count = 0
    digit = False
    for x in data:
        count += 1
        if x.isupper():
            upper = True
        elif x.islower():
            lower = True
        if x.isdigit():
            digit = True
    if count > 9 and upper and lower and digit:
        return True
    else:
        return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"