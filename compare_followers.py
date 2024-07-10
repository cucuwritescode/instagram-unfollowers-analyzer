import json
# cargar data de los archivos de json
with open('followers.json', 'r') as file:
    followers_data = json.load(file)
with open('following.json', 'r') as file:
    following_data = json.load(file)
    following_data = following_data.get('relationships_following', [])
#extraer usuario de los seguidores
followers = set()
for entry in followers_data:
    if isinstance(entry, dict):
        for item in entry.get('string_list_data', []):
            followers.add(item['value'])
#extraer usuario de los seguidos
following = set()
for entry in following_data:
    if isinstance(entry, dict):
        for item in entry.get('string_list_data', []):
            following.add(item['value'])
#encontrar a los usuarios que seguis pero no te siguen
not_following_back = sorted(list(following - followers))
#imprimir resultado
print("Users not following back:", not_following_back)