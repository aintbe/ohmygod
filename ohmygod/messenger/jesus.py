from rich.text import Text

from .messenger import Messenger
from ..utils import _Animation, _Frame, Color, _Message


_BLESSING = _Message.from_str(r"""
                                          ♥︎ ♡
             . *  ,♡ ° . ,       , ~⌒ヽ             ♡ ゜・。。
                                +v+^v+^+    ᢉ𐭩 ✧･ﾟ
              .'  ♡ '          (/(•灬•)\)  
  ✧･ﾟ                 ♥︎       ((/__""__\))          ♡ ・ 。 。・゜ ♡
           ╭(\ ͡ ◜◝╮フ          ))  \   ((
        , ͡   ( •w•) ' .,,♥︎    (/    \__ \)   |\\
      ⊂(     ͜    ◞╯         _(          .====^||===.   ・ ♡ ° . 。
       し╰◟◞ ͜  ͜ ◟◞╯       (            :X"====^^====`
           U   U          ^ ^  ^^^^  ^^^\|XXXXXXXXXX|  ♥︎
                                         ''''''''''''   ✧･ﾟ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        God Bless        Never Crash

""")

_PRAYER_TEMPLATE = _Message.from_str(r"""{0}
                                          {1}♥︎ ♡
             . *  ,♡ ° . ,       {0}, ~⌒ヽ{1}             ♡ ゜・。。
                                {0}+v+^v+^+{1}    ᢉ𐭩 ✧･ﾟ
              .'  ♡ '          {0}(/(•灬•)\){1}  
  ✧･ﾟ                 ♥︎       {0}((/__""__\))          {1}♡ ・ 。 。・゜ ♡{0}
           ╭(\ ͡ ◜◝╮フ          ))  \   (( {bread}
        , ͡   ( •w•) {1}' .,,♥︎{0}    (/    \__ \{arm} |\\
      ⊂(     ͜    ◞╯         _(          .{basket}=^||===.   {1}・ ♡ ° . 。{0}
       し╰◟◞ ͜  ͜ ◟◞╯       (            :X"====^^====`
           U   U          ^ ^  ^^^^  ^^^\|XXXXXXXXXX|  {1}♥︎{0}
                                         ''''''''''''   {1}✧･ﾟ{0}
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            {1}Don't you worry, I'm performing a miracle for you{0}

""").color(Color.MAGENTA)
_PRAYER_LIVE = _PRAYER_TEMPLATE.animate([
    {
        "bread": "",
        "arm": "   ",
        "basket": r"\ =",
    },
    {
        "bread": "",
        "arm": "_🍞",
        "basket": "===",
    },
    {
        "bread": "🍞 Take it!",
        "arm": "/  ",
        "basket": "===",
    },
])
_PRAYER = _PRAYER_LIVE.get_clean_message(2)

def _get_hurray_frames():
    frames = []

    for frame_i in range(1, 5):
        formatter = {}
        for key_i in range(1, 4):
            formatter[f"bread{key_i}"] = "🍞" if key_i == frame_i else "  "
            formatter[f"wine{key_i}"] = "🍷" if key_i == frame_i else "  "

        match frame_i:
            case 1:
                duration = 0.2
            case 4:
                duration = 0.3
            case _:
                duration = 0.1
        frames.append(_Frame(_HURRAY_TEMPLATE.format(**formatter), duration))

    return frames * 3 + frames[0:1]

_HURRAY_TEMPLATE = _Message.from_str(r"""
                                          ♥︎ ♡
             . *  ,♡ ° . ,       , ~⌒ヽ             ♡ ゜・。。
                                +v+^v+^+    ᢉ𐭩 ✧･ﾟ
              .'  ♡ '    {wine3}{wine2}  (/(•灬•)\)  {bread2}{bread3}
  ✧･ﾟ                 ♥︎    {wine1} ((/__""__\)) {bread1}       ♡ ・ 。 。・゜ ♡
           ╭(\ ͡ ◜◝╮フ        \ ))  \   (( /
        , ͡   ( •w•) ' .,,♥︎    \/    \__ \/  |\\
      ⊂(     ͜    ◞╯         _(          .====^||===.   ・ ♡ ° . 。
       し╰◟◞ ͜  ͜ ◟◞╯        (____       :X"====^^====`
           U   U          ^ ^  ^^^^  ^^^\|XXXXXXXXXX|  ♥︎
                                         ''''''''''''   ✧･ﾟ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                He that cometh to me shall never hunger
               He that believeth on me shall never thirst

""")
_HURRAY_LIVE = _Animation(_get_hurray_frames())
_HURRAY = _HURRAY_LIVE.get_clean_message(0)

_ERROR_TEMPLATE = _Message.from_str(r"""{0}
                                          ♥︎ ♡
             . *  ,♡ ° . ,       , ~⌒ヽ             ♡ ゜・。。
                                +v+^v+^+    ᢉ𐭩 ✧･ﾟ
              .'  ♡ '          (/(8灬8)\)
  ✧･ﾟ                 ♥︎       ((/__""__\))          ♡ ・ 。 。・゜ ♡
           ╭(\ ͡ ◜◝╮フ          ))  \   (( {1}🍃 Nothing...{0} 
        , ͡   ( -w-) ' .,,♥︎    (/    \__ \/  |\\
      ⊂(     ͜    ◞╯         _(          .====^||===.   ・ ♡ ° . 。
       し╰◟◞ ͜  ͜ ◟◞╯        (____       :X"====^^====`
           U   U          ^ ^  ^^^^  ^^^\|XXXXXXXXXX|  ♥︎
                                         ''''''''''''   ✧･ﾟ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                          """)
_ERROR_COLORED = _ERROR_TEMPLATE.color(Color.RED)
_ERROR_FOCUS = _Message.from_str("""We're out of bread...
""")
_ERROR = _ERROR_TEMPLATE.clean() + _ERROR_FOCUS


class Jesus(Messenger):
    @property
    def BLESSING(self):
        return _BLESSING
    
    @property
    def PRAYER_LIVE(self):
        return _PRAYER_LIVE.activate()
    
    @property
    def HURRAY_LIVE(self):
        return _HURRAY_LIVE.activate()
    
    @property
    def ERROR(self):
        return _ERROR_COLORED
    
    @property
    def ERROR_FOCUS(self):
        return _ERROR_FOCUS
    
    class Quotes(Messenger.Quotes):
        @property
        def BLESSING(self):
            return Text(_BLESSING)
        
        @property
        def PRAYER(self):
            return Text(_PRAYER)
        
        @property
        def HURRAY(self):
            return Text(_HURRAY)
        
        @property
        def ERROR(self):
            return Text(_ERROR)
