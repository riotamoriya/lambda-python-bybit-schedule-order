# Developer Guide

## 開発言語
- 使用言語: **Python**

## 開発環境
- 開発はDockerfileに記述されているコンテナ環境で行います。
- `docker-compose.yml`を使用すると開発が効率的に行えます。

## 開発ツール
- `blueprint.ipynb`: 開発のヘルパーツールとして使用します。
- `lambda_function.py`: これが最終的なエンドポイントとなります。
  - ただし、実際の開発は`main.py`で行い、ユーザーに対する直接的な入出力を除き、こちらを使用します。
  - `lambda_function.py`は`main.py`をimportして利用します。

## 開発手順
1. `blueprint.ipynb`を使用して、ローカル環境でロジックを完成させます。
2. そのロジックを`main.py`に取り込み、コンテナ環境に適用します。
3. `lambda_function.py`に取り込んだ後、curlコマンドを使用して動作確認を行います。

```
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

> **Note**: port番号は環境によって異なる可能性があります。`docker-compose.yml`には9000でリッスンしています。

## 環境変数
- `.env.local`はテンプレートとして提供されています。適切な内容を埋めて`.env`として使用してください。
- 開発環境では`.env`の内容が反映されますが、本番環境（Lambda）にデプロイする際は環境変数を直接設定する必要があります。

## コンテナ開発環境のセットアップ
1. 以下のコマンドでコンテナを立ち上げます。
   ```
   docker-compose up —build
   ```
2. 以下のコマンドでコンテナ内に入ります。
   ```
   docker-compose exec {service_name} bash
   ```
3. コンテナ内でpythonの実行を行います。

## 依存ライブラリ
- 必要なPythonライブラリは`requirements.txt`に記載してください。

---

Happy coding!
F