import tool

def entry_to_dict(tupla:tuple)->dict:
    if tuple is tuple and len(tupla)==27:
        result = dict()
        attributes = tool.getIpAtributes()
        for i,item in enumerate(tupla):
            result.update({attributes[i]:item})
        return result
    else:
        raise ValueError(f"{tupla} is not a tuple or length!=27")