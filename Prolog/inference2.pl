enemy(nono,america).
owns(nono,m1).
missile(m1).
sell(west,m1,nono).
american(west).
hostile(nono).
crime(X):- american(X),sell(X,W,H),weapons(W),hostile(H).
weapons(X):- missile(X).