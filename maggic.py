def risk_factor ( factor ):
    """(list) -> int
    Return risk factor per MAGGIC scoring
    """
    factor_low = [element.lower() for element in factor]
    count = 0
    for i in factor_low:
        if i == "male":
            count = count +1
        if i == "smoker":
            count = count +1
        if i == "diabetic":
            count = count +3
        if i == "copd":
            count = count +2
        if i == "first diagnosis of hf within 18 months":
            count = count +2
        if i == "not on beta blocker":
            count = count +3
        if i == "not on ace-i/arb":
            count = count +1
    return count

def ejection_fraction ( ef ):
    """(int) -> int
    Return ejection fraction per MAGGIC scoring
    """
    if ef < 20:
        return 7
    elif ef >= 20 and ef <= 24:
        return 6
    elif ef >= 25 and ef <= 29:
        return 5
    elif ef >= 30 and ef <= 34:
        return 3
    elif ef >= 35 and ef <= 39:
        return 2
    else:
        return 0

def nyha_class ( point ):
    """(int) -> int
    Return nyha class point per MAGGIC scoring
    """
    if point == 1:
        return 0
    elif point == 3:
        return 6
    elif point == 4:
        return 8
    else:
        return point
    
def creatinine ( ranges ):
    """(int) -> int
    Return creatinine ranges per MAGGIC scoring
    """
    if ranges < 90:
        return 0
    elif ranges >= 90 and ranges <= 109:
        return 1
    elif ranges >= 110 and ranges <= 129:
        return 2
    elif ranges >= 130 and ranges <= 149:
        return 3
    elif ranges >= 150 and ranges <= 169:
        return 4
    elif ranges >= 170 and ranges <= 209:
        return 5
    elif ranges >= 210 and ranges <= 249:
        return 6
    else:
        return 8
    
def bmi(index ):
    """(int) -> int
    Return bmi per MAGGIC scoring
    """
    if index < 15:
        return 6
    elif index >= 15 and index <= 19:
        return 5
    elif index >= 20 and index <= 24:
        return 3
    elif index >= 25 and index <= 29:
        return 2
    else:
        return 0
    
def systolic_bp( ef, bp ):
    """(int) -> int
    Return systolic_bp per MAGGIC scoring
    """
    if ef < 30:
        if bp < 110:
            return 5
        elif bp >= 110 and bp <= 119:
            return 4
        elif bp >= 120 and bp <= 129:
            return 3
        elif bp >= 130 and bp <= 139:
            return 2
        elif bp >= 140 and bp <= 149:
            return 1
        else:
            return 0
    if ef >= 30 and ef <= 39:
        if bp < 110:
            return 3
        elif bp >= 110 and bp <= 119:
            return 2
        elif bp >= 120 and bp <= 129:
            return 1
        elif bp >= 130 and bp <= 139:
            return 1
        else:
            return 0
    if ef >= 40:
        if bp < 110:
            return 2
        elif bp >= 110 and bp <= 119:
            return 1
        elif bp >= 120 and bp <= 129:
            return 1
        else:
            return 0

def age( ef, year ):
    """(int) -> int
    Return age per MAGGIC scoring
    """
    if ef < 30:
        if year < 55:
            return 0
        elif year >= 56 and year <= 59:
            return 1
        elif year >= 60 and year <= 64:
            return 2
        elif year >= 65 and year <= 69:
            return 4
        elif year >= 70 and year <= 74:
            return 6
        elif year >= 75 and year <= 79:
            return 8
        else:
            return 10
    if ef >= 30 and ef <= 39:
        if year < 55:
            return 0
        elif year >= 56 and year <= 59:
            return 2
        elif year >= 60 and year <= 64:
            return 4
        elif year >= 65 and year <= 69:
            return 6
        elif year >= 70 and year <= 74:
            return 8
        elif year >= 75 and year <= 79:
            return 10
        else:
            return 13
    if ef >= 40:
        if year < 55:
            return 0
        elif year >= 56 and year <= 59:
            return 3
        elif year >= 60 and year <= 64:
            return 5
        elif year >= 65 and year <= 69:
            return 7
        elif year >= 70 and year <= 74:
            return 9
        elif year >= 75 and year <= 79:
            return 12
        else:
            return 15
        
def score(factor, ef, point, ranges, index, bp, year ):
    """(list, int, int, int, int, int, int)
    This function uses the logic form from https://www.mdcalc.com/maggic-risk-calculator-heart-failure#evidence to compute Heart Failure Risk score,
        
    >>> score(factor = ['male','COPD'], ef= 42, point = 2, ranges = 112, index = 22, bp = 123, year = 45)
    11
    """
    return risk_factor(factor) + ejection_fraction ( ef ) + nyha_class ( point ) + creatinine ( ranges ) + bmi( index ) + systolic_bp( ef, bp ) + age( ef, year ) 
