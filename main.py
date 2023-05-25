from funcoes import limparTela, aguardar
while True:
    limparTela()
    print("(0) Sair")
    print("(1) Incluir Alunos")
    print("(2) Mostrar Lista")
    print("(3) Deletar todos os registros")
    opcao = input()
    if opcao == "0":
        break
    elif opcao == "1":
        nome = input("Nome: ")
        email = input("E-mail:")
        arquivo = open("bd.atitus","a") #w  write # r read # a append
        arquivo.write(nome+" "+email+"\n")
        arquivo.close()
        print("Dados Salvos")
        aguardar(5)
    elif opcao == "2":
        try:
            arquivo = open("bd.atitus","r")
            dados = arquivo.read()
            print(dados)
            arquivo.close()
            aguardar(5)
        except:
            print("Banco de Dados não localizado!")
            print("Estamos criando um para vc!")
            arquivo = open("bd.atitus","w")
            arquivo.close()
            aguardar(1)
    else:
        print("Opção Inválida!")
        aguardar(2)
