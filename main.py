import folium # 匯入 folium 套件
import json

fmap = folium.Map(location=[25.01206450477216, 121.5414458747392], zoom_start=15)

path = r'F:\AI\Line_Chatbot\map_test\taipei_fitness.json'

with open(path, 'r', encoding='utf-8') as f:
    taipei_fitness = json.load(f) # taipei_fitness type :dict

taipei_fitness_list = taipei_fitness['features']

for mark in taipei_fitness_list:
    mark['geometry']['coordinates'].reverse()

    folium.Marker(location = mark['geometry']['coordinates']).add_to(fmap)

    print(mark['geometry']['coordinates'])

fmap.save(r"F:\AI\Line_Chatbot\map_test\taipei_fitness.html")