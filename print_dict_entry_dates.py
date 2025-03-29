
import tool
import readLog
import log_to_dict
from datetime import datetime

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
                min_log = logs[i][time_name]
            if logs[i][time_name] > max_log:
                max_log = logs[i][time_name]
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

def __2xx_requests(logs:[dict])->float:
    #? nie wiem ktore to numer ma byc
    if len(logs)==0:
        return 0
    counter = 0
    request_name = tool.getIpAtributes()[14]
    for log in logs:
        if not request_name in log:
            raise ValueError(f"{request_name} not in log dictionary")
        if not isinstance (log[request_name], float):
            return 0.0
        if 300>log[request_name]>=200:
            counter += 1
    return counter/len(logs)





def str_dict_entry_dates(log_dict:dict[str,[dict]],first_user_index=0)->str:
    if not isinstance(log_dict, dict):
        raise ValueError("log_dict must be a dictionary")
    elif len(log_dict) == 0:
        return 'empty'
    else:
        result = ''
        for i_user,(uid,logs) in enumerate(log_dict.items()):
            result += f'{i_user+first_user_index}: UserId: {uid}\n'
            result += f'\tNumber of requests: {len(logs)}\n'
            (first,last) = __get_first_last_date(logs)
            if first is not None and last is not None:
                result += f'\tFirst date: {first}\n'
                result += f'\tLast date: {last}\n'
            result += f'\t{__get__percentage(logs)}\n'
            result += f'\tStatus code 2xx: {__2xx_requests(logs)}\n'
            result +=('\n'+(__get_str_from_user(logs)))
        return result

if __name__ == '__main__':
    tuples = readLog.read(tool.readInput())
    try:
        tool.writeOutput(str_dict_entry_dates(log_to_dict.log_to_dict(tuples)))
    except ValueError as e:
        tool.writeOutput(e.__str__())