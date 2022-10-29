#CEM MIL EM AMONTADA POPULAÇÃO
#TAXA ANUAL CRSCIOMENTO 1,5% POR ANO
#45 MIL EM MIRAIMA
#TAXA DE CESCIMENTO 3% POR ANO
#CALCULE E IMPRIMA O NUMERO DE ANOS NECESSÁRIOS PARA QUE A POPULAÕA DE MIRAIMA ULTRAPASSE OU FIQUE 
#IGUAL A DE AMONTADA


pop_tot_amon = 100000
pop_tot_mir = 45000
cont_anos = 0
while True:
    if pop_tot_mir >= pop_tot_amon:
        print(cont_anos)
        break
    else:
        pop_amon_acres = pop_tot_amon * 0.015
        pop_tot_amon = pop_tot_amon + pop_amon_acres

        pop_mir_acres = pop_tot_mir * 0.030
        pop_mir_amon = pop_tot_mir + pop_mir_acres
        cont_anos += 1
        print(cont_anos)

