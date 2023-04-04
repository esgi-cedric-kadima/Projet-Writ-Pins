from pydantic import BaseModel


class Citation(BaseModel):
    title: str
    content: str
    source: str
    preference: int = 0
    tags: object = {}
    id_utilisateur: int
