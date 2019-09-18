import string
def rotate(text, key):
    alphalist1 = list(string.ascii_lowercase)
    shiftlist1 = alphalist1[key:]+alphalist1[:key]
    alphalist2 = list(string.ascii_uppercase)
    shiftlist2 = alphalist2[key:]+alphalist2[:key]
    corr1 = dict(zip(alphalist1, shiftlist1))
    corr2 = dict(zip(alphalist2, shiftlist2))
    result = []
    for i in text: 
        if i in corr1:
            result.append(corr1[i])
        elif i in corr2:
            result.append(corr2[i])
        else:
            result.append(i)
    return ''.join(result)