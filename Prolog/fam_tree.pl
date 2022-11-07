male(aanimuthu).
male(subramaniyan).
male(raja).
male(selvaraj).
male(ajith).
male(avinash).

female(veni).
female(vairam).
female(chandra).
female(kavitha).

spouse(aanimuthu,veni).
spouse(veni,aanimuthu).
spouse(subramaniyan,vairam).
spouse(vairam,subramaniyan).
spouse(raja,chandra).
spouse(chandra,raja).
spouse(kavitha,selvaraj).
spouse(selvaraj,kavitha).

parent(aanimuthu,chandra).
parent(veni,chandra).
parent(vairam,raja).
parent(subramaniyan,raja).
parent(vairam,kavitha).
parent(subramaniyan,kavitha).
parent(raja,ajith).
parent(raja,avinash).
parent(chandra,ajith).
parent(chandra,avinash).

sibling(X,Y):- parent(Z,X),parent(Z,Y).
brother(X,Y):- male(X),sibling(X,Y),X\==Y.
sister(X,Y):- female(X),sibling(X,Y),X\==Y.
son(X,Y):- male(X),parent(Y,X).
daughter(X,Y):- female(X),parent(Y,X).
aunty(X,Y):- (sister(X,Z),parent(Z,Y)).
uncle(X,Y):- (brother(X,Z),parent(Z,Y));(spouse(X,Z),aunty(Z,Y)).