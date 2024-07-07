import subprocess

def runfinder():
    command = "python finder.py -w 32 -t 200 -p proxies.txt"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    runfinder()
