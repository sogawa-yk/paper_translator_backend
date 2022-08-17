FROM python:3.9

WORKDIR /app

# コンテナ内で必要なパッケージをインストール
RUN apt install -y git
RUN cd /app
RUN git clone -b develop/1.0 https://github.com/sogawa-yk/paper_translator_backend.git
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r /app/paper_translator_backend/requirements.txt


EXPOSE 8000
# FastAPIを8000ポートで待機
#CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
