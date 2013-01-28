#!/usr/bin/python3
# -*- coding: utf-8 -*-

#様々なグローバル変数群

canonb = []*CANBSIZ #削除か終了のためのバッファ
coremap = []*CMAPSIZ #コア割り当てのための空き
swapmap = []*SMAPSIZ #スワップ割り当てのための空き

rootdir = None #rootディレクトリのinodeのポインタ

cputype = None #CPUの種類　40，45，または　70

execnt = None #exec内のプロセス数

lbolt = None #time of day in 60th not in time
time = []*2 #1970年からの経過時間（秒）
tout = []*2 #次のスリープまでの時間

mpid = = None #一般的で独特なPID

runin = None #スケジューリングフラグ
runout = None #スケジューリングフラグ
runrun = None #スケジューリングフラグ

curpri = None #更なるスケジューリング

maxmem = None #プロセスごとの最大メモリ量

lks = None #クロックデバイスへのポインタ

rootdev = None #rootのdev conf.c参照
swapdev = None #swapのdev conf.c参照

swplo = None #スワップ空間のブロック数
nswap = None #スワップ空間のサイズ

updlock = None #同期のためのロック
rablock = None #前方読み込みのためのブロック

regloc = "" #ユーザーのレジスタ保存命令 trap.c参照

'''
ルーチンの呼び出し構造であり，クロックの割り込みによってアレンジされる。（clock.cを参照。）
時間の量を含む明確な引数を受け取ります。
例えばテレタイプ上での時間を遅延させるのに使われる。
'''
class Callo():
	def __init__(self, c_time, c_arg, c_func):
		self.c_time = c_time #増加する時間
		self.c_arg = c_arg #ルーチンの引数
		self.c_func = c_func #ルーチン

class Mount():
	'''
	マウント構造：
	マウントされたファイルのスーパーブロックと
	位置を特定するのに使われる。
	'''
	def __init__(self, m_dev, m_bufp, m_inodp):
		self.m_dev = m_dev #マウントされたデバイス
		self.m_bufp = m_bufp #スーパーブロックのポインタ
		self.m_inodp = m_inodp #マウントされたinodeへのポインタ
		
if __name__ == '__main__':
	print(__file__+" is loaded.")

