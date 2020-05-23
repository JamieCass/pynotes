def check(lookup, file):
    '''
        Function to search through notes for certain phrase

        Params
        ---------------
        lookup: str
        file: location of the file we are searching through
    '''

    with open(file) as f:
        datafile = f.readlines()

    return datafile

    #found = False  # This isn't really necessary
    for line in datafile:
        if lookup.lower() in line:
            # found = True # Not necessary
            return [x for x in datafile if lookup in x]
    return False  # Because you finished the search without finding

datafile = check('groupkeywords', file = '/Users/jamie/Coding/pynotes/coding_help.py')

datafile

lines_lookup = [x for x in datafile if 'groupkeywords' in x.split()]

test_word = lines_lookup[0]
datafile.index(test_word)

test_loc = datafile.index(test_word)
test_loc
print(test_word)

for test_word in lines_lookup:
    print('*'*80)
    print('SEARCHING FOR:', test_word)
    if test_word == '#':
        comment = test_word

        test_loc = datafile.index(test_word)

        lines_to_keep = datafile[test_word:].index('\n')

        code_str = ''.join(datafile[test_loc:test_loc+lines_to_keep])
