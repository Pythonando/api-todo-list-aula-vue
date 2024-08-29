from ninja import NinjaAPI
from tarefas.api import tarefas_router

api = NinjaAPI()

api.add_router('/tarefas', tarefas_router)