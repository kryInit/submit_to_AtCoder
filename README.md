# submit_to_AtCoder

## 用途
その名の通りプログラムをAtCoderにsubmitするときに使います  

1. ログイン  
2. サンプルケースで正しいか確認  
3. サンプルケースが全て通れば提出  

の手順を踏みます

## 使い方
`python hoge/app.py contest_grade contest_number task_grade source_code_path`  
で実行します  

例えば`./main.cpp`を`AGC030`の`A`問題に`./app.py`で提出するには  
`python app.py AGC 30 A ./main.cpp`  
で実行できます  

contest_grad, task_gradeは大文字,小文字のどちらでも良いです  

## その他
`constant.py`の`USERNAME`と`PASSWORD`に適切なものを入力してから使ってください  
password直書きはどうなのだろうかと思いましたが、他に良い方法を思いつき(知り)ませんでした... 

## 注意事項及び免責事項
このプログラムはpython,スクレイピング初心者が勉強のために製作したものです  
将来的にAtCoderのサイト構成や提出方法などが変更された場合、正常に提出できなくなる可能性があります  
また、サンプルケースでのチェックも絶対に成功するとは限らないことをご理解ください

このプログラムを使用したことによる全ての損害・不都合等については、一切責任を負いません  
自己責任でご利用ください  
