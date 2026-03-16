from fastapi import FastAPI
from app.api.v1 import routes

app = FastAPI(title="RBAC")
app.include_router(routes.router)
