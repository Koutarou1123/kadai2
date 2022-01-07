# kadai2
ロボットシステム学　課題2　リポジトリ
## 概要
---
今回のリポジトリは先生が授業でやっていたcount.pyを残したままtwice.pyを改良し二倍にしていたものを三倍にした。  
奇数の数の時は絵文字を出力し偶数の時はそのままの数字を出力するというものです。

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
  
⑧次に初めにroscore開いた方での操作  
(rosに何が入っているか見たい場合)  
```  
$rostopic list  
```  
  
⑨count.pyが正常に動いているかの確認。抜け出すにはctrl+Cを使用する。   
```  
$rostopic echo /count_up  
```  
  
⑩twice.pyが正常に動いているかの確認。抜け出すにはctrl+Cを使用する。  
```  
$rostopic echo /twice  
```  
  




















