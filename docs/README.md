# Tag for Dayu Widgets
Tag for categorizing or markup.

## When To Use
* It can be used to tag by dimension or property.
* When categorizing.


## Install
```pip install dayu-widgets-tag```

## Import Module
```python
from dayu_widgets_tag import MTag, MNewTag, MCheckableTag
```

## Examples

### Basic

![basic](_media/basic.png)


```python
tag1 = MTag('Tag 1')
tag2 = MTag('Clickable Tag').clickable()
tag3 = MTag('Closeable Tag').closeable()
```
[View source code](https://github.com/muyr/dayu_widgets_tag/tree/master/examples/basic.py)

You can use method `clickable` to make the tag clickable, and when you hover the tag, the cursor shape is `Qt.PointHandCursor`. After clicked, the signal `sig_clicked`will be emitted.
You can use method `closeable` to make the tag closeable.  the. After press the  `x` button closed, the signal`sig_closed`will be emitted.

### Style

You can use method`set_dayu_color(color)`to set the tag's color, `coloring(color)` works also.

You can use method`no_border()`to cancel the `border` style, then we will use `dayu_color` to fill the background.

We preset a series of color in `dayu_widgets.dayu_theme`.

![preset-color](_media/preset-color.png)

```python
from dayu_widgets import MFlowLayout, dayu_theme

preset_color_lay = MFlowLayout()
for index, (text, color) in enumerate([
    ('magenta', dayu_theme.magenta),
    ('red', dayu_theme.red),
    ('volcano', dayu_theme.volcano),
    ('orange', dayu_theme.orange),
    ('gold', dayu_theme.gold),
    ('lime', dayu_theme.lime),
    ('green', dayu_theme.green),
    ('cyan', dayu_theme.cyan),
    ('blue', dayu_theme.blue),
    ('geekblue', dayu_theme.geekblue),
    ('purple', dayu_theme.purple),
]):
    tag = MTag(text)
    tag.set_dayu_color(color)
    if index > 5:
        tag.no_border()
        preset_color_lay.addWidget(tag)
```

[View source code](https://github.com/muyr/dayu_widgets_tag/tree/master/examples/colorful.py)

You can also set it to a hex color string for custom color.

![custom-color](_media/custom-color.png)

```python
custom_color_lay = MFlowLayout()
custom_color_lay.addWidget(MTag('#f00').coloring('#f00'))
custom_color_lay.addWidget(MTag('#f66').coloring('#f66'))
custom_color_lay.addWidget(MTag('#f0f').coloring('#f0f').no_border())
```

[View source code](https://github.com/muyr/dayu_widgets_tag/tree/master/examples/colorful.py)

### Add & Remove Dynamically

You can use `MNewTag` class to add a tag dynamically. Make a tag closeable by `closeable()`, then you can delete the tag dynamically.

![tag_add_delete_light](_media/tag_add_delete_light.gif)

```python
# __init__

    self.tag_lay = MFlowLayout()
    self.tag_lay.addWidget(MTag('Unremoveable'))
    self.tag_lay.addWidget(MTag('Tag2').closeable())
    self.tag_lay.addWidget(MTag('Tag3').closeable())
    
    add_tag = MNewTag('New Tag')
    add_tag.sig_add_tag.connect(self.slot_add_tag)
    self.tag_lay.addWidget(add_tag)

@Slot()
def slot_add_tag(self, text):
    tag = MTag(text).closeable()
    self.tag_lay.insertWidget(self.tag_lay.count() - 1, tag)

```

[View source code](https://github.com/muyr/dayu_widgets_tag/tree/master/examples/add_delete.py)

### Checkable

`MCheckableTag`works like `QCheckBox`, click it to toggle checked state.

![tag_checkable_light](_media/tag_checkable_light.gif)

```python
topic_lay = QHBoxLayout()
topic_lay.addWidget(QLabel('Categories:'))
for i in ['Movies', 'Books', 'Music', 'Sports']:
    topic_lay.addWidget(MCheckableTag(text=i))
topic_lay.addStretch()
```

[View source code](https://github.com/muyr/dayu_widgets_tag/tree/master/examples/checkable.py)

## API

### MTag

**Inherits**： `QLabel`

#### Properties

* `dayu_color`: str the tag's color

#### Public Functions

* `MNewTag(text='New Tag', parent=None)`
* `get_dayu_color()` get the color of tag.
* `set_dayu_color(str)` set the color of tag.
* `coloring(str)` same as `set_dayu_color`, support chain.
* `closeable()` make the tag closeable, support chain.
* `clickable()`make the tag clickable, support chain.
* `no_border()`cancel the border style, fill the `dayu_color` to background instead, support chain.

#### Signals

* `sig_clicked()`emitted when tag clicked.
* `sig_closed()`emitted when tag closed.

### MCheckableTag

**Inherits**：`QCheckBox` 

Only change the stylesheet and  `setCheckable(True)`, no more extend.

please reference `QCheckBox` API .

### MNewTag

**Inherits**：`QWidget`

#### Public Functions

* `MNewTag(text='New Tag', parent=None)`
* `set_completer(QCompleter)` set the Completer when enter into edit mode

#### Signals

* `sig_new_tag(str)` emitted when user press enter to finish edit, the argument is the text user entered.

