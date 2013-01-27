#!/usr/bin/python3
# -*- coding: utf-8 -*-

#基本的な定数群：変更しないこと。

USIZE = 16 #ユーザーのブロックサイズ（*64）
NULL = 0
NODEV = -1
ROOTINO = 1 #全てのrootのi番号
DIRSIZ = 14 #ディレクトリごとの最大文字サイズ

#シグナル群：変更しないこと。

NSIG = 20
SIGHUP = 1 #ハングアップ
SIGINT = 2 #割り込み（rubout）
SIGQIT = 3 #終了（FS）
SIGINS = 4 #不正な命令
SIGTRC = 5 #トレースまたはブレークポイント
SIGIOT = 6 #iot
SIGEMT = 7 #emt
SIGFPT = 8 #浮動小数点の例外
SIGKILL = 9 #終了
SIGBUS = 10 #バスエラー
SIGSEG = 11 #セグメント違反
SIGSYS = 12 #sys
SIGPIPE = 13 #パイプの終端

#調整することができる変数群

NBUF = 15 #バッファーキャッシュサイズ
NINODE = 100 #コアinode数
NFILE = 100 #コアファイル構造数
NMOUNT = 5 #マウントできるファイルシステムの数
NEXEC = 3 #同時exec数
MAXMEM = 64*32 #プロセスごとの最大コア。最初の数はkw。
SSIZE = 20 #初期スタックサイズ（*64バイト）
SINCR = 20 #スタックの増加量（*64バイト）
NOFILE = 15 #開くことができるファイルの，プロセスごとの最大の数
CANBSIZ = 256 #タイプライターラインの最大サイズ
CMAPSIZ = 100 #コア割り当て領域の最大サイズ
SMAPSIZ = 100 #スワップ割り当て領域の最大サイズ
NCALL = 20 #同時呼び出しの最大数
NPROC = 50 #プロセスの最大数
NTEXT = 40 #純粋な文字列の最大数
NCLIST = 100 #clistの最大合計サイズ
HZ = 60 #時計の毎秒の刻み

#優先度：あまり変更しないこと。

PSWP = -100
PINOD = -90
PROBIO = -50
PPIPE = 1
PWAIT = 40
PSLEP = 90
PUSER = 100

#必要なプロセッサーのレジスタ

PS = 0177776
KL = 0177560
SW = 0177570

#アクセス整数の構造体群

class SingleInteger():
	def __init__(self, integ=0):
		self.integ = integ

class Bytes():
	def __init__(self, lobyte="", hibyte=""):
		self.lobyte = lobyte
		self.hibyte = hibyte
	
class Sequence():
	def __init__(self, r=[]):
		self.r = r

if __name__ == '__main__':
	print(__file__+" is loaded.")

