male(john).
male(paul).
male(mike).
male(david).

female(linda).
female(susan).
female(anna).
female(emma).

parent(john, paul).
parent(john, anna).
parent(linda, paul).
parent(linda, anna).
parent(paul, mike).
parent(paul, emma).
parent(susan, mike).
parent(susan, emma).
parent(anna, david).

father(X,Y):- parent(X,Y), male(X).
mother(X,Y):- parent(X,Y), female(X).

sibling(X,Y):- parent(Z,X), parent(Z,Y), X\=Y.
brother(X,Y):- sibling(X,Y), male(X).
sister(X,Y):- sibling(X,Y), female(X).

grandparent(X,Y):- parent(X,Z), parent(Z,Y).
grandfather(X,Y):- grandparent(X,Y), male(X).
grandmother(X,Y):- grandparent(X,Y), female(X).

uncle(X,Y):- brother(X,Z), parent(Z,Y).
aunt(X,Y):- sister(X,Z), parent(Z,Y).