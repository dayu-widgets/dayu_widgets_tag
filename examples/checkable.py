#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.8
# Email : muyanru345@163.com
###################################################################

# Import third-party modules
from dayu_widgets import MLabel
from dayu_widgets import dayu_theme
from qtpy.QtWidgets import QApplication
from qtpy.QtWidgets import QHBoxLayout
from qtpy.QtWidgets import QWidget

# Import local modules
from dayu_widgets_tag import MCheckableTag


class Checkable(QWidget):
    def __init__(self, parent=None):
        super(Checkable, self).__init__(parent)
        label = MLabel("Categories:")
        topic_lay = QHBoxLayout()
        topic_lay.addWidget(label)
        for i in ["Movies", "Books", "Music", "Sports"]:
            topic_lay.addWidget(MCheckableTag(text=i))
        topic_lay.addStretch()

        main_lay = QHBoxLayout()
        main_lay.addLayout(topic_lay)
        self.setLayout(main_lay)


if __name__ == "__main__":
    # Import built-in modules
    import sys

    app = QApplication(sys.argv)
    test = Checkable()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
