[corporate_data_addition.py](https://github.com/user-attachments/files/27786171/corporate_data_addition.py)# corporate_data_addition

## 概要（OverView）
企業の業績データ（ROE,営業CF,自己資本比率）を管理・表示するプログラムです。
既存の辞書にない企業を入力した場合、新規データとして登録し、リストを更新することができます。

## 使い方（Usage）
1. Pythonをインストールする
2. ターミナルで以下を実行する
   corporate_data_addition(spilit関数ver.).py
   corporate_data_addition.py

4. 企業名を入力する
   ・既存の企業の場合(パナソニックホールディングス、富士通、NEC)：現在のデータが表示されます
   ・新規の企業の場合：ガイドに従って財務数値を入力するとデータが追加されます

## 学んだこと（what I learned）
- 辞書の階層構造
  辞書の中に辞書を入れ、複雑なデータ構造を管理する方法。
  
- KeyErrorの解決と初期化
  存在しないキーにアクセスしようとした際のエラー対処と新規のキーの作成手順

- split()関数の活用
  一行の入力をカンマ区切りで分割し、複数の変数へ同時に代入(アンパック)する手法
  
- f-stringのネスト
  文字列の中で辞書のキーを指定する際の、クォーテーションの使い分け（"と'）

## 目的（Purpose）
企業の財務分析において、複数の指標を効率的にデータ化・管理するためのPythonの基礎スキルを習得するため。
