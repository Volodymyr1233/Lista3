import sys


def __isValidIp(ip:str):
    nums = ip.split('.')
    if len(nums) != 4:
        return False
    for num in nums:
        if not num.isdigit():
            return False
        else:
            if not (0<=int(num)<=255):
                return False
    if int(nums[0])==0:
        return False
    return True

def __isValidDomain(domain:str):
    domain_parts = domain.split('@')
    if len(domain_parts) != 2:
        return False
    if len(domain_parts[0])==0:
        return False
    if len(domain_parts[1])==0:
        return False
    if not len(domain_parts[1].strip('.'))==2:
        return False
    return True

class InvalidIp(Exception):
    def __init__(self, message:str):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f'Invalid Ip: {self.message}'

def getEntriesByAddr(tuples:[str], addr:str):
    if len(tuples) == 0:
        raise ValueError("empty tuples")
    elif __isValidIp(addr) or __isValidDomain(addr):
        result = []
        for tup in tuples:
            for value in tup:
                if value == addr:
                    result.append(value)
                    break
    else:
        raise InvalidIp(addr)


