import folium # 匯入 folium 套件
import json

self_coordinates = [25.01206450477216, 121.5414458747392]
fitness_coordinates = []

fmap = folium.Map(location=self_coordinates, zoom_start=13)


path = 'fitness.geojson'

with open(path, 'r', encoding='utf-8') as f:
    taipei_fitness = json.load(f) # taipei_fitness type :dict

taipei_fitness_list = taipei_fitness['features']

for mark in taipei_fitness_list:
    mark['geometry']['coordinates'].reverse()

    # folium.Marker(location = mark['geometry']['coordinates']).add_to(fmap)
    fitness_coordinates.append(mark['geometry']['coordinates'])

distance = []
# print(len(fitness_coordinates))

for coord in fitness_coordinates:
    dist = ((coord[0] - self_coordinates[0])**2 + (coord[1] - self_coordinates[1])**2) ** (1/2)
    distance.append(dist)
    # print(dist)

print(min(distance)*(111))
print(distance.index(min(distance)))

tooltip ='請點選我檢視該點資訊'
text_ = '與目前所在地最近的運動場所\n距離約 {:.2f} km'.format(min(distance)*(111))


# popup = folium.Popup(text_, min_width=500, max_width=500)
#
# html = '''目前所在地'''
#
# iframe = folium.IFrame(html)
# popup = folium.Popup(iframe,
#                      min_width=500, max_width=500)

m1 = folium.Marker(location=self_coordinates,
                   popup='<b>目前所在地</b>')

m2 = folium.Marker(location=fitness_coordinates[distance.index(min(distance))],
                   popup='<i>與目前所在地最近的運動場所<br>距離約 {:.2f} km</i>'.format(min(distance)*(111)),
                   icon=folium.Icon(color='green', # Marker顏色
                                    )) # 使用Font Awesome Icons

# m3 = folium.Marker(location=[35.715092, 139.796666],
#                    popup='Asakusa Temple',
#                    icon=folium.Icon(icon='info-sign',
#                                     color='red'))





# folium.Marker(location = self_coordinates,
#               popup=folium.Popup(folium.IFrame('目前所在地')),
#               icon=folium.Icon(color='red')).add_to(fmap)
# folium.Marker(location = fitness_coordinates[distance.index(min(distance))],
#               popup=folium.Popup(folium.IFrame('與目前所在地最近的運動場所<br>距離約 {:.2f} km'.format(min(distance)*(111)))),
#               tooltip=tooltip).add_to(fmap)


# print(fitness_coordinates)
fmap.add_child(child=m1)
fmap.add_child(child=m2)
fmap.save("taipei_fitness.html")