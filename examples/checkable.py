#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.8
# Email : muyanru345@163.com
###################################################################

from dayu_widgets_tag import MCheckableTag
from dayu_widgets.qt import QWidget, QHBoxLayout, QApplication, Slot
from dayu_widgets import dayu_theme, MLabel


@dayu_theme.deco
class Checkable(QWidget):
    def __init__(self, parent=None):
        super(Checkable, self).__init__(parent)
        label = MLabel('Categories:')
        topic_lay = QHBoxLayout()
        topic_lay.addWidget(label)
        for i in ['Movies', 'Books', 'Music', 'Sports']:
            topic_lay.addWidget(MCheckableTag(text=i))
        topic_lay.addStretch()

        main_lay = QHBoxLayout()
        main_lay.addLayout(topic_lay)
        self.setLayout(main_lay)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = Checkable()
    test.show()
    sys.exit(app.exec_())
