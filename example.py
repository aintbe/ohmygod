from ohmygod import OhMyGod, Buddha
import time

omg = OhMyGod(Buddha)

@omg.protect("> Praying for a long running process")
def long_running_process(fail: bool):
    time.sleep(3)
    if fail:
        raise Exception("> Process failed")
    else:
        return "> Process succeeded"

# Print a message and get user input
key = omg.key("> Do you want to make it fail? (y/n): ")
fail = key.lower() == "y"

# Run the process and pray for success
try:
    res = long_running_process(fail)
    omg.success(res)
except Exception as e:
    # Show an error message if the process fails
    omg.clear()
    omg.error(str(e))

# Print using messages defined by the package
omg.print(omg.quotes.BLESSING)