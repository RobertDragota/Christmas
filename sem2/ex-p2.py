import z3

x = z3.Bool('x')
y = z3.Bool('y')

F = z3.Not(z3.And(x, y)) == z3.Or(z3.Not(x), z3.Not(y))

print(F)

z3.solve(F)

z3.solve(z3.Not(F))

