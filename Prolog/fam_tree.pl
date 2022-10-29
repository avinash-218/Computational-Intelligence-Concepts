female(chandra).
male(raja).
male(ajith).
male(avinash).
male(vijith).
male(manoharan).
parent(chandra,ajith).
parent(chandra,avinash).
parent(raja,ajith).
parent(raja,avinash).
spouse(raja,chandra).
spouse(chandra,raja).
parent(ajith,vijith).
parent(avinash,manoharan).
sibling(ajith,avinash).
sibling(avinash,ajith).
child(avinash,raja).
child(ajith,raja).
child(avinash,chandra).
child(ajith,chandra).
mother(X,Y):- parent(X,Y),female(X).
father(X,Y):- parent(X,Y),male(X).