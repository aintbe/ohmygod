from abc import ABC, abstractmethod
from rich.text import Text

from ..utils import _Message, _LiveContext


class Messenger(ABC):
    @property
    @abstractmethod
    def BLESSING(self) -> _Message:
        pass

    @property
    @abstractmethod
    def PRAYER_LIVE(self) -> _LiveContext:
        pass

    @property
    @abstractmethod
    def HURRAY_LIVE(self) -> _LiveContext:
        pass

    @property
    @abstractmethod
    def ERROR(self) -> _Message:
        pass

    @property
    @abstractmethod
    def ERROR_FOCUS(self) -> _Message:
        pass

    @property
    def quotes(self) -> 'Quotes':
        """Importable messages for the OhMyGod"""
        return self.Quotes()

    class Quotes(ABC):
        @property
        @abstractmethod
        def BLESSING(self) -> Text:
            pass
            
        @property
        @abstractmethod
        def PRAYER(self) -> Text:
            pass

        @property
        @abstractmethod
        def HURRAY(self) -> Text:
            pass

        @property
        @abstractmethod
        def ERROR(self) -> Text:
            pass
