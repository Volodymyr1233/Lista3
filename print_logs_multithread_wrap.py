import concurrent.futures

import log_to_dict
import print_dict_entry_dates
import readLog
import tool
import os




if __name__ == '__main__':
    tuples = readLog.read(tool.readInput())
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futury = []
        first = 0
        window = min(5000, len(tuples)//os.cpu_count())
        while first < len(tuples):
            last = min(len(tuples), first + window)
            future = executor.submit(print_dict_entry_dates.str_dict_entry_dates,
                                     log_to_dict.log_to_dict(tuples[first:last]),first)
            futury.append(future)
            first = last
        index = 0
        while index < len(futury):
            if futury[index].done():
                print(futury[index].result())
                index += 1

