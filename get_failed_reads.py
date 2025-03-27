

def get_failed_reads(tuples:[tuple],linked:bool=False)->[tuple]:
    if len(tuples)==0:
        return []
    result4 = []
    result5 = []
    for item in tuples:
        if len(item)==27:
            if 500>item[14]>=400:
                result4.append(item)
            elif 600>item[14]>=500:
                result5.append(item)
    return (result4+result5) if linked else result4,result5
