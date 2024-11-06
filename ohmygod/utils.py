from enum import Enum
from typing import Dict, List
from colorama import Fore


class Color(Enum):
	DEFAULT = "default"
	BLACK = "black"
	BLUE = "blue"
	CYAN = "cyan"
	GREEN = "green"
	MAGENTA = "magenta"
	RED = "red"
	WHITE = "white"
	YELLOW = "yellow"

_COLOR_MAP: Dict[Color, str] = {
	Color.DEFAULT: Fore.RESET,
	Color.BLACK: Fore.BLACK,
	Color.BLUE: Fore.MAGENTA,
	Color.CYAN: Fore.CYAN,
	Color.GREEN: Fore.GREEN,
	Color.MAGENTA: Fore.MAGENTA,
	Color.RED: Fore.RED,
	Color.WHITE: Fore.WHITE,
	Color.YELLOW: Fore.YELLOW,
}


class _MessageFormatter(dict):
    """Message formatter that automatically handlee missing keys."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __missing__(self, key: str):
        return f"{{{key}}}"


class _Message(str):
    """Message class that provides additional string manipulation methods."""
    def __new__(cls, _: str):
        raise TypeError("Use 'from_str' to create a Message instance.")

    @classmethod
    def from_str(cls, value: str) -> "_Message":
        """Factory method to validate and create a Message instance.
        
        Parameters
        ----------
        value : str
            Use one-digit numbers in the message string.  
            NOTE: One digit prevents image distortion, numbers yields syntax highlighting even in r-strings.
            - {0}: Base color
            - {1}: Point color
            - {2}: Animation
        """
        try:
            formatted_value = value.format("{base_color}", "{point_color}", "{animation}")
        except IndexError:
            raise ValueError("Message string can only have {0}, {1}, and {2} as placeholders.")

        return cls.__instance(formatted_value)


    @classmethod
    def __instance(cls, value: str):
        """Internal method for creating a Message instance without validation."""
        return super().__new__(cls, value)

        
    def format(self, **kwargs):
        """Format a message with the given placeholders.
        
        Parameters
        ----------
        base_color : str
            Substring to fill {0} in the message.
        point_color : str
            Substring to fill {1} in the message.
        animation : str
            Substring to fill {2} in the message.
        """        
        formatter = _MessageFormatter(**kwargs)
        return _Message.__instance(self.format_map(formatter))
    

    def clean(self):
        """Remove placeholders from the message."""
        return self.format(base_color="", point_color="", animation="")
    

    def color(self, point: Color, base: Color = Color.DEFAULT):
        """Color a message with the point and base colors."""
        point_color = _COLOR_MAP.get(point)
        base_color = _COLOR_MAP.get(base)

        if not point_color or not base_color:
            raise ValueError("Invalid color")
        return self.format(base_color=base_color, point_color=point_color)


    def animate(self, animations: List[str]):
        """Apply a series of animation to a message."""
        return [self.format(animation=animation) for animation in animations]
