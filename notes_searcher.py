
import pandas as pd
import numpy as np

def check(lookup, file):
    '''
        Function to search notes for certain phrase

        Params
        ------------------
        lookup: str
        file: location of file you are searching for
    '''

    with open(file) as f:
        datafile = f.readlines()

    return datafile

    #found = False  # This isn't really necessary
    for line in datafile:
        if lookup.lower() in line:
            # found = True # Not necessary
            return True
    return False  # Because you finished the search without finding


# Run
datafile =  check('format', file='/Users/dshaw/Documents/DBS/python_code/python_utils/numpy_utils.py')



'format' in ' this is an example of format here'
'format' in ' this is an example of formatting here'

'format' in ' this is an example of format here'.split()
'format' in ' this is an example of formatting here'.split()


## Looks for word within words
lines_with_lookup = [x for x in datafile if 'format' in x]

## Looks for distinct word in list of words (Split by space), not within words
[x for x in datafile if 'format' in x.split()]


test_str = lines_with_lookup[0]
test_str = lines_with_lookup[1]
test_str = lines_with_lookup[2]



## Looks for word within words
lines_with_lookup = [x for x in datafile if 'format' in x]

for test_str in lines_with_lookup:
    print('*'*100)
    print("SEARCHING FOR:",test_str)
    ## FOR COMMENTS AS FIRST VALUE  i.e '# Change format from mathematical to float\n'
    if test_str[0]=='#':
        comment = test_str

        # Look for the location of the code in the file
        test_loc = datafile.index(test_str)

        # Look for the next blank link (Where our code ends)
        lines_to_keep = datafile[test_loc:].index('\n')

        # Final Code string
        code_str = ''.join(datafile[test_loc:test_loc+lines_to_keep])
        print('\nCOMMENT\n')
        print(code_str)

    else:
        test_loc = datafile.index(test_str)

        # Reverse the list & find first comment
        inverselist = datafile[:test_loc+1][::-1]
        inverselist_first_val = [x[0] for x in inverselist]
        first_comment_index = inverselist_first_val.index('#')

        # Look for the next blank link (Where our code ends)
        lines_to_keep = datafile[test_loc:].index('\n')

        # Final Code string
        code_str = ''.join(datafile[test_loc-first_comment_index:test_loc+lines_to_keep])
        print('\nNON COMMENT\n')
        print(code_str)
