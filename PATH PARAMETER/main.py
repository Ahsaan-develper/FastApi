from fastapi import FastAPI
from typing import Any


app =FastAPI()

dict1  = {
  1: {
        "id" : 1,
    "title" : "item 1",
   },
  2: {
        "id" : 2,
        "title" : "item 2",
   },
  3: {
       "id" : 3,
       "title" : "item 3",
   },
  4: {
         "id" : 4,
         "title" : "item 4",
   },
   5: {
        "title" : "item 5",
   }
}

list1  = [
   {
        "id" : 1,
    "title" : "item 1",
   },
  {
        "id" : 2,
        "title" : "item 2",
   },
   {
       "id" : 3,
       "title" : "item 3",
   },
   {
         "id" : 4,
         "title" : "item 4",
   },
   {
        "id" : 5,
        "title" : "item 5",
   }
]


# @app.get("/item/latest")
# def get_item ():
#     return {
#         "id": 2,
#         "title": "item 2",
#     }


# @app.get("/item/{id}")
# def get_item(id: int)  ->dict[str,Any]:
#     if id not in dict1:
#         return {
#             "error": "item not found",
#         }
#     return {
#         "id": id,
#         "title": f"item {id}",
#     }

@app.get("/item/{id}")
def get_item(id: int)  ->dict[str,Any]:
    for item in list1:
        if item["id"] == id:
            return item
        
    return {
       "error":"Id not found"
    }


# data = get_item(1)
# print(data)
