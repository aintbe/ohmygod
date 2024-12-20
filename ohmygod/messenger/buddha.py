from rich.text import Text

from .messenger import Messenger
from ..utils import Color, _Message


_BLESSING = _Message.from_str(r"""
      `--._    `-._   `-.   `.  \   :   /  .'   .-'   _.-'    _.--'
`--.__     `--._   `-._  `-.  `. `. : .' .'  .-'  _.-'   _.--'     __.--'
__    `--.__    `--._  `-._ `-. `. \:/ .' .-' _.-'  _.--'    __.--'    __
  `--..__   `--.__   `--._ `-._`-.`_=_'.-'_.-' _.--'   __.--'   __..--'
--..__   `--..__  `--.__  `--._`-q(-_-)p-'_.--'  __.--'  __..--'   __..--
      ``--..__  `--..__ `--.__ `-'_) (_`-' __.--' __..--'  __..--''
...___        ``--..__ `--..__`--/__/  \--'__..--' __..--''        ___...
      ```---...___    ``--..__`_(<_   _/)_'__..--''    ___...---'''
```-----....._____```---...___(__\_\_|_/__)___...---'''_____.....-----'''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        God Bless        Never Crash

""")

_PRAYER_TEMPLATE = _Message.from_str(r"""{0}
      `--._    `-._   `-.   `.  \   :   /  .'   .-'   _.-'    _.--'
`--.__     `--._   `-._  `-.  `. `. : .' .'  .-'  _.-'   _.--'     __.--'
__    `--.__    `--._  `-._ `-. `. {1}\:/{0} .' .-' _.-'  _.--'    __.--'    __
  `--..__   `--.__   `--._ `-._`-{1}.`{0}_=_{1}'.{0}-'_.-' _.--'   __.--'   __..--'
--..__   `--..__  `--.__  `--.{1}_`-{0}q(-_-)p{1}-'_{0}.--'  __.--'  __..--'   __..--
      ``--..__  `--..__ `--.__ `{1}-'{0}_) (_{1}`-{0}' __.--' __..--'  __..--''
...___        ``--..__ `--..__{1}`--{0}{2}{1}--'{0}__..--' __..--''        ___...
      ```---...__     ``--..{1}__`{0}_(<_   _/)_{1}'__{0}..--''    ___...---'''
```-----....._____```---..._{1}__{0}(__\_\_|_/__){1}__{0}_...---'''_____.....-----'''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^{1}^^^^^^^^^^^^^^^{0}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        {1}N a m u a m i t a b u l ~{0}

""")
_PRAYER_COLORED_TEMPLATE = _PRAYER_TEMPLATE.color(Color.YELLOW)
_PRAYER_ANIMATED = _PRAYER_COLORED_TEMPLATE.animate(["/___||_)", "(_||___\\"])
_PRAYER = _PRAYER_TEMPLATE.animate(["/__|__\\"])[0].clean()


_HURRAY_TEMPLATE = _Message.from_str(r"""
      `--._    `-._   `-.   `.  \   :   /  .'   .-'   _.-'    _.--'
`--.__     `--._   `-._  `-.  `. `. : .' .'  .-'  _.-'   _.--'     __.--'
__    `--.__    `--._  `-._ `-. `. \:/ .' .-' _.-'  _.--'    __.--'    __
  `--..__   `--.__   `--._ `-._`-.`_=_'.-'_.-' _.--'   __.--'   __..--'
--..__   `--..__  `--.__  `--._`-q(•u{2}-'_.--'  __.--'  __..--'   __..--
      ``--..__  `--..__ `--.__ `-'_) (_`-' __.--' __..--'  __..--''
...___        ``--..__ `--..__`--/__/  \--'__..--' __..--''        ___...
      ```---...___    ``--..__`_(<_   _/)_'__..--''    ___...---'''
```-----....._____```---...___(__\_\_|_/__)___...---'''_____.....-----'''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                  May no obstacle come across your way

""")
_HURRAY_ANIMATED = _HURRAY_TEMPLATE.animate(["•)p", _Message.from_str("-){1}⟡{0}").color(Color.CYAN)])
_HURRAY = _HURRAY_ANIMATED[0]

_ERROR_TEMPLATE = _Message.from_str(r"""{1}
      `--._    `-._   `-.   `.  \   :   /  .'   .-'   _.-'    _.--'
`--.__     `--._   `-._  `-.  `. `. : .' .'  .-'  _.-'   _.--'     __.--'
__    `--.__    `--._  `-._ `-. `. \:/ .' .-' _.-'  _.--'    __.--'    __
  `--..__   `--.__   `--._ `-._`-.`{0}_=_{1}'.-'_.-' _.--'   __.--'   __..--'
--..__   `--..__  `--.__  `--._`-{0}q(⊙_⊙)p{1}-'_.--'  __.--'  __..--'   __..--
      ``--..__  `--..__ `--.__ `-'{0}_) (_{1}`-' __.--' __..--'  __..--''
...___        ``--..__ `--..__`--{0}/__/  \\{1}--'__..--' __..--''        ___...
      ```---...___    ``--..__`{0}_(<_   _/)_{1}'__..--''    ___...---'''
```-----....._____```---...___{0}(__\_\_|_/__){1}___...---'''_____.....-----'''
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^{0}
                      """)
_ERROR_COLORED = _ERROR_TEMPLATE.color(Color.RED)
_ERROR_ANIMATION = _Message.from_str("""ALL within the palm of my hand
""")
_ERROR = _ERROR_TEMPLATE.clean() + _ERROR_ANIMATION


class Buddha(Messenger):
    @property
    def BLESSING(self):
        return _BLESSING
    
    @property
    def PRAYER_ANIMATED(self):
        return _PRAYER_ANIMATED
    
    @property
    def HURRAY_ANIMATED(self):
        return _HURRAY_ANIMATED
    
    @property
    def ERROR_COLORED(self):
        return _ERROR_COLORED
    
    @property
    def ERROR_ANIMATION(self):
        return _ERROR_ANIMATION
    
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
