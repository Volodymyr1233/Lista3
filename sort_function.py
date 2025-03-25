def sort_cryt(element, index):
    if (index > len(element)-1):
        raise IndexError("Index is more then tupple length")
    return element[index]

def sort_log(log, index):
    return sorted(log, key=lambda element: sort_cryt(element, index))