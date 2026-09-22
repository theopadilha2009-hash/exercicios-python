# Exercício 13 - Repetição com while
# Enunciado: Peça uma senha ao usuário e continue pedindo até que ele digite senai123.
# Ao acertar, exiba "Acesso liberado".

senha_correta = "senai123"
senha_digitada = input("Digite a senha: ")

while senha_digitada != senha_correta:
    print("Senha incorreta! Tente novamente.")
    senha_digitada = input("Digite a senha: ")

print("Acesso liberado")
