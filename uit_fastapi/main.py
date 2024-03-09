from fastapi import FastAPI, Path
from typing import Dict, Optional

app = FastAPI(title="Hello World API",
              version="0.0.1",
              servers=[
                    {
                        "url": "http://0.0.0.0:8000",  # ADD NGROK URL Here Before Creating GPT Action
                        "description": "Development Server"
                    }
              ])

# Path Parameters


@app.get("/")
def read_root():
    return 'Hello Muhammad Ali here'


students: Dict[int, Dict[str, str]] = {
    1: {
        'id': '1',
        'age': '17',
        'name': "Muhammad"
    },
    2: {
        'id': '2',
        'age': '16',
        'name': "Ayan"
    }
}


@app.get("/get-students/{student_id}")
def get_id(student_id: int):
    return students[student_id]


# Query Parameters

@app.get("/get-byname")
def get_byname(name: Optional[str] = None):
    for student_id in students:
        if students[student_id]['name'] == name:
            return students[student_id]
    return {'details': 'Not found'}
