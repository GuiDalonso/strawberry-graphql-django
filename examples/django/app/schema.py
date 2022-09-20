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

from asgiref.sync import sync_to_async
from .paginator import get_paginator

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
class FruitResponse(PaginatedType):
    objects: List[Fruit] = strawberry.field(
        description="The list of fruit."
    )

@strawberry.type
class Query:
    @strawberry.field(description="Returns a paginated list of fruits.")
    async def get_fruits(self, page_size: int, page: int) -> FruitResponse:
        """
        Paginate fruits 

        query{
            getFruits(pageSize: 5, page: 7){
                objects{name}
                }
            }
        """
        from .models import Fruit as FruitModel
        #this needs some rework due to an async exception
        sliced_fruits = await sync_to_async(list)(FruitModel.objects.all().order_by('id'))
        return get_paginator(sliced_fruits, page_size, page, FruitResponse)

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
