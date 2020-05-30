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

datafile = check('groupkeywords', file = '/Users/jamie/Coding/pynotes/numpy_utils.py')

datafile

lines_lookup = [x for x in datafile if 'groupkeywords' in x.split()]
type(lines_lookup)
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










datafile
#finds where all the functions START.
function_lookup = [x for x in datafile if 'def' in x.split()]
function_lookup


l = function_lookup[0]
line_to_start = datafile.index(l)
l
line_to_start
#
# #find where functions END
# counter = 0
# for line in datafile[line_to_start:]:
#     if counter < 1:
#         if ':' in line:
#             line_to_end = datafile.index(line)
#             print(line_to_end, line)
#             counter +=1

all_funtions = []
for l in function_lookup:
    line_to_start = datafile.index(l)

    #find where functions END
    counter = 0
    for line in datafile[line_to_start:]:
        if counter < 1:
            if 'return' in line:
                line_to_end = datafile.index(line)
                counter +=1
    #find the full code for function and save it as end_up. Then join it together so it prints it nicely
    end_up = datafile[line_to_start:line_to_end+1]
    print(''.join(end_up))
    all_funtions.append(end_up)






end_up = datafile[line_to_start:line_to_end+1]
print(''.join(end_up))


datafile[20:31]
