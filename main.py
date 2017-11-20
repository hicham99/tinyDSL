import sys

input_data = {
'selector': ['a','b','c']}


def main():
    if 'selector' in input_data :
        a = 'SELECT ' + selector(input_data['selector'])+' FROM crawls'
    else:
        print 'Selector field not defined'
        sys.exit(1)

    if 'filters' in input_data:
        pass
    print (a)


# recursive data selection function
def selector (liste):
    if len(liste)==0:
        print 'no selector defined'
        sys.exit(1)
    elif len(liste)==1:
        return liste[0]
    else:
        return liste[0]+','+selector(liste[1:])

def filters(predicate):
    pass


if __name__ == '__main__':
  main()
