def check(lookup, file):
    with open(file) as f:
        datafile = f.readlines()
    #found = False  # This isn't really necessary
    for line in datafile:
        if lookup.lower() in line:
            # found = True # Not necessary
            return ''.join(x for x in line)
    return False  # Because you finished the search without finding

check('', file = '/Users/jamie/Coding/F1_code/google_trends_tracker.py')
