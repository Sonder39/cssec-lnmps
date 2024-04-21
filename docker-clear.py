import subprocess

output = subprocess.check_output("docker images | grep none", shell=True)
image_ids = [line.split()[2] for line in output.decode().split('\n') if line]
if image_ids:
    cmd = "docker rmi " + " ".join(image_ids)
    # print(cmd)
    subprocess.run(cmd, shell=True)
