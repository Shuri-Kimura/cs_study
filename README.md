# シフト作成ツール

### Video Demo: <https://youtu.be/IqJsYm_kp3o>
#### Description: 下に記述.

## Requirement:

```
・cs50
・flask
・Werkzeug
・sqlite3
・pandas
```



## Usage:

必要なモジュールをインストールした後

```
flask run
```

にて実行を行ったら

![login](C:\Users\81808\OneDrive\デスクトップ\python\make_shift\images\login.png)

Registerボタンから、新しい従業員の登録を行います。また従業員を消す場合はDeleteボタンから名前を入力し消すことが出来ます。（デモとして現在、users.dbには"m","T","k"が入っています。必要に応じて消してください。

![home](C:\Users\81808\OneDrive\デスクトップ\python\make_shift\images\home.png)

その後、homeページに飛ぶのでシフト登録ボタンにて、テンプレートのダウンロードを行い出れるシフトのセルに何か文字を入力します（１など）

![shift](C:\Users\81808\OneDrive\デスクトップ\python\make_shift\images\shift.png)

そのエクセルファイルをシフトアップロードボタンより選択し送信します。

シフトの確認をする場合は

![inquire](C:\Users\81808\OneDrive\デスクトップ\python\make_shift\images\inquire.png)

ダウンロードボタンを押しシフト候補のダウンロードを行います。

１シート目にはシフトの候補が出力され、足りない人員の場所は"＿dummy＿"としてダミーの従業員が入ります。それぞれの必要な人員は４,5列目に出力されます。

２シート目には従業員それぞれの名前と、出勤回数が出力されます。



## Description:

#### 	staticディレクトリ

​		styles.cssやアイコンの画像などが格納されています。

#### 	templateディレクトリ

​		htmlがここにあり、それぞれのページにおける処理と表示がここにあります。

##### 		layout

​			基本的なhtmlのレイアウトです。

##### 		apology

​			予期せぬエラーが起こった時のhtmlです。

##### 		delete

​			データベースから従業員を消すdeleteボタンを押したときのhtmlです。

##### 		index

​			基本的なhomeのhtmlです。

##### 		inquire

​			シフト照会ボタンを押されたときのhtmlです。

##### 		login

​			ログイン時のhtmlです。

##### 		register

​			従業員を新しく登録するregisterボタンをした時のhtmlです。

##### 		shift

​			シフト登録ボタンを押した場合のhtmlです。

#### 	application.py

​			基本的なpythonファイルとして、flaskでこちらが実行されます。

#### 	helpers.py

​			application.pyに用いられる関数がここに書かれています。シフト作成の関数などがあります。

#### 	users.db

​			従業員のデータベースです。personalテーブルがありカラムは（id, username, hash, shift）となっています。shiftにはその従業員が出られる日付が入っています。