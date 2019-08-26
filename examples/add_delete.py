#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.8
# Email : muyanru345@163.com
###################################################################

from dayu_widgets_tag import MTag, MNewTag
from dayu_widgets.qt import QWidget, QHBoxLayout, QApplication, Slot
from dayu_widgets import dayu_theme, MFlowLayout


@dayu_theme.deco
class AddDelete(QWidget):
    def __init__(self, parent=None):
        super(AddDelete, self).__init__(parent)
        self.tag_lay = MFlowLayout()
        tag1 = MTag('Unremoveable')
        tag2 = MTag('Tag2').closeable()
        tag3 = MTag('Tag3').closeable()
        add_tag = MNewTag('New Tag')
        add_tag.sig_add_tag.connect(self.slot_add_tag)
        self.tag_lay.addWidget(tag1)
        self.tag_lay.addWidget(tag2)
        self.tag_lay.addWidget(tag3)
        self.tag_lay.addWidget(add_tag)

        main_lay = QHBoxLayout()
        main_lay.addLayout(self.tag_lay)
        self.setLayout(main_lay)

        geo = QApplication.desktop().screenGeometry()
        self.setGeometry(geo.width() / 4, geo.height() / 4, geo.width() / 2, geo.height() / 2)

    @Slot()
    def slot_add_tag(self, text):
        tag = MTag(text).closeable()
        self.tag_lay.insertWidget(self.tag_lay.count() - 1, tag)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = AddDelete()
    test.show()
    sys.exit(app.exec_())
