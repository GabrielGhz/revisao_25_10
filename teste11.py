from datetime import datetime

hora_atual = datetime.now()
h = hora_atual.strftime ('%H')
hora_completa = hora_atual.strftime ("%H:%M:%S")

dicio={
	'manha' : 'Bom Dia!',
	'tarde' : 'Boa Tarde!',
	'noite' : 'Boa Noite!',
	'dormi' : 'Está na hora de dormi!'

}

if int (h) >= 6 and int (h) <= 12:
	print ('A hora agora é: ', hora_completa, 'tenha um ' ,dicio ['manha'])
elif int (h) >= 13 and int (h) <= 17:
	print ('A hora agora é: ', hora_completa, 'tenha uma', dicio ['tarde'])
elif int (h) >= 18 and int (h) <=23:
	print ('a hora agora é: ', hora_completa, 'tenha uma', dicio ['noite'])
else:
	print ('A hora agora é: ', hora_completa, dicio['dormi'])
