def solve(a=0, b=0, c=0, d=0):
    '''
    ax^2 + bx + c = d 
    '''
    if a != 0:
        D = b ** 2 - 4 * a * (c - d)  
        Ds = abs(D) ** 0.5 
        return (-b + Ds) / (2 * a), (-b - Ds) / (2 * a)
    elif b != 0:
        return (d - c) / b
    else:
        raise ValueError('Invalid equation')
