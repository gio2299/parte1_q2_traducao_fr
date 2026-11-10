import torch
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import MarianMTModel, MarianTokenizer

app = FastAPI(title="Tradutor EN -> FR")

MODELO = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = MarianTokenizer.from_pretrained(MODELO)
modelo = MarianMTModel.from_pretrained(MODELO)


def traduzir_texto(texto: str) -> str:
    entradas = tokenizer(texto, return_tensors="pt", truncation=True, max_length=512)
    with torch.no_grad():
        saida = modelo.generate(**entradas, max_new_tokens=512)
    return tokenizer.decode(saida[0], skip_special_tokens=True)


class Entrada(BaseModel):
    texto: str


@app.post("/traduzir")
def traduzir(entrada: Entrada):
    return {"original": entrada.texto, "traducao": traduzir_texto(entrada.texto)}