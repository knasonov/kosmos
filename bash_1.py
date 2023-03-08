import subprocess

# Run a bash command and capture its output
output = subprocess.check_output(["ls", "-l"])

# Decode the output and print it
print(output.decode("utf-8"))