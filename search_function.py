def check(lookup):
    with open('cards.py') as f:
        datafile = f.readlines()
    #found = False  # This isn't really necessary
    for line in datafile:
        if lookup.lower() in line:
            # found = True # Not necessary
            return True
    return False  # Because you finished the search without finding

check('')
