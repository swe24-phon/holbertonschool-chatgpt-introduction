import subprocess

def remove_prefix(line, prefix):
    if line.startswith(prefix):
        return line[len(prefix):]
    return line

if __name__ == "__main__":
    prefix = "./"
    command = ["./test.py", "1", "2", "3"]
    result = subprocess.run(command, capture_output=True, text=True)
    
    for line in result.stdout.splitlines():
        print(remove_prefix(line, prefix))
