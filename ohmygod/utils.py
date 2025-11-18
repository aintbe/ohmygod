from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
import time
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

_COLOR_MAP: dict[Color, str] = {
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


class _MessageFormatter(dict[str, str]):
    """Message formatter that automatically handle missing keys."""

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
            Use one-digit numbers in the message string. This is because
            one digit prevents image distortion, numbers yields syntax 
            highlighting even in r-strings.
            - {0}: Base color
            - {1}: Point color
            
            Meanwhile, animation placeholders do not have to be numbered.
            They by nature causes image distortion and thus there is no 
            benefit in using numbered placeholders.
            - {placeholder}: Animation string
        """
        try:
            formatted_value = value.replace("{0}", "{base_color}") \
                                   .replace("{1}", "{point_color}")
        except IndexError:
            raise ValueError("Message string can only have {0} and {1} as numbered placeholders.")

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
        """        
        formatter = _MessageFormatter(**kwargs)
        return _Message.__instance(self.format_map(formatter))
    

    def clean(self):
        """Remove placeholders from the message."""
        return _Message.__instance(self.format_map(defaultdict(str)))
    

    def color(self, point: Color, base: Color = Color.DEFAULT):
        """Color a message with the point and base colors."""
        point_color = _COLOR_MAP.get(point)
        base_color = _COLOR_MAP.get(base)

        if not point_color or not base_color:
            raise ValueError("Invalid color")
        return self.format(base_color=base_color, point_color=point_color)


    def animate(self, partial_frames: list[dict[str, str]], interval: float = 0.5) -> _Animation:
        """Create an animation from the message with the given replacements."""
        return _Animation([
            _Frame(self.format(**pf), interval) for pf in partial_frames
        ])


@dataclass
class _Frame():
    message: _Message
    duration: float


class _Animation():
    """Animation class representing a series of frames."""
    def __init__(self, frames: list[_Frame]):
        if not frames:
            raise ValueError("Frames cannot be empty.")
        if any(frame.duration < 0 for frame in frames):
            raise ValueError("Frame duration cannot be negative.")
        
        self.frames = frames

    
    def activate(self) -> "_LiveContext":
        """Activate the animation to use in live."""
        return _LiveContext(self)
    

    def get_clean_message(self, index: int) -> _Message:
        """Get the clean message from the first frame."""
        if index < 0 or index >= len(self.frames):
            raise IndexError("Frame index out of range.")
        return self.frames[index].message.clean()


class _LiveContext():
    """Context for live messages, managing the current state."""
    def __init__(self, animation: _Animation):
        self._animation = animation
        self._current_index = None


    def next(self) -> _Message:
        """Get the next live message, after waiting for the duration."""
        if self._current_index is None:
            self._current_index = 0
        else:
            # Wait for the duration of the current frame
            current_frame = self._animation.frames[self._current_index]
            time.sleep(current_frame.duration)

            # Advance to the next frame
            self._current_index = (self._current_index + 1) % len(self._animation.frames)
        
        # print(f"Current index: {self._current_index} {len(self._animation)}")
        next_frame = self._animation.frames[self._current_index]
        return next_frame.message


    @property
    def frames(self) -> list[_Frame]:
        """Get all frames in the live message."""
        return self._animation.frames
