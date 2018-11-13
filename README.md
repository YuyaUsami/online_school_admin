# 環境
||version|
|:--|:--|
|Python|3.7.1|
|Django|2.1.2|

# annocondaのインストールしてからの手順
```
# pythonの実行環境を作成する
python -n py37

# 実行環境を切り替える
source activate py37

# djangoのインストール
conda install django
```


# 初期設定
```
# migrationファイルを作成
python manage.py makemigrations employee

# migrate
python manage.py migrate employee

```

# superuserの作成('/admin'でデータの追加 or 削除が可能になる)
```
python manage.py createsuperuser
```

# 備考
## 使用したサイト
https://hackerthemes.com/bootstrap-cheatsheet/