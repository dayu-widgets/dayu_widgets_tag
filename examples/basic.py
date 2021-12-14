#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.8
# Email : muyanru345@163.com
###################################################################

# Import built-in modules
import functools

# Import third-party modules
from dayu_widgets import dayu_theme
from qtpy.QtWidgets import QApplication
from qtpy.QtWidgets import QHBoxLayout
from qtpy.QtWidgets import QWidget

# Import local modules
from dayu_widgets_tag import MTag


class Basic(QWidget):
    def __init__(self, parent=None):
        super(Basic, self).__init__(parent)
        main_lay = QHBoxLayout()
        tag1 = MTag("Tag 1")
        tag2 = MTag("Clickable Tag").clickable()
        tag3 = MTag("Closeable Tag").closeable()

        tag2.sig_clicked.connect(
            functools.partial(self.slot_handle_signal, "sig_clicked")
        )
        tag3.sig_closed.connect(
            functools.partial(self.slot_handle_signal, "sig_closed")
        )
        main_lay.addWidget(tag1)
        main_lay.addWidget(tag2)
        main_lay.addWidget(tag3)
        main_lay.addStretch()
        self.setLayout(main_lay)

    def slot_handle_signal(self, text):
        print("Signal {} emitted.".format(text))


if __name__ == "__main__":
    # Import built-in modules
    import sys

    app = QApplication(sys.argv)
    test = Basic()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
