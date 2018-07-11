def region ( text ):
    """This function computing the risk multiplier by the following rules. 
    
    >>>multipliers.region('large city in the northwest United States')
    1.0
    >>>multipliers('rural Midwest America')
    1.2100000000000002
    >>>multipliers.region('small town in the western USA')
    1.1550000000000002
    """
    score = 1.0
    descript = text.split(' ')
    descript_low = [element.lower() for element in descript]
    for j in descript_low:
        if j == "united":
            a=descript_low.index("united")
            if descript_low[a+1] =="states":
                score = score +0.05
    for i in descript_low:
        if i == "america" or i == "usa":
            score = score + 0.05
        if i == "midwest":
            score = score + 0.05
        if i == "northwest" or i == "northeast":
            score = score - 0.05
    for k in descript_low:    
        if k == "small" or k == "rural":
            score = score * 1.1
    return score
