import time
"""
Assuming 9pm -6am ->Dark and Day otherwise
"""
current_time = time.localtime()
print("Day" if (6<=current_time.tm_hour<=21) else "Night")