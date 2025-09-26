from time import time
from os import getpid
from psutil import Process

#for decorate
from colorama import Fore

def get_process_memory():
    process = Process(getpid())
    return process.memory_info().rss

#For Requirement 8 and 9
def track(func):
    def wrapper(*args, **kwargs):
        #set up
        startTime = time()
        memoryBefore = get_process_memory()

        #test function
        result = func(*args, **kwargs)
    
        #time elapsed result
        memoryAfter = get_process_memory()
        endTime = time() - startTime
        memUsed = memoryAfter - memoryBefore

        print(f"{func.__name__} memory used stat")
        print(f"memory before: {memoryBefore:,} bytes")
        print(f"memory after: {memoryAfter:,} bytes")
        print(f"memory consumed: {memUsed:,} bytes")
        print(f"function execution time : {endTime} seconds")
        return result
    return wrapper
