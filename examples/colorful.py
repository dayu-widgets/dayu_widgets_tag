#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.8
# Email : muyanru345@163.com
###################################################################

# Import third-party modules
from dayu_widgets import MFlowLayout
from dayu_widgets import dayu_theme
from qtpy.QtWidgets import QApplication
from qtpy.QtWidgets import QVBoxLayout
from qtpy.QtWidgets import QWidget

# Import local modules
from dayu_widgets_tag import MTag


class Colorful(QWidget):
    def __init__(self, parent=None):
        super(Colorful, self).__init__(parent)
        preset_color_lay = MFlowLayout()
        for index, (text, color) in enumerate(
            [
                ("magenta", dayu_theme.magenta),
                ("red", dayu_theme.red),
                ("volcano", dayu_theme.volcano),
                ("orange", dayu_theme.orange),
                ("gold", dayu_theme.gold),
                ("lime", dayu_theme.lime),
                ("green", dayu_theme.green),
                ("cyan", dayu_theme.cyan),
                ("blue", dayu_theme.blue),
                ("geekblue", dayu_theme.geekblue),
                ("purple", dayu_theme.purple),
            ]
        ):
            tag = MTag(text)
            tag.set_dayu_color(color)
            if index > 5:
                tag.no_border()
            preset_color_lay.addWidget(tag)
        custom_color_lay = MFlowLayout()
        custom_color_lay.addWidget(MTag("#f00").coloring("#f00"))
        custom_color_lay.addWidget(MTag("#f66").coloring("#f66"))
        custom_color_lay.addWidget(MTag("#f0f").coloring("#f0f").no_border())

        main_lay = QVBoxLayout()
        main_lay.addLayout(preset_color_lay)
        main_lay.addLayout(custom_color_lay)
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import built-in modules
    import sys

    app = QApplication(sys.argv)
    test = Colorful()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
