import z3
x, y = z3.Bools('x y')

s = z3.Solver()

s.add( z3.Implies(x, y) )
s.add( z3.Implies(y, x) )

print( s.check() )
print( s.model() )

s.add( x )

print( s.check() )
print( s.model() )

s.add( z3.Not(y) )

print( s.check() )
