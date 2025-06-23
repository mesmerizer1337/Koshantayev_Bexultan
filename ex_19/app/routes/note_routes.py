from fastapi import APIRouter, HTTPException
from app.schemas import NoteOut, NoteCreate

router = APIRouter()

fake_notes_db = []

@router.get(
    "/notes",
    summary="�������� ��� �������",
    description="���������� ������ ���� ������� (�� ��������� ����)",
    response_model=list[NoteOut]
)
def get_notes():
    return fake_notes_db

@router.post(
    "/notes",
    summary="������� ����� �������",
    description="������� ������� � ���������� �",
    response_model=NoteOut,
    responses={
        201: {
            "description": "������� ������� �������",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1,
                        "title": "����� �������",
                        "content": "������ �����������"
                    }
                }
            }
        }
    }
)
def create_note(note: NoteCreate):
    new_note = {"id": len(fake_notes_db) + 1, **note.dict()}
    fake_notes_db.append(new_note)
    return new_note
