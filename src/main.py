from fastapi import FastAPI
from src.deepl_request import translate
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

class SendText(BaseModel):
    text: str
    uri: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/translate/')
def translate_text(request: SendText):
    """投げたテキストを翻訳して返す。

    Args:
        text (str, optional): 英語の文章. Defaults to ''.
        uri (str, optional): PDFのURL

    Returns:
        _type_: 結果が入った辞書
    """
    if '\n' in request.text:
        request.text = request.text.replace('\n', '')
    result = translate(request.text, request.uri)
    # result = result.replace('。', '.')
    # result = result.replace('、', ',')
    return {'text': result}
