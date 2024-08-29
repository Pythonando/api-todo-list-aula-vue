from ninja import ModelSchema
from .models import Tarefa
from typing import Optional

class TarefaSchema(ModelSchema):
    id: Optional[int] = None

    class Config:
        model = Tarefa
        model_fields = ['nome', 'data_inicial', 'data_encerramento', 'status',]