:- use_module(library(date)).

% # Nazwy dni tygodnia
day(1, monday).
day(2, tuesday).
day(3, wednesday).
day(4, thursday).
day(5, friday).
day(6, saturday).
day(7, sunday).

% # Dni w które wywozimy dany rodzaj śmieci
collect_glass(X) :- X = monday ; X = saturday.
collect_plastic(X) :- X = tuesday ; X = friday ; X = sunday.
collect_metal(X) :- X = wednesday.
collect_paper(X) :- X = monday ; X = thursday ; X = saturday.

% # Zwraca dzisiejszą datę
current_date(D, M, Y) :-
  get_time(TS),
  stamp_date_time(TS, Date, -7200),
  arg(1, Date, Y),
  arg(2, Date, M),
  arg(3, Date, D).

% # Zwraca nazwe dzisiejszego dnia tygodnia
current_day(N) :-
  current_date(X, Y, Z),
  day_of_the_week(date(Z, Y, X), D),
  day(D, N).

% # X - rodzaj śmieci, Y - dzień tygodnia
% # Sprawdzenie, czy danego dnia wywozimy dany rodzaj śmieci
collect(X, Y) :-
  X = glass, collect_glass(Y) ;
  X = plastic, collect_plastic(Y) ;
  X = metal, collect_metal(Y) ;
  X = paper, collect_paper(Y).

% # X - rodzaj śmieci 
% # Sprawdzenie czy dzisiaj je wywozimy
collect_trash(X) :-
  current_day(N),
  collect(X, N).
