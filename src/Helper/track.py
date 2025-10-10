from time import time
from os import getpid
from psutil import Process
from Helper.color import *
#for decorate

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
        print()
        print("=============memory used stat==============")
        print(f"Function : {bcolors.GREEN}{func.__name__}{bcolors.ENDC}")
        # print(f"memory before: {memoryBefore:,} bytes")
        # print(f"memory after: {memoryAfter:,} bytes")
        print(f"memory consumed: {bcolors.GREEN}{memUsed:,}{bcolors.ENDC} bytes")
        print(f"function execution time : {bcolors.GREEN}{endTime}{bcolors.ENDC} seconds")
        print("===========================================")
        print()
        return result
    return wrapper
