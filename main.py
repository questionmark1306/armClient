from fastapi import FastAPI,Cookie
import uvicorn
from typing_extensions import Annotated
from typing import Union





app = FastAPI()

# http://127.0.0.1:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}


# http://127.0.0.1:8000/items/1
# @app.get("/items/{item_id}/")
# async def read_item(item_id):
#     return {"item_id": item_id} # item_id自定义


# @app.get("/items/{item_id}/{user_id}/")
# async def read_item(item_id, user_id):
#     return {"item_id": item_id, "user_id": user_id}


# http://127.0.0.1:8000/items/?skip=0&limit=2
# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]


# http://127.0.0.1:8000/items/1?q=admin
# from typing import Union
# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# http://127.0.0.1:8000/users/1/items/2
# or 
# http://127.0.0.1:8000/users/1/items/2?q=query&short=true
# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
#         user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
# ):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item



# from pydantic import BaseModel
# from typing import Union
# class Item(BaseModel):
#     name: str = '小明'
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
# @app.post("/items/")
# async def create_item(item: Item):
#     print(item.name)
#     return item


@app.get("/items/")
async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id": ads_id}


if __name__ == '__main__':
    uvicorn.run(app='main:app',  host="192.168.2.200", port=8100, reload=True)