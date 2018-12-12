# Every Python File i.e. anyname.py is known as Python Module
# Every Module is a main thread
print(__name__)

def main():
    print("==Welcome==")
    print("This is main thread")

# if you wish execution of program to begin from some point
if __name__ == "__main__":
    main()