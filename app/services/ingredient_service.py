from sqlalchemy.orm import Session
from app.models.ingredient import Ingredient


def get_all(db: Session):
    return db.query(Ingredient).all()


def get_by_id(db: Session, id: int):
    return db.query(Ingredient).filter(Ingredient.id == id).first()


def create(db: Session, data):
    item = Ingredient(**data.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def update(db: Session, id: int, data):
    item = get_by_id(db, id)

    if not item:
        return None

    for key, value in data.dict().items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)
    return item


def delete(db: Session, id: int):
    item = get_by_id(db, id)

    if not item:
        return False

    db.delete(item)
    db.commit()
    return True