from abc import ABC, abstractmethod
from rich.text import Text
from typing import List

from ..utils import _Message


class Messenger(ABC):
    @property
    @abstractmethod
    def BLESSING(self) -> _Message:
        pass

    @property
    @abstractmethod
    def PRAYER_ANIMATED(self) -> List[_Message]:
        pass

    @property
    @abstractmethod
    def HURRAY_ANIMATED(self) -> List[_Message]:
        pass

    @property
    @abstractmethod
    def ERROR_COLORED(self) -> _Message:
        pass

    @property
    @abstractmethod
    def ERROR_ANIMATION(self) -> _Message:
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
