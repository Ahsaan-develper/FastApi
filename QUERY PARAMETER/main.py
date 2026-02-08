from fastapi import FastAPI, status , HTTPException
app = FastAPI()
from typing import Any
dict1 = {
    1: {
        "id" : 1,
        "item" : "sand"
    },
    2: {
        "id" : 2,
        "item" : "Chip"
    },
     3: {
        "id" : 3,
        "item" : "Tofu"
    },
    4: {
        "id" : 4,
        "item" : "Comp"
    },
    5: {
        "id" : 5,
        "item" : "Ship"
    }
}


@app.get("/item")
def get_item (id : int | None = None) ->dict[str , Any]:
    # if not id :
    #     return dict1[id]
    
    # if id not in dict1 :
    #     return {
    #         "error " : "Id is not found"
    #     }
    if id not in dict1 :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="The id is not found")
    return dict1[id]


@app.post("/item")
def post_item (id : int , item : str ):
    if id  > 10 :
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE , detail="The id is not accessable")
    
    new_id = max(dict1.keys()) + 1
    dict1[new_id] = {
        "id" : id,
        "item" : item
    }

