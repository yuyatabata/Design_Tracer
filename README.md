# Design_Tracer

## Overview
イケてるデザインをトレースして学ぶWebアプリです。
自分の好きなデザイン(画像)をアップし、なぜイケてると思ったのか言語化したコメントをストックしていきます。
トレースしたデザインはユーザー情報と紐づいており、他人のトレースを覗くことも可能です。

企画参考：「デザインを「見る」訓練をしている話。4つのステップと勉強法」
 https://note.com/cha_sd/n/n1f7075798197

## Description
画像をストックしやすいよう、ドラッグ&ドロップでのアップロードを検討していました。
{{ form }}のようなDjangoのテンプレートタグを使用すると、どうしてもデフォルトボタンが表示されてしまう問題がありました。<br>  
そのため、下記のような手順でformクラスでのデータ取得を回避する方針を採りました。

1. HTMLのフォームタグからrequestデータを取得
2. FileSystemStorageでアップロードファイルを処理
3. ImageFieldに処理したファイルパスを渡す。

## TechnologyElement
Django/HTML/CSS/Javascript/Bootstrap/PostgreSQL/AWS/Gunicorn/Nginxなど

## Usage/Demo
1. ドラッグ&ドロップもしくはアップロードボタンで画像ファイルを選択
2. サブミットボタンを押すと画像のアップロードが完了です。
3. 過去アップロードした写真の一覧も表示されます。

トップページ
<img width="945" alt="トップ" src="https://user-images.githubusercontent.com/27131456/72234758-e6a2e300-3611-11ea-9f1d-d117ca35806c.png">

画像詳細：トレースのために言語化したコメントが確認できます
<img width="954" alt="detail" src="https://user-images.githubusercontent.com/27131456/72234777-fb7f7680-3611-11ea-9a1b-9929525d8a04.png">

他のユーザーがトレースした情報の閲覧も可能です。
<img width="718" alt="user" src="https://user-images.githubusercontent.com/27131456/72234821-2073e980-3612-11ea-8362-d2ab9dba7fac.png">

