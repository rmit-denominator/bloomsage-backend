import uvicorn
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from typing import Annotated
from dotenv import dotenv_values
from fastapi.staticfiles import StaticFiles
# from machine_learning.model_pipeline_template import predict_step

import os, sys
module_path = os.path.abspath(os.path.join('.'))
if module_path not in sys.path:
    sys.path.append(module_path)

import uvicorn

from machine_learning.pipeline import classify, recommend

config = dotenv_values(".env")

app = FastAPI()

app.mount("/images", StaticFiles(directory="data/recommender-database"), name="images")

class Data(BaseModel):
    item: str


@app.get("/data", response_model=Data)
async def get_data() -> Data:
    """
    Get Data
    """
    return Data(item="devops")


@app.get("/")
async def main():
    content = """
        <body>
            <h1>Hello World from FastAPI</h1>
        </body>
    """
    return HTMLResponse(content=content)

@app.post("/upload/")
async def upload_image(image: UploadFile):
    root_dir = os.path.dirname(os.path.realpath(__file__))
    
    image_binary, species = classify(
        image,
        os.path.join(root_dir, "models/clf-cnn")
    )
    recommendations = recommend(
        image, 10,
        os.path.join(root_dir, "data/recommender-database.csv"),
        os.path.join(root_dir, "models/clf-cnn"),
        os.path.join(root_dir, "models/fe-cnn"),
        os.path.join(root_dir, "models/clu-kmeans")
    )
    
    return {
        "species": species,
        "recommendations": recommendations
    }

@app.get("/items/{item_id}")
async def read_item(item_id: str) -> dict[str, str]:
    """
    Get an Item
    """
    return {"item_id": item_id}


@app.post("/uploadfiles/")
async def create_upload_files(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    image_paths = []
    for file in files:
        contents = await file.read()
        # Save the file to images folder
        with open(f"images/{file.filename}", "wb") as f:
            f.write(contents)

        image_paths.append(f"./images/{file.filename}")

    # Use os.listdir to get all files in the directory
    # files = os.listdir("./images/tmp")

    # print(image_paths)
    # preds = predict_step(image_paths)

    # return {"predictions": [pred for pred in preds]}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )
