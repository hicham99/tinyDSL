import sys
import json


def main() :
    input_data = json.load(open('queryExample.json'))

    if 'fields' in input_data :
        a = 'SELECT ' + selector(input_data['fields']) + ' FROM crawls'
    else:
        print 'Selector field not defined'
        sys.exit(1)

    if 'filters' in input_data:
        a+= ' WHERE ' + filters(input_data['filters'])
    print (a)


# recursive data selection function
def selector (liste):
    if len(liste) == 0:
        print 'no selector defined'
        sys.exit(1)
    elif len(liste) == 1:
        return liste[0]
    else:
        return liste[0] + ',' + selector(liste[1:])

def filters(predicate) :

    if 'and' in predicate :
        if len(predicate['and']) > 1 :
            return '(' + filters(predicate['and'][0]) +' AND ' + filters({'and':predicate['and'][1:]}) + ')'
        else:
            return filters(predicate['and'][0])

    elif 'or' in predicate :
        if len(predicate['or']) > 1 :
            return '(' + filters(predicate['or'][0]) + ' OR ' + filters({'or':predicate['or'][1:]}) + ')'
        else:
            return filters(predicate['or'][0])

    else:
        return predicate['field'] + ' ' + formatting(predicate['predicate'] , predicate['value'])

def formatting(predicate,value):
    if predicate == 'gt':
        return '> ' + str(value)
    elif predicate == 'equal':
        return '= ' + str(value)
    elif predicate == 'lt':
        return '< ' + str(value)
    elif predicate == 'contains':
        return 'LIKE \'%' + str(value) +'%\''
    else:
        print 'unknown predicate'
        sys.exit(0)


if __name__ == '__main__':
  main()
