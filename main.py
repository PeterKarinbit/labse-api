from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()
model = SentenceTransformer('sentence-transformers/LaBSE')

class TextIn(BaseModel):
    text: str

@app.post('/embed')
def embed_text(data: TextIn):
    embedding = model.encode([data.text])[0]
    return {'embedding': embedding.tolist()}
