from fastapi import FastAPI
from app.routers import note_routes
from app.models import Base
from app.database import engine

app = FastAPI(title="FastAPI + Alembic")

# �������� ��������
app.include_router(note_routes.router)

# ������� ������� ��� ������ (�������������, ����� �������� �������� �� Alembic)
@app.on_event("startup")
async def startup():
    # ������� ���, ���� ����������� alembic:
    # await conn.run_sync(Base.metadata.create_all)
    pass

