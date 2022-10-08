from functools import total_ordering
import pandas as pd
import win32com.client as win32
#importando a tabela para o pandas
tabela_vendas = pd.read_excel('./Vendas.xlsx')
#vizualizar a tabela de vendas
pd.set_option('display.max_columns', None)
#print(tabela_vendas)
#Faturamento por loja
faturamento = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
print(faturamento)
print('-' * 50)
#Quantidade de produtos vendidos por loja
totalLoja = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(totalLoja)
print('-' * 50)
#Ticket Médio por produto em cada loja
ticketMedio = (faturamento['Valor Final'] / totalLoja['Quantidade']).to_frame()
ticketMedio = ticketMedio.rename(columns={0: 'Ticket Médio'})
print(ticketMedio)

#Enviar relatório por email
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'contatoalex@live.com'
mail.Subject = 'Aula Python - Relatório de Vendas por Loja'
mail.HTMLBody = f'''
Prezados,
<p>Segue relatorio de vendas por loja,</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{totalLoja.to_html()}

<p>Ticket Médio dos produtos por loja:</p>
{ticketMedio.to_html(formatters={'Ticket Médio':'R${:,.2f}'.format})}
<p>Qualquer dúvida estou à disposição</p>
<p>Att</p> <p>Alex</p>
'''
mail.Display()