import os, glob


for dname in glob.glob("m*/"):
    dname = dname.strip("/")
    os.system(
        f"rclone sync  "
        + f"-v  "
        + f"--ignore-existing  "
        + f"--ignore-size "
        + f"--check-first "
        + f"{dname}/  bits-gdrive-manga:/{dname}/"
    )
