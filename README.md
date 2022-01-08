# kadai2
ロボットシステム学　課題2　リポジトリ
## 概要
---
今回のリポジトリは先生が授業でやっていたcount.pyを残したままtwice.pyを改良し二倍にしていたものを三倍にしました。  
奇数の数の時は絵文字を出力し偶数の時はそのままの数字を出力するというものです。つまり偶数判別です。

---
## 動作環境  
・Raspberry Pi 4B  
・ubunt20.04.3 server  
・ROS1  

---
## 動作方法  
### [インストールする]  
以下のコマンドをディレクトリ内で実行してください。  

①catkin_ws/srcに移動。  
```
$cd ~/catkin_ws/src  
```

②今回使うリポジトリをクローンする。  
```
$git clone https://github.com/Koutarou1123/kadai2.git  
```

③makeする。  
```  
$cd ~/catkin_ws  
$catkin_make  
```  

④rosを起動させるために以下のコマンドを打ち込む。  
```  
roscore &  
```  

⑤別の端末を二つ起動しscriptsに移動。
```  
$cd ~/catkin_ws/src/mypkg/kadai2/scripts  
```  

⑥別端末の一つ目での操作  
count.pyをrosで動かす。  
```  
$rosrun mypkg count.py  
```  

⑦別端末の二つ目での操作  
twice.pyをrosで動かす。  
```  
$rosrun mypkg twice.py  
```  
ここで実行したプログラムが動いているのを確認する。  

⑧次に初めにroscore開いた方での操作  
(rosに何が入っているか見たい場合)  
```  
$rostopic list  
```  

⑨count.pyが正常に動いているかの確認。抜け出すにはctrl+Cを使用する。   
```  
$rostopic echo /count_up  
```  

## 実行結果  
---
以下のリンクから今回の動画がyoutubeで見ることが可能です。  
https://youtu.be/6SApEPgf9x0  
動画で見にくい方はこちらの写真をご覧ください。  
<img src="https://user-images.githubusercontent.com/95609545/148554056-9f996a7d-ff46-4ab6-a253-9e10e6efabff.jpg" width="500">
<img src="https://user-images.githubusercontent.com/95609545/148554225-05b1f70f-af0a-4b4e-82c5-e793bea6371b.jpg" width="500">  
## ライセンス  
---
BSD 2-Clause "Simplified" License  
ライセンスの詳細が見たい場合はリポジトリ内にあるLICENCEを参照してください。

  




















