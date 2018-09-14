def faulty():
    raise Exception("Something is wrong!")

def ignore_exception():
    faulty()

def handle_exception():
    try:
        ignore_exception()
    except:
        print("Exception handled.")


# ignore_exception()
# zhengjuns-MacBook-Pro:chapter08 zhengjun$ python3 exceptions_path.py
# Traceback (most recent call last):
#   File "exceptions_path.py", line 14, in <module>
#     ignore_exception()
#   File "exceptions_path.py", line 5, in ignore_exception
#     faulty()
#   File "exceptions_path.py", line 2, in faulty
#     raise Exception("Something is wrong!")
# Exception: Something is wrong!

handle_exception()
# zhengjuns-MacBook-Pro:chapter08 zhengjun$ python3 exceptions_path.py
# Exception handled.
