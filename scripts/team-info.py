import json
import subprocess

teamInfos = []
command = "pwgen -s 14 | md5sum"
for i in range(1, 28):
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    password = output.stdout.decode("utf-8").replace("  -\n", "")
    teamInfo = {
        "tid": i,
        "tname": f"team{i}",
        "root_password": "iyFYFMRyWIjB3Jol8dqg",
        "awd_password": password
    }
    teamInfos.append(teamInfo)

with open("/home/qing/Cardinal/data/team-info.json", "w") as f:
    json.dump(teamInfos, f)
