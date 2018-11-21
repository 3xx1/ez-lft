# ez-lft
## Prerequisite
You will need to have [Docker](https://www.docker.com/) installed in your local environment.

## How to develop this python application (on Mac/Windows)
1. `make build` (or `.\MakeFile build` on Windows) - to build a docker image.
2. `make shell` (or `.\MakeFile shell` on Windows) - to attach the image and run. It will also take you in the container.
3. `pip install --trusted-host pypi.python.org -r requirements.txt` (Optional) - Only if you have a new pip package to install, run this following command in the container.
4. Run your python script! Example: `python src/app.py`
5. `exit` - to exit the container.
