import sympy as sp

def getFactorizedExpression(expression):
    factor = sp.factor_nc(expression)
    return factor