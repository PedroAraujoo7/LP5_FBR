nome = 'Jeova'
sobrenome = "Jirê"
idade = 3000
altura = 3.78
adulto = False

# Escrevendo no console.
print(nome)
print(sobrenome)
print(idade)
print(altura)
print(adulto)

# concatenando informações
print('Ele é o senhor',nome)
print('Seu nome é',nome,sobrenome)
print('Sua idade é {} e sua altura é {}'.format(idade,altura))

# Maneira moderna(baiana) de concatenar
print(f'Seu nome é {nome} e ele tem {idade} de idade')

# Verificando o tipo da variavel
print(type(nome))
print(type(sobrenome))
print(type(idade))
print(type(altura))
print(type(adulto))

# Expressões numericas

numero1 = 10
numero2 = 5
soma = numero1 + numero2
sub = numero1 - numero2
mult = numero1 * numero2
div = numero1 / numero2
print(f'A soma é {soma}')
print(f'A sub é {sub}')
print(f'A mult é {mult}')
print(f'A div é {div}')

expressao = numero1 + (numero2*numero1) + numero1
print(expressao)

# outras operações
potencia = numero1**2
print(potencia)
div_exata = numero1//4
print(div_exata)