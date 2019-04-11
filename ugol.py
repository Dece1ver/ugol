from PyQt5 import QtWidgets, QtGui
from design import Ui_MainWindow  # импорт сгенерированного файла дизайна
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import sys


class MyInterface(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyInterface, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Nesuperzalupa')
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('chest.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(self.icon)
        self.fig = self.graph()
        self.gl = QtWidgets.QGridLayout(self.ui.widget)
        self.gl.setContentsMargins(2, 2, 0, 0)
        self.gl.setSpacing(1)
        self.canvas = Canvas(self.fig)
        self.gl.addWidget(self.canvas)
        self.ui.pushButton.clicked.connect(self.calc)

    def graph(self, diameter=None, step=None):
        fig = plt.figure()
        plt.title('Угол подъема резьбы')
        ax1 = plt.subplot2grid((1, 1), (0, 0))
        ax1.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8])

        font_dict = {'family': 'serif',
                     'style': 'normal',
                     'weight': 'normal',
                     'color': 'darkblue',
                     'size': 12}

        plt.xlabel('Диаметр резьбы, мм')
        plt.ylabel('Шаг резьбы, мм')
        plt.text(150, 8.1, '1°', fontdict=font_dict)
        plt.text(70, 8.1, '2°', fontdict=font_dict)
        plt.text(47, 8.1, '3°', fontdict=font_dict)
        plt.text(33.5, 8.1, '4°', fontdict=font_dict)
        plt.text(12, 8.1, '5°', fontdict=font_dict)

        def formula(i, k):
            return i / (np.tan(np.radians(k)) * np.pi)

        def eba_formula(d, k):
            return np.tan(np.radians(k)) * d * np.pi

        plt.plot([0, 220], [0, eba_formula(220, 0.5)], 'k', linewidth=0.5)
        plt.plot([0, formula(8.5, 1.5)], [0, 8.5], 'k', linewidth=0.5)
        plt.plot([0, formula(8.5, 2.5)], [0, 8.5], 'k', linewidth=0.5)
        plt.plot([0, formula(8.5, 3.5)], [0, 8.5], 'k', linewidth=0.5)
        plt.plot([0, formula(8.5, 4.5)], [0, 8.5], 'k', linewidth=0.5)
        if diameter and step:
            plt.scatter(diameter, step, color='darkred', s=40, marker='x')
            plt.text(diameter + 3, step + .2, f'{self.if_int(str(diameter))}x{self.if_int(str(step))}', color='darkred', weight='medium', size=12)
        plt.grid(True)   # линии вспомогательной сетки

        return fig

    def if_int(self, string):
        if string[-2:] == '.0':
            string = string[:-2]
            return string
        else:
            return string

    def calc(self):
        diameter = self.ui.diameter_input.text()
        step = self.ui.step_input.text()
        step = step.replace(',', '.')
        if not diameter.replace('.', '').isdigit() or not step.replace('.', '').isdigit() or diameter.count('.') >= 2 or diameter.count(',') >= 2 or step.count('.') >= 2 or step.count(',') >= 2:
            self.ui.diameter_input_2.setText('')
            self.ui.step_input_2.setText('')
            self.ui.statusbar.showMessage('Указанные параметры неверны!')
            self.gl.removeWidget(self.canvas)
            self.fig = self.graph()
            self.canvas = Canvas(self.fig)
            self.gl.addWidget(self.canvas)
            self.gl.update()
            self.ui.widget.update()
        else:
            diameter, step = float(diameter), float(step)
            # h = (0.5 * step * math.tan(math.radians(60)))
            # diameter = diameter - 2 * (3 / 8) * h
            tg = step / (diameter * np.pi)
            result = np.degrees(np.arctan(tg))
            self.ui.diameter_input_2.setText(str(round(result, 1)))
            self.ui.step_input_2.setText(str(int(round(result if result <= 5 else 5))))
            self.gl.removeWidget(self.canvas)
            self.fig = self.graph(diameter=diameter, step=step)
            self.canvas = Canvas(self.fig)
            self.gl.addWidget(self.canvas)
            self.gl.update()
            self.ui.widget.update()
            self.ui.statusbar.showMessage(f'Рекомендованная опорная пластина: {int(round(result if result <= 5 else 5))}°')


class Canvas(FigureCanvas):
    def __init__(self, fig, parent=None):
        self.fig = fig
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.updateGeometry(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap('splash.png'))
    splash.show()
    application = MyInterface()
    application.show()
    splash.finish(application)
sys.exit(app.exec())
