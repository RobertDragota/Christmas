import z3

Pair = z3.DeclareSort('Pair')

null = z3.Const('null', Pair)

cons = z3.Function('cons', z3.IntSort(), z3.IntSort(), Pair)
first = z3.Function('first', Pair, z3.IntSort())

ax1 = (null == cons(0, 0))
x, y = z3.Ints('x y')
ax2 = z3.ForAll([x, y], first(cons(x, y)) == x)

s = z3.Solver()
s.add(ax1)
s.add(ax2)

F = first(null) == 0

# check validity
s.add(z3.Not(F))
print( s.check() )
