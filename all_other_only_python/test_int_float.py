
def is_int(v):
    try:
        int(v)
        return true
    except ValueError:
        return False
    
def is_float(v):
    try:
        float(v)
        return true
    except ValueError:
        return False

def test():
    v = 'Kud'
    if is_int(v):
        print 'partha'
    else:
        print 'not partha'
    #assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    #assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])
    
if __name__ == "__main__":
    test()
