import z3
xal, xam, xar, xbl, xbm, xbr, xcl, xcm, xcr = z3.Bools('xal xam xar xbl xbm xbr xcl xcm xcr')
s = z3.Solver()

# Alice does not sit next to Charlie
s.add( z3.And( z3.Implies( z3.Or(xal, xar), z3.Not(xcm) ), z3.Implies( xam, z3.And( z3.Not(xcl), z3.Not(xcr)))))

# Alice does not sit on the leftmost chair
s.add( z3.Not(xal) )

# Bob does not sit to the right of Charlie (if Charlie is L, Bob is not M; if Charlie is M, Bob is not R)
s.add( z3.Implies(xcl, z3.Not(xbm)) )
s.add( z3.Implies(xcm, z3.Not(xbr)) )

# Each person gets at least one chair
s.add( z3.Or(xal, xam, xar) )
s.add( z3.Or(xbl, xbm, xbr) )
s.add( z3.Or(xcl, xcm, xcr) )

# Every person gets at most one chair
s.add( z3.Implies(xal, z3.And(z3.Not(xam), z3.Not(xar))) )
s.add( z3.Implies(xam, z3.And(z3.Not(xal), z3.Not(xar))) )
s.add( z3.Implies(xar, z3.And(z3.Not(xal), z3.Not(xam))) )

s.add( z3.Implies(xbl, z3.And(z3.Not(xbm), z3.Not(xbr))) )
s.add( z3.Implies(xbm, z3.And(z3.Not(xbl), z3.Not(xbr))) )
s.add( z3.Implies(xbr, z3.And(z3.Not(xbl), z3.Not(xbm))) )

s.add( z3.Implies(xcl, z3.And(z3.Not(xcm), z3.Not(xcr))) )
s.add( z3.Implies(xcm, z3.And(z3.Not(xcl), z3.Not(xcr))) )
s.add( z3.Implies(xcr, z3.And(z3.Not(xcl), z3.Not(xcm))) )

# Every chair gets at most one person
s.add( z3.Implies(xal, z3.And(z3.Not(xbl), z3.Not(xcl))) )
s.add( z3.Implies(xbl, z3.And(z3.Not(xal), z3.Not(xcl))) )
s.add( z3.Implies(xcl, z3.And(z3.Not(xal), z3.Not(xbl))) )

s.add( z3.Implies(xam, z3.And(z3.Not(xbm), z3.Not(xcm))) )
s.add( z3.Implies(xbm, z3.And(z3.Not(xam), z3.Not(xcm))) )
s.add( z3.Implies(xcm, z3.And(z3.Not(xam), z3.Not(xbm))) )

s.add( z3.Implies(xar, z3.And(z3.Not(xbr), z3.Not(xcr))) )
s.add( z3.Implies(xbr, z3.And(z3.Not(xar), z3.Not(xcr))) )
s.add( z3.Implies(xcr, z3.And(z3.Not(xar), z3.Not(xbr))) )

print( s.check() )

if s.check() == z3.sat:
    m = s.model()
    print("O posibila asezare (Left, Middle, Right):")
    chairs = ['Left', 'Middle', 'Right']
    
    # Gasim scaunul fiecaruia in model
    for person, vars in [('Alice', [xal, xam, xar]), ('Bob', [xbl, xbm, xbr]), ('Charlie', [xcl, xcm, xcr])]:
        for i, var in enumerate(vars):
            if m[var]:
                print(f"{person} sta pe: {chairs[i]}")
