import configparser

config = configparser.ConfigParser()
config.read("config.ini")

user = config["general"]["username"]
fullname = config["general"]["fullname"]

print(user)
print(fullname)