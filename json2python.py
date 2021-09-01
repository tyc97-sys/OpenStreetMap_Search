import json

path = r'F:\AI\Line_Chatbot\map_test\taipei_fitness.json'

with open(path, 'r', encoding='utf-8') as f:
    output = json.load(f)


print(output['features'][0]['geometry']['coordinates'])
# print(type(output))