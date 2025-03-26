%a
% movie(american_beauty, ANO)
%b
mesmo_ano(F1,F2,ANO):- movie(F1,ANO),movie(F2,ANO), F1 \=F2.
%c
antes_ano(F1,ENTRADA,ANO):- movie(F1,ANO),ANO < ENTRADA.
%d
depois_ano(F1,ENTRADA,ANO):- movie(F1,ANO),ANO > ENTRADA.
%e
%diretor_do_ator(scarlett_johansson)
diretor_do_ator(DIRETOR,ATOR) :- (   actress(FILME,ATOR,_);   actor(FILME,ATOR,_)),director(FILME,DIRETOR).
%f
ator_diretor(PESSOA, FILME):- ((actor(FILME, PESSOA,_);actress(FILME, PESSOA,_)),director(FILME,PESSOA)).
%g
%coestrela(john_goodman,jeff_bridges,F1)
coestrela(A1,A2,F1):- (actor(F1,A1,_);actress(F1,A1,_)),(actor(F1,A2,_);actress(F1,A2,_)).
