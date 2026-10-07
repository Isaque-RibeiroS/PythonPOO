from pessoa import Professor, Aluno

espacamento = '\033[33m=\033[m'*60
validar_entrada = False

# Professores da Instituição

professor_logica_programacao = Professor('Lucas Carvalho','lucascarvalho@gmail.com',6000,
                                         'Lógica de Programação',30)
professor_interfaces = Professor('Roberto da Silva','robertosilva@gmail.com',7500,
                                 'Desenvolvimento de Interfaces',40)
professor_banco_dados = Professor('Gilberto Ferreira','gilbertoferreira@gmail.com',6000,
                                  'Banco de Dados',30)

print(espacamento)
print(" "*25,"\033[1mAluno\033[m")
print(espacamento)
print("\033[1mDisciplinas disponíveis:\033[m \n> (1) {}\n> (2) {}\n> (3) {}".format(professor_logica_programacao.get_disciplina(),
                                               professor_interfaces.get_disciplina(),professor_banco_dados.get_disciplina()))
print(espacamento)

nome = input('Nome do Aluno(a): \n> ')
print(espacamento)

email = input('E-mail: \n> ')
print(espacamento)

# Erro email

while '@' not in email:
    print("\033[31mEndereço de email inválido\033[0m")
    email = input('E-mail do Aluno(a): \n> ')
    print(espacamento)

disciplina = (input('N° da Disciplina: \n> '))
print(espacamento)

# Erro disciplina

while validar_entrada == False:

    try:
        disciplina = int(disciplina)
    except ValueError:
        print("\033[31mDigite o apenas o N° da disciplina disponível.\033[m")
        disciplina = (input('N° da Disciplina: \n> '))
        print(espacamento)
        continue

    if int(disciplina) == 1 or int(disciplina) == 2 or int(disciplina) == 3:
        validar_entrada = True
    else:
        print("\033[31mDigite o apenas o N° da disciplina disponível.\033[m")
        disciplina = (input('N° da Disciplina: \n> '))
        print(espacamento)
        continue

# Caso disciplina de Lógica de Programação

if int(disciplina) == 1:

    aluno = Aluno(nome,email,'Lógica de Programação','ALP3011')
    aluno.mostrar_dados()

    print(espacamento)

    print("\033[1mBoas-vindas para nosso novo aluno(a)! \033[m")
    aluno.boas_vindas()
    print("\033[1mE boas-vindas para seu professor! \033[m")
    professor_logica_programacao.boas_vindas()
    print(espacamento)

# Caso disciplina de Desenvolvimento de Interfaces

if int(disciplina) == 2:

    aluno = Aluno(nome,email,'Desenvolvimento de Interfaces','ADI4011')
    aluno.mostrar_dados()

    print(espacamento)

    print("\033[1mBoas-vindas para nosso novo aluno(a)! \033[m")
    aluno.boas_vindas()
    print("\033[1mE boas-vindas para seu professor! \033[m")
    professor_interfaces.boas_vindas()
    print(espacamento)

# Caso disciplina de Banco de Dados

if int(disciplina) == 3:

    aluno = Aluno(nome,email,'Banco de Dados','ABC3011')
    aluno.mostrar_dados()

    print(espacamento)

    print("\033[1mBoas-vindas para nosso novo aluno(a)! \033[m")
    aluno.boas_vindas()
    print("\033[1mE boas-vindas para seu professor! \033[m")
    professor_banco_dados.boas_vindas()
    print(espacamento)