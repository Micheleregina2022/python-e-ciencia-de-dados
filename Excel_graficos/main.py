import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_excel("dadosMulher.xlsx")
df2 = pd.read_excel("dadosHomem.xlsx")

print(df1)
print(df2)
#ler as duas separadamente

plt.plot(df1["Idade"])
plt.plot(df2["Idade"])
plt.figlegend("MH")
plt.show()
#gráfico de linha

plt.hist(df1["Idade"], bins= 20)
plt.hist(df2["Idade"], bins= 20)
plt.figlegend("MH")
plt.show()
#gráfico em barras

plt.pie(df1["Idade"], labels=df1["Nome"], autopct="%1.0f%%")
plt.show()
plt.pie(df2["Idade"], labels=df2["Nome"], autopct="%1.0f%%")
plt.show()
#gráfico pizza; porcentagem de pessoas com determinada idade, separado por sexo

df3 = pd.concat([df1 + df2])
plt.pie(df3["Idade"], autopct="%1.0f%%")
plt.show()
#porcentagem da soma das duas listas.