# import multiprocessing
# import time
# def timetaken_log(start, stepname=''):
#     end = time.time()
#     hours, rem = divmod(end-start, 3600)
#     minutes, seconds = divmod(rem, 60)
#     str_time = "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds)
#     print(str_time, stepname)
#     return end, str_time
# cpus = multiprocessing.cpu_count()
# "There are %d CPUs on this machine" % cpus
# def example_func(n):
#     return n**2
# ## Example input list
# input_list = [x for x in range(1000000)]
# # Create pool with available cpus
# p = multiprocessing.Pool(cpus)
# # Run multiprocess
# start_time = time.time()
# returned_values = p.map(example_func, input_list)
# end_time = timetaken_log(start_time, stepname='Running with Multiprocessing')
# p.terminate()
#
#
# # Run without multiprocess
# start_time = time.time()
# [example_func(i) for i in input_list]
# end_time = timetaken_log(start_time, stepname='Running without Multiprocessing')


import os
from multiprocessing import Process
def doubler(number):
    """
    A doubling function that can be used by a process
    """
    result = number * 2
    proc = os.getpid()
    print('{0} doubled to {1} by process id: {2}'.format(
        number, result, proc))
if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []

    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
