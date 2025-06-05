from sympy import *

def round_expr(expr, num_digits):
    return expr.xreplace({n : round(n, num_digits) for n in expr.atoms(Number)})
    
    
def latex_val(t):
    cansp = sympify(str(t).replace('_', ''))
    cansp = cansp.subs(dict([(str(p).replace('_', ''), v) for p, v in t.par_values['d0'].items()]))
    #cansp = sympy.simplify(cansp)
    return latex(round_expr(cansp, 2))

#he hagut de crear aquesta expressió perquè amb el round a dos decimals de l'anterior funció hi havia problemes
def latex_val_file_generator(t):
    cansp = sympify(str(t).replace('_', ''))
    cansp = cansp.subs(dict([(str(p).replace('_', ''), v) for p, v in t.par_values['d0'].items()]))
    #cansp = sympy.simplify(cansp)
    return latex(round_expr(cansp, 3))