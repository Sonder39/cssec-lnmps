import json
import subprocess

imageName = 'sonder39/john'
ips = {
    "web": 10001,
    "ssh": 10002
}
with open('info.json', 'r', encoding='utf-8') as f:
    info = json.load(f)
for teamInfo in info:
    for k in ips.keys():
        ips[k] += 10
    command = f"docker run -d --name={teamInfo['tname']} "
    command += f"-p {ips['web']}:80 -p {ips['ssh']}:22 "
    command += f"-e ROOT_PASSWORD={teamInfo['root_password']} "
    command += f"-e AWD_PASSWORD={teamInfo['awd_password']} "
    command += f"{imageName}:latest"
    subprocess.run(command, shell=True)
