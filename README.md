# Payload Caching Service

A simple FastAPI-based microservice that accepts two lists of strings, transforms them using an external service (simulated), interleaves the results, and stores them in PostgreSQL.  
Previously processed inputs are cached, so the service does not recompute the same data with external service.

---

## Features

- **POST /payload**  
  Accepts two lists of strings (`list_1`, `list_2`), transforms them (without sorting), interleaves results, and stores them in DB.  
  Returns a unique payload ID.  
  If the same lists were already processed, the cached result is returned.

- **GET /payload/{id}**
  Returns the transformed and interleaved result by payload ID.  
  If not found, returns `404`.

- **Caching**  
  Inputs are cached by content (`list_1`, `list_2`), avoiding redundant processing.

---

## API Examples

### Create Payload
**Request**
```http
POST http://localhost:8000/api/payload/
Content-Type: application/json

{
  "list_1": ["1", "2"],
  "list_2": ["3", "4"]
}
````

**Response**

```json
{
  "result": "['1', '3', '2', '4']",
  "id": "b4a9a1f2-87aa-4c22-9d88-47bead44e8cf"
}
```

---

### Get Payload

**Request**

```http
GET http://localhost:8000/api/payload/b4a9a1f2-87aa-4c22-9d88-47bead44e8cf
```

**Response**

```json
{
    "id": "b4a9a1f2-87aa-4c22-9d88-47bead44e8cf",
    "list_1": [
        "1",
        "2"
    ],
    "list_2": [
        "3",
        "4"
    ],
    "result": "['1', '3', '2', '4']",
    "created_at": "2025-08-20T18:37:41.615994Z",
    "updated_at": null
}
```

---

## Running with Docker
 
```bash
# configuring env variables
cp .env.example .env
nano .env

"
DEBUG             #debug mode on (BOOLEAN)
APP_HOST          #application host 
APP_PORT          #application port
APP_WORKERS       #number of uvicorn workers
POSTGRES_USER     #DB user
POSTGRES_PASSWORD #DB password
POSTGRES_DB       #DB name
POSTGRES_DSN      #DB DSN
"

# build image && run container
docker compose -f docker-compose.yml up --build -d
```

You can now access the service at [http://localhost:8000/docs](http://localhost:8000/docs)
