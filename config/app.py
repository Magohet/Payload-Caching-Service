from fastapi import FastAPI

from api.router import router

app = FastAPI(debug=True, title="Caching Service")

app.include_router(router=router)
