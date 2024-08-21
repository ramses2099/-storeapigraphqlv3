import strawberry
from database import Session
from models import Category
from .types import CategoryType

@strawberry.type
class Query:
    @strawberry.field
    def get_caterories(self) -> list[CategoryType]:
        with Session() as session:
            return session.query(Category).all()

    @strawberry.field
    def get_category_by_id(self, id: int) -> CategoryType:
        with Session() as session:
            return session.query(Category).filter(Category.id == id).first()

