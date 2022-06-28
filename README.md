# Vamp Technical Challenge

## Steps to get it up and running

1. `python3 -m venv env` to create a virtual environment
2. `env/bin/pip install -r requirements.txt` to install python dependencies.
3. Install [node version manager](https://github.com/nvm-sh/nvm)
4. Install a version of node (`nvm install node`)
5. Install yarn (`npm install -g yarn`)
6. Run yarn (`yarn`)
7. `yarn setup` to load the csv files into a sqlite database.
8. In one terminal `yarn start-api` to start the API server.
9. In another terminal `yarn start` to start the frontend server.
