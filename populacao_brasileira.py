# Crescimento da População Brasileira 1980-2016
# Datasus

import matplotlib.pyplot as plt 

dados = open("original.csv").readlines()

x = []
y = []


for i in range(len(dados)):
	if i != 0:
		#linha = dados[i]
		linha = dados[i].split(';')
		x.append(int(linha[0]))
		y.append(int(linha[1]))
		#print(linha)


#print(y)
#print(y)

plt.bar(x, y, color='#e4e4e4')
plt.plot(x, y, color='#000033', linestyle='--')
plt.title('Crescimento da População Brasileira 1980-2016')
plt.xlabel('Ano')
plt.ylabel('População X 100.000.000')
#plt.show()
plt.savefig('Populacao_brasileira.png', dpi=300)
plt.savefig('Populacao_brasileira.pdf')


