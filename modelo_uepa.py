https://github.com/Marcelosantos-c/modelo_uepa.py.git
class MembroUEPA:
    def __init__(self, nome: str, matricula: str, email: str):
        self.nome = nome
        self.matricula = matricula
        self.email = email

    def apresentar(self):
        print(f"Sou um membro da UEPA. Nome: {self.nome}, Matrícula: {self.matricula}, Email: {self.email}")


class Aluno(MembroUEPA):
    def __init__(self, nome: str, matricula: str, email: str, curso: str):
        super().__init__(nome, matricula, email)
        self.curso = curso

    def apresentar(self):
        print(f"Sou o aluno {self.nome}, matrícula {self.matricula}, do curso de {self.curso}. Email: {self.email}")

    def verificar_notas(self, notas: list[float]):
        if not notas:
            print("Nenhuma nota registrada.")
            return

        media = sum(notas) / len(notas)
        print(f"A média das notas do aluno {self.nome} é {media:.2f}")
        if media >= 7:
            print("Situação: Aprovado ")
        else:
            print("Situação: Reprovado ")


class Professor(MembroUEPA):
    def __init__(self, nome: str, matricula: str, email: str, departamento: str):
        super().__init__(nome, matricula, email)
        self.departamento = departamento

    def apresentar(self):
        print(f"Sou o professor {self.nome}, matrícula {self.matricula}, do departamento de {self.departamento}. Email: {self.email}")

    def lancar_frequencia(self, alunos: dict[str, int]):
        print(f"Lançando frequência do professor {self.nome}:")
        for aluno, presencas in alunos.items():
            print(f" - {aluno}: {presencas}% de presença")

if __name__ == "__main__":
    aluno1 = Aluno("Maria Silva", "2023001", "maria@aluno.uepa.br", "Engenharia")
    professor1 = Professor("Carlos Souza", "P1234", "carlos@uepa.br", "Exatas")

    aluno1.apresentar()
    professor1.apresentar()

    aluno1.verificar_notas([8.0, 7.5, 6.0])