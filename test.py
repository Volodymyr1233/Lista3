import get_failed_reads
import tool
attributes = tool.getIpAtributes()

def readFile(path, countLines=-1):
    if countLines < 0:
        with open(path) as f:
            return f.read()
    else:
        with open(path) as f:
            return ''.join(f.readlines()[:countLines])


def print_test(tuples:[tuple]):
   print(f'tuples size: {len(tuples)}')
   for index_a,atr in enumerate(attributes):
       print(index_a,atr,sep=':')
       if len(tuples)==0:
           print('empty')
       for i,item in enumerate(tuples):
           if len(item) == 27:
               print(f'{i}: {item[index_a]}')
           else:
               print(f'{i}: invalid length {len(item)}')
       print('------------------------------')

def print_dicts(d:dict):
    for key, value in d.items():
        print(f'{key}: {value}')

import readLog
import print_pretty_logs

tuples = readLog.read(readFile('test.txt'))
print_pretty_logs.print_pretty_logs(tuples)

