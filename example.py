

def returns_true(): 
    return True

def returns_false(): 
    return False

def returns_opposite(bool): 
    return not bool


def main():
    result = returns_true()
    print str(result)
    with open('out.txt', 'w') as f: f.write(str(result))



