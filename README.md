## Poke-Controller-Modified 自作ライブラリ


```
pip install git+https://github.com/novast1024/pokelib
```

#### 使い方

import文

```
from pokelib import settings
from pokelib.combo import *
from pokelib.button import *
from pokelib.hatswitch import *
import pokelib.leftstick as ls
import pokelib.rightstick as rs
```

初期化ブロック
```
settings.python_command = self
settings.input_seconds = 0.05
settings.minimum_interval = 0.05
```

コマンド例
```
send(A(1), 1) # 一秒間Aボタン押して後、一秒待機
send(X() + Y()) # X,Yボタン同時押し
send(Hold(ls.Up() + ls.Right()), A(), A(), A()) # 左スティックを右上に押しながら、Aボタンを三回押す
```


サンプルプログラム

```
from Commands.PythonCommandBase import PythonCommand, ImageProcPythonCommand

from pokelib import settings
from pokelib.combo import *
# from pokelib.button import *
# from pokelib.hatswitch import *
import pokelib.leftstick as ls
# import pokelib.rightstick as rs


class Kurukuru(ImageProcPythonCommand):
    NAME = "クルクルテスト"

    def do(self):
        settings.python_command = self
        settings.input_seconds = 0.033
        settings.minimum_interval = 0.0
        c = Combo()
        c.parse(
            [
                ls.N(),
                ls.NNE(),
                ls.NE(),
                ls.ENE(),
                ls.E(),
                ls.ESE(),
                ls.SE(),
                ls.SSE(),
                ls.S(),
                ls.SSW(),
                ls.SW(),
                ls.WSW(),
                ls.W(),
                ls.WNW(),
                ls.NW(),
                ls.NNW()
            ] * 20
        )
        c.send()
```
