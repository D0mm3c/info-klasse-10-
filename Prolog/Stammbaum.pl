% Autor: D0mm3
% Datum: 01.09.2021
%elternteil = X
vater(Vater, Kind) :- maennlich(Vater), kind(Vater, Kind).
mutter(Mutter, Kind) :- weiblich(Mutter), kind(Mutter, Kind).
elternteil(EL, Kind) :-vater(EL, Kind); mutter(EL, Kind).

%kind = Y
sohn(EL, Kind) :- maennlich(Kind), elternteil(EL, Kind).
tochter(EL, Kind):- weiblich(Kind), elternteil(EL, Kind).

%geschwister = G
bruder(Geschwister, Kind):- maennlich(Geschwister), elternteil(EL, Geschwister),
                             elternteil(EL, Kind), Geschwister \= Kind.
schwester(Geschwister, Kind):- weiblich(Geschwister), elternteil(EL, Geschwister),
                                elternteil(EL, Kind), Geschwister \= Kind.
geschwister(Geschwister, Kind):- bruder(Geschwister, Kind); schwester(Geschwister, Kind).

%grosseltern
opa(Opa, Enkel):- vater(Opa, Kind), elternteil(Kind, Enkel).
oma(Oma, Enkel):- mutter(Oma, Kind), elternteil(Kind, Enkel).
grosseltern(Grosseltern, Enkel):- opa(Grosseltern, Enkel); oma(Grosseltern, Enkel).


%tante/onkel
onkel(Onkel, NichteNeffe):- elternteil(EL, NichteNeffe), bruder(Onkel, EL).
tante(Tante, NichteNeffe):- elternteil(EL, NichteNeffe), schwester(Tante, EL).
%tanteoderonkel(TantOnk, NichteNeffe):- onkel(Onkel, NichteNeffe); tante(Tante, NichteNeffe).

%cousin/cousine
cousin(Cousin, Ich):- sohn(EL, Cousin), (tante(El, Ich); onkel(EL, Ich)).
cousine(Cousine, Ich):- tochter(EL, Cousine), (tante(EL, Ich); onkel(EL, Ich)).

maennlich(bart).
maennlich(homer).
maennlich(clancy).
maennlich(jojo).
maennlich(chester).
maennlich(pepe).
maennlich(francoise).

weiblich(lisa).
weiblich(maggie).
weiblich(ling).
weiblich(marge).
weiblich(patty).
weiblich(selma).
weiblich(jacqueline).
weiblich(charlene).
weiblich(bambi).
weiblich(monique).
weiblich(lalique).
weiblich(fifi).
weiblich(coquette).
weiblich(jacques).

%francoise
kind(francoise, pepe).
kind(francoise, monique).
kind(francoise, lalique).
kind(francoise, fifi).
kind(francoise, coquette).
 
%jacques
kind(jacques, pepe).
kind(jacques, monique).
kind(jacques, lalique).
kind(jacques, fifi).
kind(jacques, coquette).

%bambi
kind(bambi, clancy).
kind(bambi, charlene).
kind(bambi, jojo).
kind(bambi, chester).

% pepe
kind(pepe, clancy).
kind(pepe, charlene).
kind(pepe, jojo).
kind(pepe, chester).

%jacqueline

kind(jacqueline, marge).
kind(jacqueline, patty).
kind(jacqueline, selma).

%clancy
kind(clancy, marge).
kind(clancy, patty).
kind(clancy, selma).

%homer
kind(homer, bart).
kind(homer, lisa).
kind(homer, maggie).

%marge
kind(marge, bart).
kind(marge, lisa).
kind(marge, maggie).

%selma
kind(selma, ling).

