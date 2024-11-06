"""OH MY GOD package built upon rich console interface"""

__version__ = "0.1.5"


from .main import OhMyGod
from .message import Message as HolyMessage
from .utils import Color as HolyColor

__all__ = ["OhMyGod", "HolyMessage", "HolyColor"]
