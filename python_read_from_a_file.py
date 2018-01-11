class A(object):
    
    def __init__(self, e):
        self.experession = e
        self.varaible = None
        self.clause = None
        self.pair = None


def main():
    aobject = A('(A + B) * (B + C)')

    print aobject.experession
    print aobject.varaible
    print aobject.clause
    print aobject.pair


main()
