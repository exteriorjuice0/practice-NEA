def isValidLength(value,minLength,maxLength):
    if len(value) < minLength:
        return False
    
    if len(value) > maxLength:
        return False
    
    return True