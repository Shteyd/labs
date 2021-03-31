counter = 0; new_counter = 0
some_dict = {
    '1': '123',
    2: '12134',
    '3': [
        '111',
        {
            11: 'afxcz',
            '12': 123
        },
        {
            13: 12323,
            '14': {
                15: 123,
                '16': 12345,
            },
        }
    ],
    '4': {
        '5': 123,
        6: '567',
    },
    '7': 25257,
    '8': {
        '9': 123,
        10: '567',
    },
}

def parseList(listName, new_counter):
    for j in listName:
        if type(j) == dict:
            newDict = j
            new_counter += parseDict(newDict, counter)
    return new_counter


def parseDict(dictName, counter):
    dictKeys = list(dictName.keys())
    counter += len(dictKeys)
    for i in range(len(dictName)):
        if type(dictName.get(dictKeys[i])) == dict:
            newDict = dictName.get(dictKeys[i])
            counter = parseDict(newDict, counter)
        if type(dictName.get(dictKeys[i])) == list:
            listName = dictName.get(dictKeys[i])
            counter += parseList(listName, new_counter)
    return counter + new_counter

print(parseDict(some_dict, counter))