ENV = {}

def initEnv(path: str, file: str = ".env"):
    """
    Initialize the environment variables from a .env file.

    Args:
        path (str): The path to the directory containing the .env file.
        file (str): The name of the .env file. Defaults to ".env".
    """
    import os
    from dotenv import dotenv_values

    env_path = os.path.join(path, file)
    r = dotenv_values(env_path)

    for key, value in r.items():
        ENV[key] = value

def getEnvs() -> dict:
    """
    Get the environment variables.

    Returns:
        dict: A dictionary containing the environment variables.
    """
    return ENV

def getEnvByKey(key: str) -> str | dict:
    """
    Get the value of an environment variable by its key.

    Args:
        key (str): The key of the environment variable.

    Returns:
        str: The value of the environment variable, or None if the key does not exist.
    """
    return ENV.get(key) if key in ENV else f"Key '{key}' not found in environment variables."

def addEnv(key: str, value: str|dict|int) -> str|dict|int:
    """
    Add variables in environment

    Args:
        key (str): The key of the environment variable.
        Value (str|dict|int): The value can be a string or a dict or int 
    """

    if not ENV.get(key):
        ENV[key] = value

def updateEnvValueByKey(key: str, value: str|dict|int):
    """
    Update Value from key in ENV dict

    Args:
        key (str) : The key to access in environment dict
        value (str|dict|int) : The values was updated by the key
    """

    if ENV.get(key):
        ENV[key] = value