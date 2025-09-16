from datetime import date
atual = date.today().year
ano = (int(input('ano de nascimento?  ')))
idade = atual - ano
print(f'quem nasceu em {ano} tem {idade} anos em {atual}.')
if idade == 18:
    print('você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'você ainda não tem 18 anos. Ainda faltam {saldo} anos para o alistamento.')
    ano = atual + saldo
    print(f'seu alistamento sera em {ano}')
elif idade > 18:
    saldo = idade - 18
    print(f'você ja devia ter se alistado a {saldo} anos')
    ano = atual - saldo
    print(f'seu alistamento foi em {ano}')