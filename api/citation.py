import json

from fastapi import APIRouter, HTTPException
from typing import List
from model.Citation import Citation
from repository.CitationRepository import CitationRepository

router = APIRouter(prefix="/pins", )


# Création d’un Pins
@router.post("/")
async def create_item(pin: Citation):
    item_dict = pin.dict()
    item_id = CitationRepository().create_citation(item_dict)
    return {**item_dict, "id": item_id}


# Récupère la liste des Pins
@router.get("/", response_model=List[Citation])
async def read_items():
    items = CitationRepository().list_citations()
    return [{"id": i[0], "title": i[1], "content": i[2], "source": i[3], "preference": i[4], "tags": i[5],
             "id_utilisateur": i[6]} for i in items]


# Récupère un Pins spécifique
@router.get("/{item_id}", response_model=Citation)
async def read_item(item_id: int):
    pin = CitationRepository().get_citation(item_id)
    if not pin:
        raise HTTPException(status_code=404, detail="Item not found")

    return {"id": pin[0], "title": pin[1], "content": pin[2], "source": pin[3], "preference": pin[4], "tags": pin[5],
            "id_utilisateur": pin[6]}


# Mise à jour d’un Pins
@router.put("/{item_id}", response_model=Citation)
async def update_item(item_id: int, item: Citation):
    item_dict = item.dict()
    update_data = {
        "title": item_dict["title"],
        "content": item_dict["content"],
        "source": item_dict["source"],
        "preference": item_dict["preference"],
        "tags": json.dumps(item_dict["tags"]),
        "id_utilisateur": item_dict["id_utilisateur"],
        "id": item_id,
    }
    CitationRepository().update_citation(item_id, update_data)
    return {**update_data}


# Suppression d’un Pins
@router.delete("/{item_id}")
async def delete_item(item_id: int):
    CitationRepository().delete_citation(item_id)
    return {"message": "Item deleted"}
