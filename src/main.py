from fastapi import FastAPI
from src.deepl_request import translate

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/translate/')
def translate_text(text: str=''):
    """投げたテキストを翻訳して返す。

    Args:
        text (str, optional): 英語の文章. Defaults to ''.

    Returns:
        _type_: 結果が入った辞書
    """
    if '\n' in text:
        text = text.replace('\n', '')
    result = translate(text)
    return {'text': result}
