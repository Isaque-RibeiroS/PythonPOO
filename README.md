# PythonPOO
Minhas atividades práticas do uso de Programação Orientada a Objetos, utilizando a linguagem Python.
# Descrições:
## EX01 (Produto)
### Classe Produto:
**Atributos:** nome / preco / quantidade / id_produto

**Métodos:** Init / Getter / Setter /

mostrar_produto - Mostra todos os atributos de determinado objeto

adicionar_estoque - Adiciona um valor inteiro ao atributo "quantidade" referente ao Objeto.

### Classe Main:
Utiliza de todos os métodos disponíveis na classe Produto, trazendo funcionalidades para o usuário, como:

- Olhar catálogo
- Novo produto
- Adicionar estoque
- Modificar produto

Também possui comandos para caso de erros, como:

- Uso de try/exception para prevenção de erros de entrada de valor não correspondente.
- Adicionar padrões obrigatórios para opções de cadastro de novo produto e modificação.
- Prevenção de respostas não correspondentes a instrução do menu principal.
- Não mostrar catálogo caso não haja produtos.

## EX02 (Aluno)
### Classe Pessoa (SuperClasse):
**Atributos:** nome / email / disciplina

**Métodos:** Init / Getter / Setter / 

boas_vindas - Mostra mensagem de boas vindas com nome e a disciplina correspondente

### Classe Professor (SubClasse):
**Atributos:** Herança(Pessoa) {nome, email, disciplina} / salario / carga_horaria 

**Métodos:** Init / Getter / Setter 

### Classe Aluno (SubClasse):
**Atributos:** Herança(Pessoa) {nome, email, disciplina} / matricula

**Métodos:** Init / Getter / Setter 

### Classe Main:
Utiliza a classe 'Professor' para adicionar registros fixos no sistema de professores e disciplinas disponíveis. Com isso, se consegue ao instanciar a classe 'Aluno':
- Adicionar um novo aluno a alguma das disciplinas disponíveis
- Gerar mensagem de boas-vindas para aluno e seu respectivo professor (método boas_vindas) ao completar a matrícula.

Também possui comandos para casos de erros, como:
- Uso do try/exception e condições para prevenir erros de entrada de valores inválidos.
- Prevenção de respostas não correspondentes a instrução do menu principal.
