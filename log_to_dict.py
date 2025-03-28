import entry_to_dict
def log_to_dict(tuples:[tuple])->dict[str,tuple]:
    if len(tuples)==0:
        return dict()
    dictionary = dict()
    #uid 1
    for item in tuples:
        if not isinstance(item,tuple):
            raise ValueError(f"{item.__class__.__name__} is not a tuple")
        if not len(item) == 27:
            raise ValueError(f"{item} length is not a valid ip length")
        if isinstance(item[1],str):
            if item[1] in dictionary:
                dictionary[item[1]].append(entry_to_dict.entry_to_dict(item))
            else:
                dictionary.update({item[1]: [entry_to_dict.entry_to_dict(item)]})
    return dictionary



