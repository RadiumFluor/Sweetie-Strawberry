import json
import config
from lib.main import client

configJson = json.loads(config.variables)

client.run(configJson["TOKEN"])
print("Cliente iniciado")



