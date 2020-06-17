# Visualização de dados em Python

import matplotlib.pyplot as plt


# Gráfico Simples

# x = [5] 
# y = [2]
# x = [1, 2, 4, 6, 8] 
# y = [2, 2, 5, 4, 2]

# #titulo = ['Gráfico de Linha', 'Gráfico de Barras']
# titulo = {'linha':'Gráfico de Linha', 'barra':'Gráfico de Barras'}
# eixox = 'Eixo X'
# eixoy = 'Eixo Y'

# # Legendas
# plt.xlabel("Eixo X")
# plt.ylabel("Eixo Y")

# # Gráfico de linha
# # plt.title(titulo['linha'])
# # plt.plot(x, y)

# # Gráfico de Barras
# plt.title(titulo['barra'])
# plt.bar(x,y)

# plt.show()


# #Gráficos comparativos

# x1 = [1, 3, 5, 7, 9] 
# y1 = [2, 2, 5, 4, 2]

# x2 = [2, 4, 6, 8, 10] 
# y2 = [5, 4, 7, 3, 8]

# titulo = 'Gráfico de Barras Comparativo'
# eixox = 'Eixo X'
# eixoy = 'Eixo Y'

# # Legendas
# plt.title(titulo)
# plt.xlabel(eixox)
# plt.ylabel(eixoy)

# plt.bar(x1, y1, label = 'Grupo 1', color='#0000ff')
# plt.bar(x2, y2, label = 'Grupo 2', color='#00ff00')
# plt.legend()

# plt.show()

# Gráfico de Pontos

#Gráficos comparativos

x1 = [1, 3, 5, 7, 9] 
y1 = [2, 2, 5, 4, 2]
z =  [20, 30, 50, 70, 100] # é o tamanho dos pontos no gráfico

titulo = 'Scatterplot: Gráfico de Dispersão'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

# Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x1, y1, label = 'Meus pontos', color='r', marker = 'h', s=z)
plt.plot(x1, y1, color = '#002300', linestyle = '--', linewidth = 4)
plt.legend()
# plt.show()

# Salvando a figura
#plt.savefig('figura1.png')
#plt.savefig('figura1.png', dpi=300)
plt.savefig('figura1a.png', dpi=1200)
#plt.savefig('figura1.pdf')

# CORES (color)
# 'b' blue
# 'g' green
# 'r' red
# 'c' cyan
# 'm' magenta
# 'y' yellow
# 'k' black
# 'w' white

# Marcadores (marker)
# '.' point marker
# ',' pixel marker
# 'o' circle marker
# 'v' triangle_down marker
# '^' triangle_up marker
# '<' triangle_left marker
# '>' triangle_right marker
# '1' tri_down marker
# '2' tri_up marker
# '3' tri_left marker
# '4' tri_right marker
# 's' square marker
# 'p' pentagon marker
# '*' star marker
# 'h' hexagon1 marker
# 'H' hexagon2 marker
# '+' plus marker
# 'x' x marker
# 'D' diamond marker
# 'd' thin_diamond marker
# '|' vline marker
# '_' hline marker


# Tipos de linha (linestyle)
# '-' solid line style
# '--' dashed line style
# '-.' dash-dot line style
# ':' dotted line style