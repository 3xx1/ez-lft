# ez-lft
## Prerequisite
You will need to have [Docker](https://www.docker.com/) installed in your local environment.

## How to enable your GUI environment
Since a Docker instance does not support GUI (such as rendering images, graph, etc.), you will need to configure your local environment to get it ready to lend its display. Remember this process is work-in-progress and supports only Mac user. Windows GUI environment setup is under development. Here is breakdown of the process:

### Configure Your .bash_profile to store IP address
1. In your terminal (or iTerm), type this command - `echo "export IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')" >> ~/.bash_profile`
2. Close your terminal and reopen it (this will reload the bash profile)
3. Type this command - `echo $IP`
4. If this returns your computer's IP address, you're good to go!

### Install XQuartz
1. If your computer doesn't have `brew` installed yet, do it from [here](https://brew.sh/)
2. Run `brew cask install xquartz`
3. Now you should have XQuartz app installed in your Applications/XQuartz directory. Open it.
4. Under "XQuartz" -> "Preferences" -> "Security" tab, enable the checkbox labeled as "Allow connections from network clients"
5. Close XQuartz app
6. REBOOT YOUR COMPUTER (important).

### Give an executable privilege to the GUI startup process automation shell script
1. In your terminal, go to this project directory. `cd path/to/ez-lft`
2. Run `sudo chmod +x enable-gui.sh`: this will allow Makefile to run this shell script at any circumstance

## How to develop this python application (on Mac/Windows)
1. `make build` (or `.\MakeFile build` on Windows) - to build a docker image.
2. `make shell` (or `.\MakeFile shell` on Windows) - to attach the image and run. It will also take you in the container.
3. `pip install --trusted-host pypi.python.org -r requirements.txt` (Optional) - Only if you have a new pip package to install, run this following command in the container.
4. Run your python script! Example: `python src/app.py`
5. `exit` - to exit the container.
