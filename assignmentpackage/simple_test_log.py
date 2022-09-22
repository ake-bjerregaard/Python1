import sys
old_stdout = sys.stdout

log_file = open("message.testoop","w")

sys.stdout = log_file

print("this will be written to message.log")

sys.stdout = old_stdout

log_file.close()

# python file.py &> out.txt