from models import db

class Task(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    #user_id = 
    status = db.Column(db.String(100), default="Pendente")
    #user = User
    # TODO: Define os campos e o relacionamento da tabela Task
    # - id: chave primária da tarefa (OK)
    # - title: título da tarefa (obrigatório) (OK)
    # - description: descrição detalhada da tarefa (obrigatório)(OK)
    # - user_id: chave estrangeira que conecta a tarefa a um usuário (não nulo)
    # - status: indica o estado da tarefa, padrão "Pendente"(OK)
    # - user: relacionamento com a classe User, usando back_populates="tasks" para criar o vínculo bidirecional

    def __repr__(self):
        return f"<Task {self.title} - {self.status}>"
