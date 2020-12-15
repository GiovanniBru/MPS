def mostraLogin():
  print("============ LOGIN ============")
  print("Digite seu login: ", end="")

def mostraSenha():
  print("============ SENHA: ============")
  print("Digite seu senha: ", end="")

def mostraLoginESenha():
  mostraLogin()
  login = input()
  mostraSenha()
  senha = input()