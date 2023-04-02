FROM mysql:8.0.32

# ベースイメージの指定
FROM python:3.9

# 作業ディレクトリの指定
WORKDIR /app

# 依存パッケージのインストール
COPY requirements.txt .
RUN pip install -r requirements.txt

# アプリケーションのコピー
COPY . /app

# ポート番号の指定
EXPOSE 8000

# アプリケーションの実行
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

