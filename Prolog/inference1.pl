hungry(ram).
eats_quick(X):- hungry(X).
pain(X):- eats_quick(X).
medicine(X):- pain(X).	