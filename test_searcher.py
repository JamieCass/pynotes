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
datafile


#define the work we want to look up.
##########################################
str_to_lookup = 'def'
##########################################

#make sure what we are searching for is a seperate word/string.. using the .split()
word_lookup = [x for x in datafile if str_to_lookup in x.split()]
word_lookup
