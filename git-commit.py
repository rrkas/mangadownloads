import glob, os
from tqdm import tqdm
import pathlib, json

os.system(
    "git add *.py .gitignore && "
    + 'git commit -m "regular update: flushing" && '
    + "git push origin main",
)

# exit()

errors = {}
for fp in tqdm(sorted(pathlib.Path(".").glob("**/*.json"))):
    try:
        with open(fp) as f:
            json.load(f)
    except Exception as err:
        errors[str(fp)] = str(err)

if len(errors) > 0:
    print(json.dumps(errors, indent=4))

    exit()


os.system(
    "git add **/*.json && "
    + 'git commit -m "json updates" && '
    + "git push origin main",
)

# git checkout jsons && git add **/*.json && git commit -m "json updates" && git push origin jsons && git checkout main

for dir_path in sorted(glob.glob("./m*/*/imgs/*/")):
    os.system(
        f"git add {dir_path} && "
        + f'git commit -m "Updated: {dir_path.lstrip("./")}" && '
        + "git push origin main",
    )
    # os.system(f"sudo rm -rf {dir_path}")

os.system(
    "git add *.py .gitignore && "
    + 'git commit -m "regular update: flushing" && '
    + "git push origin main",
)
