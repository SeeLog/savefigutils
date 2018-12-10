import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class SaveFig():
    """lossなどをグラフに図示するためのクラス
    """
    def __init__(self):
        '''
        コンストラクタ
        '''
        self.fig_data_dict = {}
        self.xlabels_dict = {}
        self.ylabels_dict = {}
        self.grid_dict = {}

    def addColumn(self, title, xlabel='epoch', ylabel='', datadict=None, grid=True):
        """グラフの追加

        Arguments:
            title {str} -- グラフタイトル

        Keyword Arguments:
            xlabel {str} -- グラフのX軸 (default: {'epoch'})
            ylabel {str} -- グラフのY軸 (default: {''})
            datalist {dict} -- グラフの凡例とデータを直接与えて初期化する場合のみ指定 (default: {None})
            grid {bool} -- グリッドの有無 (default: {True})
        """
        self.xlabels_dict[title] = xlabel
        self.ylabels_dict[title] = ylabel
        if datadict == None:
            self.fig_data_dict[title] = {}
        else:
            self.fig_data_dict[title] = datadict
        self.grid_dict[title] = grid

    def addData(self, title, legend, data):
        """データの追加

        Arguments:
            title {str} --  グラフタイトル
            legend {str} -- 凡例
            data {float} -- 追加するデータ
        """

        if legend not in self.fig_data_dict[title]:
            self.fig_data_dict[title][legend] = []

        self.fig_data_dict[title][legend].append(data)

    def addDataList(self, title, legend, datalist):
        if legend not in self.fig_data_dict[title]:
            self.fig_data_dict[title][legend] = []
        self.fig_data_dict[title][legend].extend(datalist)

    def savetoFile(self, filename, figsize=(10, 4)):
        """

        Arguments:
            filename {str} -- 保存するファイル名

        Keyword Arguments:
            figsize {tuple} -- 保存する画像サイズ (default: {(10, 4)})
        """

        fig, tpl = plt.subplots(ncols=len(self.fig_data_dict), figsize=figsize)

        for title, ax in zip(self.fig_data_dict.keys(), tpl):
            for legend in self.fig_data_dict[title].keys():
                pdata = self.fig_data_dict[title][legend]
                ax.plot(range(1, len(pdata) + 1), pdata, linewidth=2, label=legend)

            ax.set_title(title)
            ax.set_xlabel(self.xlabels_dict[title])
            ax.set_ylabel(self.ylabels_dict[title])
            ax.grid(self.grid_dict[title])
            ax.legend()

        plt.savefig(filename, bbox_inches='tight')

