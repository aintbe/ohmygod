"""OH MY GOD package built upon rich console interface"""

__version__ = "0.2.0"

from .main import OhMyGod
from .utils import Color
from .messenger.buddha import Buddha

__all__ = ["OhMyGod", "Color", "Buddha"]
