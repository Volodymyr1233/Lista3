from print_pretty_logs import print_pretty_logs

def get_entries_by_code(log, status_code):
    if (__validate_status_code(status_code)):
        result_logs = []
        for item in log:
            if (item[14] == status_code):
                result_logs.append(item)
        print_pretty_logs(result_logs)
        print(len(result_logs))
    else:
        raise TypeError("Your status code is incorrect")


def __validate_status_code(status_code):
    if (type(status_code) == int and status_code > 100 and status_code < 600):
        return True
    return False