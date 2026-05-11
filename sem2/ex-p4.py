import z3

# declare variables
X = z3.Bool('X')
Y = z3.Bool('Y')
Z = z3.Bool('Z')

# define formula
F = z3.And( z3.Implies(X, z3.Implies(Y, Z)), X)

print(F)

z3.solve(F) # find a model for F

# find a counterexample for F
z3.solve(z3.Not(F))
