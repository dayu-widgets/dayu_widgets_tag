#!/usr/bin/env python
# -*- coding: utf-8 -*-
###################################################################
# Author: Mu yanru
# Date  : 2019.8
# Email : muyanru345@163.com
###################################################################
"""
MCheckableTag
"""
# Import third-party modules
from dayu_widgets import dayu_theme
from dayu_widgets.mixin import cursor_mixin
from dayu_widgets.theme import QssTemplate
from qtpy.QtWidgets import QCheckBox


@cursor_mixin
class MCheckableTag(QCheckBox):
    """A checkable tag."""

    def __init__(self, text, parent=None):
        super(MCheckableTag, self).__init__(text, parent)
        self.setCheckable(True)
        style = QssTemplate(
            """
            MCheckableTag{
                spacing: 8px;
                padding-top: 4px;
                padding-bottom: 4px;
                padding-right: 8px;
                border-radius: @border_radius_base@unit;
                font-size: @font_size_small@unit;
            }
            MCheckableTag::indicator{
                width: 0;
                height: 0;
                background: transparent;
            }
            MCheckableTag:pressed{
                background-color: @primary_7;
            }
            MCheckableTag:checked{
                color: @text_color_inverse;
                background-color: @primary_color;
            }
            MCheckableTag:checked:hover{
                background-color: @primary_5;
            }
            MCheckableTag:unchecked{
                color: @secondary_text_color;
                background-color: transparent;
            }
            MCheckableTag:unchecked:hover{
                color: @primary_5;
            }
            """
        )
        self.setStyleSheet(style.substitute(vars(dayu_theme)))
