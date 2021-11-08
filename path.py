from fastapi import FastAPI,Path
app = FastAPI()
items={2:{
    'pen':1,
    'book':2,
    'class':3,
    'pam':4
}
}
@app.get("/get-items/{item_id}")
async def read_item(item_id: int=Path(None,description="The ID of the items you want to view: ",gt=0)):
     return items[item_id]


# @app.get("/get-items/{item_name}")
# async def write_them(item_name: str):
#     return items[item_name]

@app.get("/get-items-by-name")
def get_items(name: str):
    for item_id in items:
        if items[item_id]["name"]==name:
            return items[item_id]
    return {"Data Not Found"}
