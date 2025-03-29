import entry_to_dict
import get_entries_by_code
import get_entries_by_extension
import get_failed_reads
import log_to_dict
import print_pretty_logs
import readLog
import sort_log
import get_entries_by_addr

def readFile(path, countLines=-1):
    if countLines < 0:
        with open(path) as f:
            return f.read()
    else:
        with open(path) as f:
            return ''.join(f.readlines()[:countLines])


tuples = readLog.read(readFile('test.txt'))

print('readLog.py')
for item in tuples:
    print(item)
print('\n\n\n')


print('sort_log.py')
print('sortowanie po dacie (atrybut 0)')
for item in sort_log.sort_log(tuples,0):
    print(item)
print('sortowanie po ip (atrybut 2)')
for item in sort_log.sort_log(tuples, 2):
        print(item)
print('\n\n\n')

print('get_entries_by_addr.py')
addr = '192.168.201.79'
print(f'adres: {addr}')
for item in get_entries_by_addr.getEntriesByAddr(tuples,addr):
    print(item)
addr = 'domena@gmail.com'
print(f'\nadres: {addr}')
for item in get_entries_by_addr.getEntriesByAddr(tuples,addr):
    print(item)
print('\n\n\n')



print('get_entries_by_code.py')
code = 404
print(f'\ncode: {code}')
for item in get_entries_by_code.get_entries_by_code(tuples,code):
    print('...',item[14:])
code = 209
print(f'\ncode: {code}')
for item in get_entries_by_code.get_entries_by_code(tuples,code):
    print('...',item[14:])
print('\n\n\n')




print('get_failed_reads.py')
fail_tup = get_failed_reads.get_failed_reads(tuples)
print('*'*50,'4XX')
for item in fail_tup[0]:
    print('4XX: ...',item[14:])
print('*'*50,'5XX')
for item in fail_tup[1]:
    print('5XX ...',item[14:])
print('\n\n\n')




print('get_entires_by_extension.py')
extension = '.nsf'
print(f'extension: {extension}')
for item in get_entries_by_extension.get_entries_by_extension(tuples,extension):
    print('...',item[9:])
extension = '.jpg'
print(f'extension: {extension}')
for item in get_entries_by_extension.get_entries_by_extension(tuples,extension):
    print('...',item[9:])
print('\n\n\n')


print('entry_to_dict.py')
print(tuples[0],'\n')
entr_d = entry_to_dict.entry_to_dict(tuples[0])
for key,item in entr_d.items():
    print(key,':\t',item)
print('\n\n\n')


print('print_dict_entry_dates.py')
print('\tlog_to_dict.py\n\n')
print_pretty_logs.print_pretty_logs(tuples)

