import funcao

print('----------')
print('bem-vindo ao JO-KEN-PÔ')
print('Temos dois modos de jogo')
print('Jogador SOLO - você contra a máquina')
print('1v1 - você contra seu amigo!')

print('modo 1 - Jogo solo')
print('modo 2 - 1v1')
escolha = input('Qual modo vai jogar?')

if escolha == "1":
    funcao.contraPc()
elif escolha == "2":
    funcao.contraPessoa()
else:
    print('Opção não encontrada')
