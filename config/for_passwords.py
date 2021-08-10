import base64
import configparser

config = configparser.ConfigParser()
config.read("config.cfg")

pw = config["server"]["Password"] # "pseudo"-crypted
print(base64.b64decode(pw).decode("utf-8")) # readable


##

print(base64.b64encode("geheim".encode("utf-8")))

print(base64.b64decode("Z2VoZWlt").decode("utf-8"))
