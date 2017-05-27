import yaml
from datetime import datetime, timezone


def read():
    """ Returns the config contents as a dictionary. """
    with open('config.yml', 'r') as file:
        return yaml.load(file)


def write(contents):
    """ Writes the contents to config.yml file. """
    with open('config.yml', 'w') as file:
        yaml.dump(contents, file)


def update_time(time=None):
    """ writes the time to the config.yml file. """
    if time is None:
        time = datetime.utcnow()

    if isinstance(time, datetime):
        # assume it is utc time
        time = time.replace(tzinfo=timezone.utc).timestamp()

    contents = read()
    contents['last_checked'] = time

    write(contents)