from typing import List

import strawberry

import strawberry_django
import strawberry_django.auth as auth
from strawberry_django import mutations

from .types import (
    Color,
    ColorInput,
    ColorPartialInput,
    Fruit,
    FruitInput,
    FruitPartialInput,
    User,
    UserInput,
)

@strawberry.type
class PaginatedType():

    page: int = strawberry.field(
        description=""
    )
    page_size: int = strawberry.field(
        description=""
    )
    pages: int = strawberry.field(
        description=""
    )
    has_next: bool = strawberry.field(
        description=""
    )
    has_prev: bool = strawberry.field(
        description=""
    )

@strawberry.type
class FruitResponse:
    fruits: List[Fruit] = strawberry.field(
        description="The list of fruit."
    )
    page_meta: PaginatedType = strawberry.field(
        description="Metadata to aid in pagination."
    )



@strawberry.type
class Query:
    @strawberry.field(description="Returns a paginated list of users.")
    def get_fruits(self, offset: int, limit: int) -> FruitResponse:
        # slice the relevant user data.
        sliced_fruits = strawberry_django.field()
        # type cast the sliced data.
        sliced_fruits = (List[Fruit], sliced_fruits)
        # calculate the total items present.
        total = len(strawberry_django.field())
        # calculate the client's current page number.
        page = ((offset-1) // limit) + 1
        # calculate the total number of pages.
        pages = (total // limit)
        
        return FruitResponse(
            fruits=strawberry_django.field(),
            page_meta=PaginatedType(
                page=page,
                page_size=limit,
                pages=pages,
                has_next=False,
                has_prev=False,
            )
        )

    fruit: Fruit = strawberry_django.field()
    fruits: List[Fruit] = strawberry_django.field()

    color: Color = strawberry_django.field()
    colors: List[Color] = strawberry_django.field()


@strawberry.type
class Mutation:
    createFruit: Fruit = mutations.create(FruitInput)
    createFruits: List[Fruit] = mutations.create(FruitInput)
    updateFruits: List[Fruit] = mutations.update(FruitPartialInput)
    deleteFruits: List[Fruit] = mutations.delete()

    createColor: Color = mutations.create(ColorInput)
    createColors: List[Color] = mutations.create(ColorInput)
    updateColors: List[Color] = mutations.update(ColorPartialInput)
    deleteColors: List[Color] = mutations.delete()

    register: User = auth.register(UserInput)


schema = strawberry.Schema(query=Query, mutation=Mutation)
