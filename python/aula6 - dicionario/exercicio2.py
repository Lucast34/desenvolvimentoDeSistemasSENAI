"""
2. Agenda de Contatos
Crie um programa para armazenar números de telefone. 
O usuário deve poder adicionar novos contatos 
(nome como chave e número como valor). Depois, 
o programa deve exibir todos os contatos cadastrados. 
Obs: O salvamento deverá parar apenas quando o usuário 
digitar "finalizar"
"""

agenda = {}

while True:
    nome = input('📕 Digite o nome do usuário: ')

    if nome == 'finalizar':
        break

    telefone = input(f'📞 Digite o telefone do usuário {nome}: ')
    print('***********')

    agenda.update({
        nome : telefone
    })

print('--------AGENDA ELETRONICA--------')  
for contatinho in agenda.items():
    print(f'📩 Nome :{contatinho[0]} - 📞 {contatinho[1]}')
