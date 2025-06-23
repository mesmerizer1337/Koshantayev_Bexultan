from pydantic import BaseModel, Field

class NoteBase(BaseModel):
    title: str = Field(..., description="��������� �������", example="������ �������")
    content: str = Field(..., description="���������� �������", example="������, ����, ���")

class NoteCreate(NoteBase):
    pass

class NoteOut(NoteBase):
    id: int = Field(..., description="���������� ������������� �������", example=1)

    class Config:
        orm_mode = True
