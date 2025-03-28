def get_entries_by_extension(log, extension_string):
    if (type(extension_string) == str):
        result_logs = []
        step = len(extension_string)
        for item in log:
            print(item[9][len(item[9])-step:len(item[9])])
            if (item[9][len(item[9])-step:len(item[9])] == extension_string):
                result_logs.append(item)

        print(result_logs)
        print(len(result_logs))
    else:
        raise TypeError("Extension must be string")
