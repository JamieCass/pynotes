def check(file):
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

#define datafile as the file we want to open.
datafile = check(file = '/Users/jamie/Coding/pynotes/numpy_utils.py')
print(''.join(datafile))


#define the work we want to look up.
##########################################
str_to_lookup = 'def'
##########################################

#make sure what we are searching for is a seperate word/string.. using the .split()
word_lookup = [x for x in datafile if str_to_lookup in x.split()]
word_lookup

l = word_lookup[0]
l

line_to_start = datafile.index(l)
line_to_start

end_line = [x for x in datafile if 'return' in x.split()]
end_line

e = end_line[0]

line_to_end = datafile.index(e)
line_to_end
datafile[line_to_start:line_to_end+1]

l
for l in word_lookup:
    line_to_start = datafile.index(l)
    print(line_to_start)
    counter = 0
    for line in datafile[line_to_start:]:
        if counter < 1:
            if e in line:
                line_to_end = datafile.index(e)
                print(line_to_end)

    end_up = datafile[line_to_start:line_to_end+1]

end_up
import cProfile
cProfile.run('2+2')
