from pydantic import BaseModel, Field

class NoteSchema(BaseModel):
    title: str = Field(..., description="��������� �������", example="�������")
    content: str = Field(..., description="���������� �������", example="������ ���� � ������")
