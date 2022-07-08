import datetime
import uuid

from starlette import status

from schemas import CreateTaskSchema, GetTaskSchema, ListTasksSchema
from server import server

TODO = []

@server.get('/todo', response_model=ListTasksSchema)
def get_tasks():
    return {'tasks': TODO}

@server.post('/todo', response_model=GetTaskSchema, status_code=status.HTTP_201_CREATED)
def create_task(payload: CreateTaskSchema):
    task = payload.dict()
    task['id'] = uuid.uuid4()
    task['created'] = datetime.datetime.utcnow()
    task['priority'] = task['priority'].value
    task['status'] = task['status'].value
    TODO.append(task)