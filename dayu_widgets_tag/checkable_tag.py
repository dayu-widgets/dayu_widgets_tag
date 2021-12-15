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
from dayu_widgets.qt import get_scale_factor
from dayu_widgets.theme import QssTemplate
from qtpy.QtWidgets import QCheckBox


@cursor_mixin
class MCheckableTag(QCheckBox):
    """A checkable tag."""

    def __init__(self, text, parent=None):
        super(MCheckableTag, self).__init__(text, parent)
        scale_x, x = get_scale_factor()
        self.setCheckable(True)
        style = QssTemplate(
            """
            MCheckableTag{
                spacing: @spaceing@unit;
                padding-top: @padding@unit;
                padding-bottom: @padding@unit;
                padding-right: @spaceing@unit;
                border-radius: @border_radius_base@unit;
                font-size: @font_size_base@font_unit;
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
        self.setStyleSheet(
            style.substitute(
                spaceing=8 * scale_x,
                padding=4 * scale_x,
                border_radius_base=dayu_theme.border_radius_base,
                unit=dayu_theme.unit,
                font_unit=dayu_theme.font_unit,
                font_size_base=dayu_theme.font_size_base,
                primary_5=dayu_theme.primary_5,
                primary_7=dayu_theme.primary_7,
                primary_color=dayu_theme.primary_color,
                secondary_text_color=dayu_theme.secondary_text_color,
                text_color_inverse=dayu_theme.text_color_inverse,
            )
        )
