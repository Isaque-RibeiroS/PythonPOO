class Pessoa:
    def __init__(self, nome, email, disciplina):
        self.nome = nome
        self.email = email
        self.disciplina = disciplina

    def get_nome(self):
        return self.nome
    def set_nome(self, nome):
        self.nome = nome

    def get_email(self):
        return self.email
    def set_email(self, email):
        if '@' in email:
            self.email = email
        else:
            print("\033[31mEndereço de email inválido\033[0m")

    def get_disciplina(self):
        return self.disciplina
    def set_disciplina(self, disciplina):
        self.disciplina = disciplina

    def boas_vindas(self):
        print("\033[32mBem-vindo a disciplina de {}, {}!\033[0m".format(self.disciplina, self.nome))
        return

# Professor

class Professor(Pessoa):
    def __init__(self, nome, email, salario, disciplina, carga_horaria):

        super().__init__(nome, email, disciplina)
        self.salario = salario
        self.carga_horaria = carga_horaria

    def get_salario(self):
        return self.salario
    def set_salario(self, salario):
        if salario > 0:
            self.salario = salario
        else:
            print("\033[31mO salário deve ser superior a 0\033[0m")
    def get_carga_horaria(self):
        return self.carga_horaria
    def set_carga_horaria(self, carga_horaria):
        self.carga_horaria = carga_horaria

# Aluno

class Aluno(Pessoa):
    def __init__(self, nome, email, disciplina, matricula):
        super().__init__(nome, email, disciplina)
        self.matricula = matricula

    def get_matricula(self):
        return self.matricula
    def set_matricula(self, matricula):
        self.matricula = matricula

    def mostrar_dados(self):
        print("Aluno(a): {}".format(self.nome))
        print("E-mail: {}".format(self.email))
        print("Disciplina: {}".format(self.disciplina))
        print("Matricula: {}".format(self.matricula))
        return