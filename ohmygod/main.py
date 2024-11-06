from rich.console import Console
from rich.text import Text
from rich.live import Live
from readchar import readkey
from threading import Thread, Event
import time
from queue import Queue

from .messenger.buddha import Buddha
from .messenger.messenger import Messenger


class OhMyGod(Console):
    """Console interface powered by gods and rich library"""
    def __init__(self, messenger: type[Messenger] = Buddha):
        super().__init__()
        self.messenger = messenger()
        self.bless()


    def bless(self):
        """Give a blessing to the program"""
        self.print(Text(self.messenger.BLESSING))

    
    @property
    def quotes(self):
        """Retrieve importable messages for the messenger"""
        return self.messenger.quotes

    
    def protect(self, message: str = ""):
        """Decorator to protect the execution of given function
        Run a long-running process and pray for its success until it ends
        """
        signal = Event()
        queue = Queue()

        def pray():
            with Live(auto_refresh=False, console=self) as live:
                state = 0
                while not signal.is_set():
                    prayer = Text(self.messenger.PRAYER_ANIMATED[state % 2])
                    dots = "." * (state % 4)

                    live.update(prayer + message + dots)
                    live.refresh()
                    time.sleep(0.5)
                    state += 1
        
        def decorator(func):
            def run_func(*args, **kwargs):
                try:
                    result = func(*args, **kwargs)
                    queue.put(result)
                except Exception as e:
                    queue.put(e)
                finally:
                    signal.set() # Stop the prayer
            
            def wrapper(*args, **kwargs):
                # Pray in a separate thread
                thread = Thread(target=pray)
                thread.start()
                run_func(*args, **kwargs)
                thread.join()

                # Return the result from the process
                if not queue.empty():
                    result = queue.get()
                    if isinstance(result, Exception):
                        raise result
                    return result
            return wrapper
        return decorator


    def success(self, message: str = ""):
        """Print a success message to the screen"""
        with Live(auto_refresh=False, console=self) as live:
            for i in range(3):
                live.update(Text(self.messenger.HURRAY_ANIMATED[i % 2] + message))
                live.refresh()
                if i < 2:
                    time.sleep(0.4 + 0.3 * i)
    

    def error(self, message: str = ""):
        """Print an error message to the screen"""
        self.print(Text(self.messenger.ERROR_COLORED), end="")

        # Print characters in the error message one by one
        for char in self.messenger.ERROR_ANIMATION:
            self.print(Text(char, style="red"), end="")
            time.sleep(0.1)

        self.print("\n" + message)


    def key(self, message: str = None) -> str:
        """Wait for a key press and return the key"""
        if message:
            self.print(message, end="")
        key = readkey()
        self.print(key)
        return key
