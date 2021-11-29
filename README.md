# Bad Store backend server
This is the [Bad store](https://github.com/willy00/BadStoreSecure) app backend server.
This handles user authentication and checkout process. The app also retrieves the products from this server to shown to the user. \n

## Development Environment setup
Creat virtual environment and install dependencies:
```commandline
source venv/scripts/activate
pip install -r requirements.txt
```
Command may be different on your system. \
Start the server by running
```commandline
python app.py
```
Server will automatically use the test DB included in the repository.