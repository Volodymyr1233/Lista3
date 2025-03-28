import tool
from datetime import datetime
from get_entries_by_extension import get_entries_by_extension




def read(input:str):
        file = input.split('\n')
        lst  = []
        for line in file:
            if len(line)==0:
                continue
            temp= line.split('\t')
            micro_lst = []
            try:
                micro_lst.append(datetime.fromtimestamp(float(temp[0])))
            except ValueError:
                continue
            for i in range(1,len(temp)):
                item = temp[i]
                if item.isnumeric():
                    micro_lst.append(float(item))
                else:
                        micro_lst.append(item)
            lst.append(tuple(micro_lst))
        return lst





if __name__ == "__main__":
    a = read(tool.readInput())
    get_entries_by_extension(a, "jpg")


