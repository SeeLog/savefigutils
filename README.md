# savefigutils
Save figure(graph) scripts for python3 and pytorch

lossとかをグラフに図示したい時に使うと楽になりそうなスクリプト．

内部的にはグラフタイトル＋凡例でデータを管理しています．

## 使い方


`addColumn`でグラフタイトルとX軸Y軸ラベル設定

`addData`でデータを追加するグラフタイトルと凡例を指定してデータを追加

`savetoFile`で保存


使用例:
```python
from savefig import SaveFig
import math

f = SaveFig()
f.addColumn('test1', xlabel='epoch', ylabel='loss')
f.addColumn('test2', xlabel='epoch', ylabel='BLEU')
f.addColumn('test3', xlabel='epoch', ylabel='test')


for i in range(100):
    f.addData('test1', 'aaa', math.sin(i/10))
    f.addData('test1', 'bbb', math.cos(i/10))
    f.addData('test2', 'ccc', math.tan(i/10))
    f.addData('test3', 'ddd', math.log1p(i/10))

f.savetoFile('test.png', figsize=(15, 4))
```
