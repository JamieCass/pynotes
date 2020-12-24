data = [[21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 22],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44],
 [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11],
 [2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018],
 [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]


column_names = ('hour', 'day', 'week', 'month', 'year', 'weekday')

dictionary = {key: [] for key in column_names}

dataDict = { key:list(values) for key,values in zip(column_names,zip(*data)) }



new = [values for values in zip(*data)]
print(new)