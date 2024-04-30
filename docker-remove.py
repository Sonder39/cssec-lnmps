import subprocess

output = subprocess.check_output("docker ps -a | grep john", shell=True)
containers = [line.split()[-1] for line in output.decode().split('\n') if line]
if containers:
    cmd = "docker stop " + " ".join(containers)
    cmd += " && docker rm " + " ".join(containers)
    # print(cmd)
    subprocess.run(cmd, shell=True)
