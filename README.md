# Paper Translator Backend
## 使い方
ローカルに落とした後、docker compose up --build -d でコンテナを作成。コンテナにアタッチし、下記手順でAPIkeyを置く。
dataディレクトリを作成し、その中にconfig.yamlファイルを作成する。
config.yamlは、api_key: [自分のAPIキー]
を書く。
その後、FastAPIを起動する。
