- use environment variables, then load all of them in a config.py

- Python config file parser https://docs.python.org/2/library/configparser.html and argparse https://docs.python.org/2/library/argparse.html.

- ConfigParser https://docs.python.org/3/library/configparser.html
Make config file store it somewhere else that you can make as easy/difficult to edit as you want
''' python
[configuration]
password = 11111
  
import ConfigParser
config = ConfigParser.ConfigParser()
config.read("/etc/config.txt")
pass = config.get("configuration","password")
```

- create credentials.py in the same directory write dictionary with passwords:
''' python
login = {
    'password' : 'YOUR_PASSWORD',
    'consumer_secret' : 'YOUR_SECRET'
}
import credentials
consumer_secret = credentials.login['consumer_secret']
gitignore file
```

- use a config.ini file which contains both the credentials and the normal settings. Then I add that config.ini to git ignore, and an empty sample_config.ini with no values to the repo.

- MACOS keyring. Interfaces with Keychain.app on my Mac, has a very user friendly interface, and let's me use a simple my_pass = keyring.get_password('reddit', 'n8henrie').
