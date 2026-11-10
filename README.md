# Parte 1 - Questão 2: Tradutor inglês para francês

API em FastAPI que usa o modelo `Helsinki-NLP/opus-mt-en-fr` da HuggingFace para traduzir textos do inglês para o francês.

## Como executar

1. Crie e ative um ambiente virtual:
   ```
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
3. Rode a aplicação:
   ```
   uvicorn main:app --reload
   ```
4. Acesse http://127.0.0.1:8000/docs para testar.

Na primeira execução o modelo de tradução é baixado automaticamente.

## Exemplo de requisição

Rota `POST /traduzir` com o corpo:

```json
{"texto": "Hello, how are you today?"}
```

Resposta:

```json
{
  "original": "Hello, how are you today?",
  "traducao": "Bonjour, comment allez-vous aujourd'hui ?"
}
```

A API aceita tanto frases curtas quanto textos mais longos.

## Observação técnica sobre o carregamento do modelo

No `transformers` v5, o atalho `pipeline("translation_en_to_fr")` foi removido. Por isso, o modelo `Helsinki-NLP/opus-mt-en-fr` é carregado diretamente com `MarianTokenizer` e `MarianMTModel`.