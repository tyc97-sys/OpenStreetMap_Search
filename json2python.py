import json
# import geojson

# path = 'taipei_fitness.json'
path = 'fitness.geojson'

with open(path, 'r', encoding='utf-8') as f:
    output = json.load(f)

print(output["features"])
print(len(output["features"]))

for f in output["features"]:
    print(f["geometry"]["coordinates"])

# print(output)
