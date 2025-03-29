import tool
import readLog
def get_entries_by_extension(log, extension_string):
    if (type(extension_string) == str):
        result_logs = []
        #step = len(extension_string)
        for item in log:
            if item[9].endswith(extension_string):
                result_logs.append(item)
            #print(item[9][len(item[9])-step:len(item[9])])
            #if (item[9][len(item[9])-step:len(item[9])] == extension_string):
            #    result_logs.append(item)
        return result_logs
        #print(result_logs)
        #print(len(result_logs))
    else:
        raise TypeError("Extension must be string")

if __name__ == "__main__":
    input_logs = readLog.read(tool.readInput())
    extension = '.nsf'
    result = get_entries_by_extension(input_logs, extension)
    print(f'Extension: {extension}')
    for item in result:
        print(item)
