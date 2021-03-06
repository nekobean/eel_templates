import eel

# Set web files folder
eel.init("web")


@eel.expose  # Expose this function to Javascript
def say_hello_py(x):
    print(f"Hello from {x}")


say_hello_py("Python World!")
eel.say_hello_js("Python World!")  # Call a Javascript function

# Start application
eel.start("index.html", size=(640, 480))
