from datetime import datetime


class Note:
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self, code: str, title: str, importance: str, creation_date: datetime.now, tags: []):
        self.code: str = code
        self.title: str = title
        self.importance: str = importance
        self.creation_date: datetime.now = creation_date
        self.tags: list[str] = tags

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"


class Notebook:

    def __init__(self):
        self.notes: List[Note]:[]

    def add_note(self, title: str, text: str, importance: str) -> int:
        new_code: len(self.notes) + 1
        note = Note(new_code, title, text, importance)
        self.notes.append(note)
        return new_code

    def delete_note(self, code: int):
        self.note = [note for note in self.notes if note.code != code]

    def importance_notes (self): -> list[Note]

    def notes_by_tag (self): -> list[Note]

    def tag_with_most_notes (self):

