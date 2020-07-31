def search(lookup, file):
    '''
        Function to search through notes for certain phrase

        Params
        ---------------
        lookup: str
        file: location of the file we are searching through
    '''
    
    with open(file) as f:
        datafile = f.readlines()

        function_lookup = [x for x in datafile if lookup in x.split()]
        l = function_lookup[0]
        line_to_start = datafile.index(l)

        all_funtions = []
        for l in function_lookup:
            print('*'*80)
            if lookup == '#':
                comment = test_word
            line_to_start = datafile.index(l)
            print('START INDEX: ',line_to_start, '\n')

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
            print('END INDEX: ',line_to_end)
            all_funtions.append(end_up)

search('def', file = '/Users/jamie/Coding/pynotes/numpy_utils.py')
