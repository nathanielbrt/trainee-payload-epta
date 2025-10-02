# comando import para importar as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt


# comandos para importar e printar tabela com informações do foguete
df = pd.read_excel("Dados.xlsx")
print(df)


# criando uma tabela secundária com as principais informações que serão usadas no cálculo estatístico
df_main = df[['Altitude (m)', 'Verticle Velocity (mph)',
              'Ground velocity (mph)', 'Acceleretion (g/s)']]
print(df_main)


# usando a função .mean() para calcular a média das colunas
media = df_main.mean()
print("\nMédia:\n", media)


# usando a função .median() para calcular a mediana das colunas
mediana = df_main.median()
print("\nMediana:\n", mediana)


# usando a função .max() é possível calcular o valor máximo de cada coluna selecionada
vmax = df_main.max()
print("\nValores máximos:\n", vmax)


# usando a função .min() é possível calcular o valor mínimo de cada coluna selecionada
vmin = df_main.min()
print("\nValores mínimos:\n", vmin)


# criar gráficos com a biblioteca matplotlib, a função .plot(p1, p2) usa 2 parametros que são os eixos x e y respectivamente; .show apresenta e .title, .label são legendas do gráfico

# gráfico da aceleração em função do tempo:
acc = df_main[['Acceleretion (g/s)']]
tempo = df[['Time (s)']]
plt.plot(tempo, acc)
plt.title('Aceleração(g/s) x Tempo(s)')
plt.xlabel('Tempo (s)')
plt.ylabel('Aceleração(g/s)')
plt.show()


# gráfico da altitude em função do distância horizontal percorrida:
disth = df[['Ground Distance Traveled (ft)']]
altura = df_main[['Altitude (m)']]
plt.plot(disth, altura)
plt.title('Altitude (m) x Distância horizontal (ft)')
plt.xlabel('Distância horizontal (ft)')
plt.ylabel('Altiutde (m)')
plt.show()

# gráfico da altitude em função do tempo:
plt.plot(tempo, altura)
plt.title('Altitude (m) x Tempo (s)')
plt.xlabel('Tempo (s)')
plt.ylabel('Altitude (m)')
plt.show()


# gráfico da distância horizontal percorrida em função do tempo:
plt.plot(tempo, disth)
plt.title('Distância horizontal(ft) x Tempo (s)')
plt.xlabel('Tempo (s)')
plt.ylabel('Distância horizontal(ft)')
plt.show()

# gráfico da velocidade vertical em função do tempo:
vv = df_main[['Verticle Velocity (mph)']]
plt.plot(tempo, vv)
plt.title('Velocidade vertical (mph) x Tempo (s)')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade vertical (mph)')
plt.show()

# gráfico da velocidade horizontal em função do tempo:
vh = df_main[['Ground velocity (mph)']]
plt.plot(tempo, vh)
plt.title('Velocidade horizontal (mph) x Tempo (s)')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade horizontal (mph)')
plt.show()
