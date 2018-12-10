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

f.show()
f.savetoFile('test.png', figsize=(15, 4))