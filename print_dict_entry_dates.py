
import tool
import readLog
import log_to_dict
from datetime import datetime

from test import attributes


def __get_str_from_user(logs:[dict])->str:
    result = ''
    for i,log in enumerate(logs):
        result += f'\tlog{i}\n'
        for key,value in log.items():
            result += f'\t\t{key}: {value}\n'
    return result

def __get_first_last_date(logs:[dict])->(datetime.date,datetime.date):
    if not isinstance(logs, list) or len(logs)==0:
        return (None,None)
    else:
        #ts to czas , ts=0
        time_name = tool.getIpAtributes()[0]
        min_log = logs[0][time_name]
        max_log = logs[0][time_name]
        for i in range(1,len(logs)):
            if logs[i][time_name] < min_log:
                min_log = logs[i]
            if logs[i][time_name] > max_log:
                max_log = logs[i]
        return min_log,max_log

def __get__percentage(logs:[dict])->str:
    """:return (GET,POST)"""
    if not isinstance(logs, list) or len(logs)==0:
        return ''
    #method 7
    method_name = tool.getIpAtributes()[7]
    all_methods_count = 0
    methods_counter_dict = dict()
    for log in logs:
            if method_name in log:
                if log[method_name] in methods_counter_dict:
                    methods_counter_dict[log[method_name]] += 1
                else:
                    methods_counter_dict[log[method_name]] = 1
                all_methods_count += 1
            else:
                raise ValueError(f"{method_name} not in log dictionary")
    result = ''
    for key,value in methods_counter_dict.items():
        result += f'{key}:{methods_counter_dict[key] / all_methods_count * 100}%, '
    return result


def str_dict_entry_dates(log_dict:dict[str,[dict]])->str:
    if not isinstance(log_dict, dict):
        raise ValueError("log_dict must be a dictionary")
    elif len(log_dict) == 0:
        return 'empty'
    else:
        result = ''
        for uid,logs in log_dict.items():
            result += f'UserId: {uid}\n'
            result += f'\tNumber of requests: {len(logs)}\n'
            (first,last) = __get_first_last_date(logs)
            if first is not None and last is not None:
                result += f'\tFirst date: {first}\n'
                result += f'\tLast date: {last}\n'
            result += f'\t{__get__percentage(logs)}'
            result +=('\n'+(__get_str_from_user(logs)))
        return result

if __name__ == '__main__':
    tuples = readLog.read(tool.readInput())
    try:
        tool.writeOutput(str_dict_entry_dates(log_to_dict.log_to_dict(tuples)))
    except ValueError as e:
        tool.writeOutput(e)