# Test Task
## Install
- python -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
## Install db
- docker compose up
- python create_tables.py
## Usage
- python main.py
- curl localhost:8000/get/records - GET
- curl -X PATCH localhost:8000/update/record/678879488 -H 'Content-Type: application/json' -d '{"name": "test1", "value": "{\"a1\": \"b1\"}"}' - PATCH
- curl -X POST localhost:8000/create/record -H 'Content-Type: application/json' -d '{"name": "test", "value": "{\"a\": \"b\"}"}' - POST
- curl -X DELETE localhost:8000/delete/record/678879488