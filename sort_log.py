def sort_cryt(element, index):
    return element[index]

def sort_log(log, index):
    try:
        return sorted(log, key=lambda element: sort_cryt(element, index))
    except IndexError:
        raise IndexError("Your index is too high!")