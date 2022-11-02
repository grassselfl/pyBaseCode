# configparse
import configparser

# 写

config = configparser.ConfigParser()
config["DEFAULT"] = {
    "ServerAliveInterval": 45,
    "Compression": "yes"
}
config["bitbucket.org"] = {"user": "da"}

with open('../config.ini', 'w') as configfile:
    config.write(configfile)

# 读

config = configparser.ConfigParser()
config.read('config.ini')
print(config.sections())
print("bitbucket.org" in config)
print("b.org" in config)
print(config["bitbucket.org"]["user"])
print(config["DEFAULT"]["Compression"])
# print(config["DEFAULT"]["C"])#没有的会报错

config.add_section("add-section")
config.remove_section("bitbucket.org")
config.set("add-section", "k1", "111")
config.set("add-section", "k2", "222")
f = open("../newconfig.ini", 'w')
config.write(f)
f.close()
