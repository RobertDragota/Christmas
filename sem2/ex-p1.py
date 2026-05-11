import z3

x = z3.Bool('x')
y = z3.Bool('y')
z = z3.Bool('z')


F = z3.Implies(x, y)
F = z3.And(F, z3.Implies(z, z))

print(F)

z3.solve(F)

z3.solve(z3.Not(F))

