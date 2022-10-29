sum(X,Y):-
 S is X+Y,
 write(S).

sub(X,Y):-
 S is X-Y,
 write(S).

mul(X,Y):-
 S is X*Y,
 write(S).

div(X,Y):-
 S is X/Y,
 write(S).

intdiv(X,Y):-
 S is X//Y,
 write(S).

modu(X,Y):-
 S is mod(X,Y),
 write(S).