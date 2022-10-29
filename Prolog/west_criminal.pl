american(west).
missile(m1).
owns(nono,m1).
enemy(nono,america).
weapon(X):- missile(X).
sells(west,X,nono):- missile(X),owns(nono,X).
hostile(X):- enemy(X,america).
criminal(X):- american(X),weapon(_),sells(X,_,nono),hostile(nono).