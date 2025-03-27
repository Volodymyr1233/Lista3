import tool
from datetime import datetime

__format = '%d-%m-%Y'


def read(input:str):
        file = input.split('\n')
        lst  = []
        for line in file:
            if len(line)==0:
                continue
            temp= line.split('\t')
            micro_lst = []
            for item in temp:
                if item.isnumeric():
                    micro_lst.append(float(item))
                else:
                    try:
                        micro_lst.append(datetime.strptime(item,__format))
                    except ValueError:
                        micro_lst.append(item)
            lst.append(tuple(micro_lst))
        return lst





if __name__ == "__main__":
    a = read(tool.readInput())
    for item in a:
        print(len(item))

