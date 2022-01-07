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

catkin_ws/srcに移動。  
```  
$cd ~/catkin_ws/src  
```  
今回使うリポジトリをクローンする。  
```  
$git clone https://github.com/Koutarou1123/kadai2.git  
```  

makeする。  
```  
$cd ~/catkin_ws  
$catkin_make  
```  

rosを起動させるために以下のコマンドを打ち込む。  
```  
roscore &  
```  

















