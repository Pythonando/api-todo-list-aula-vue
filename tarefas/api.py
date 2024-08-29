from ninja import Router
from .schema import TarefaSchema
from .models import Tarefa
from http import HTTPStatus
from django.shortcuts import get_object_or_404

tarefas_router = Router()

@tarefas_router.post('/', response={HTTPStatus.CREATED: TarefaSchema, HTTPStatus.INTERNAL_SERVER_ERROR: dict})
def tarefa(request, tarefa_obj: TarefaSchema):
    try:
        task = Tarefa(**tarefa_obj.dict())
        task.save()
    except:
        return 500, {'status': 'Erro interno do sistema'}
    return HTTPStatus.CREATED, task

@tarefas_router.get('/', response=list[TarefaSchema])
def list_tarefa(request):
    return Tarefa.objects.all()

@tarefas_router.patch('/{id}', response=TarefaSchema)
def check_tarefa(request, id: int):
    task = get_object_or_404(Tarefa, id=id)
    task.status = not task.status
    task.save()
    return task