#Comandos de Seleção  - ok    
#Comandos de Repetição - ok
#Vetores e Matrizes - ok
#Funções - ok
#Recursão fail
#persistencia - ok


print("Este é o futuro, SmartCity by Corrona in Garanhuns") 
def sejabemvindo(nome):
  if(nome[len(nome)-1] == 'o' or 'y'):
    return "seja bem vindo Sr."+nome
  else:
    return "seja bem vinda Sra. "+nome
#cadastro
nome = input('Digite um nome: ')

#banco de dados
file = open('cadastro', 'a+')
file.write('Usuario cadastrado no sistema:\n'+nome)
file.close

#cadastro
senha = input('Digite uma senha: ')

#banco de dados
file = open('cadastrosenha', 'a+')
file.write('Senha cadastrada no sistema:\n'+senha)
file.close
print(sejabemvindo(nome))
analise = 'segura'

#escolha opção
desejo = input('Deseja ver analise da cidade digite 1, para denuciar digite 2: ')
if desejo == '1':
  print ('está é a situação da sua cidade é: '+analise) 
  breakpoint (desejo == '1') 
else:
 print('1 para Crimes')
 print('2 para Doenças')
 print('3 para agromeração')
 casos = input('Digite o numero da sua ocorrencia ')
 file = open('casos', 'a+')
 file.write('Numero de casos:\n'+casos)
 file.close
if casos == '1':
 print('Crime selecionado!')
 print('1 para Roubo')
 print('2 para Agreção')
 print('3 para Atentado')
 crimes = input('Digite o numero do crime:')
 #Bancos de dados

 file = open('crimes', 'a+')
 file.write('Crimes ocorridos:\n'+crimes)
 file.close
 #cadastro de local

 estado = input('Digite o estado em que reside: ')
 cidade = input('Digite sua cidade: ')
 bairro = input('Digite o bairro em que você reside: ')
 rua = input('Digite a rua em que você reside: ')
 print('Agradeçemos sua contribuição ela é essencial.')

if casos == '2':
  print('1 Covid-19')
  print('2 Gripe')
  print('3 H1N1')
  doencas = input('Digite o numero da doença:')
  #Bancos de dados
  file = open('doencas', 'a+')
  file.write(doencas)
  file.close
  #cadastro de local
  estado = input('Digite o estado em que reside: ')
  cidade = input('Digite sua cidade: ')
  bairro = input('Digite o bairro em que você reside: ')
  rua = input('Digite a rua em que você reside: ')
  print('Agradeçemos sua contribuição ela é essencial.')

if casos == '3':
  print('1 Calçada')
  print('2 Rua')
  print('3 Comercio')
  localagro = input('Digite o numero do local da Agromeração: ')
  #Bancos de dados
  file = open('localagro', 'a+')
  file.write('Casos de agromeração:\n'+localagro)
  file.close
  #cadastro de local
  numero = int(input('digite um numero médio de pessoas: ')) #uso de numeros inteiros por int
  estado = input('Digite o estado em que reside: ')
  cidade = input('Digite sua cidade: ')
  bairro = input('Digite o bairro em que você reside: ')
  rua = input('Digite a rua em que você reside: ')
  print('Deseja ligar para denuncia? ')
  opçãodenuncia = input('Digite 1 para SIM e 2 para Não: ')
  if opçãodenuncia == '1':
   print('Ligue 133')
  else: print('Agradeçemos sua contribuição ela é essencial.')
  

#banco de dados local
file = open('Locais', 'a+')
file.write('O estado do usuario:'+estado)
file.write('\n A cidade do usuario:'+cidade)
file.write('\n O bairro do usuario:'+bairro)
file.write('\n A rua do usuario:'+rua)
file.seek(0)
file.close

#analise final para o usuario
print('Deseja analizar os casos na sua Cidade? ') 
print('Digite 1 para SIM E 2 para NÃO')
analisar = input('Digite um numero:')
if analisar == '1':
   if casos == '1':
     print('Ocorreu crimes')
   if casos == '2':
       print == 'Casos de Doenças'
   if casos == '3':
        print('casos de agromeração na região')


if casos != '1' or '2':
  crimes = '0'
  doencas = '0'
  localagro = '1'
if casos != '2' or '3':
   doencas = '0'
   localagro = '0'
   crimes = '1'
if casos != '1' or '3':
      crimes = '0'
      localagro = '0'
      doencas = '1'

#conversão para numeros inteiros
dados1 = (int(crimes))
dados2 = (int(doencas))
dados3 = (int(localagro))

#para mostrar dados
dadosusuario = [dados1,dados2,dados3]

print(dadosusuario)
print('crimes, aglomeração, doenças')


for i in range (1):                
 print('Agradeçemos sua contribuição, ela é essencial, FIM.')




