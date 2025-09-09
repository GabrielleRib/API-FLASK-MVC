from flask import render_template, request, redirect, url_for
from models import db
from models.task import Task
from models.user import User

class TaskController:

    @staticmethod
    def list_tasks():
        tasks = Task.query.all()
        # TODO buscar todas as tarefas do banco de dados

        tasks = None 
        return render_template("tasks.html", tasks=tasks)

    @staticmethod
    def create_task():
        
        if request.method == "POST":
            title = request.form["title"]
            description = request.form["description"]
            user_id = request.form["user_id"]
            # TODO capturar dados do formulário (title, description, user_id)

            new_task = Task(title=title, description=description, user_id=user_id)
            # TODO criar um novo objeto Task com os dados capturados

            db.session.add(new_task)
            db.session.commit()
            # TODO adicionar no db.session e dar commit
            pass

            return redirect(url_for("list_tasks"))
        
        #?users = User.query.all()
        # TODO buscar todos os usuários para exibir no <select> do formulário
        users = None
        return render_template("create_task.html", users=users)
    
    @staticmethod
    def update_task_status(task_id):
        task_to_update = Task.query.get(id)
        # TODO buscar a tarefa pelo id

        if task_to_update:
            task_to_update.status =="Pendente":
                task_to_update.status = "Concluído"
        else:
            task_to_update.status = "Pendente"
            db.session.commit
        # TODO: se existir, alternar status entre "Pendente" e "Concluído" e dar commit na alteração
        

        return redirect(url_for("list_tasks"))

    @staticmethod
    def delete_task(task_id):
        task_to_delete = Task.query.get(id)
        # TODO buscar a tarefa pelo id

        if task_to_delete:
            db.session.delete(task_to_delete)
            db.session.commit()
        else:
            return "Tarefa não encontrada",404
        # TODO: se ela existir, remover do db.session e dar commit
        
    
        return redirect(url_for("list_tasks"))
