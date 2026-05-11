import z3

s = z3.Solver()

if s.check() == z3.sat:
    model = s.model()
    print( model )
