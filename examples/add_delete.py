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
from qtpy.QtWidgets import QHBoxLayout
from qtpy.QtWidgets import QWidget

# Import local modules
from dayu_widgets_tag import MNewTag
from dayu_widgets_tag import MTag


class AddDeleteExampleWidget(QWidget):
    def __init__(self, parent=None):
        super(AddDeleteExampleWidget, self).__init__(parent)
        self.tag_lay = MFlowLayout()
        tag1 = MTag("Unremoveable")
        tag2 = MTag("Tag2").closeable()
        tag3 = MTag("Tag3").closeable()
        add_tag = MNewTag("New Tag")
        add_tag.sig_add_tag.connect(self.slot_add_tag)
        self.tag_lay.addWidget(tag1)
        self.tag_lay.addWidget(tag2)
        self.tag_lay.addWidget(tag3)
        self.tag_lay.addWidget(add_tag)

        main_lay = QHBoxLayout()
        main_lay.addLayout(self.tag_lay)
        self.setLayout(main_lay)

    def slot_add_tag(self, text):
        tag = MTag(text).closeable()
        self.tag_lay.insertWidget(self.tag_lay.count() - 1, tag)


if __name__ == "__main__":
    # Import built-in modules
    import sys

    app = QApplication(sys.argv)
    test = AddDeleteExampleWidget()
    dayu_theme.apply(test)
    test.show()
    sys.exit(app.exec_())
