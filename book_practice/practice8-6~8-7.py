# 练习8-6
def city_country(city,country):
    result = '"' + city + ',' + country + '"'
    return result
print(city_country('Santiago','Chile'))
print(city_country('Nanjing','China'))
print(city_country('Tokyo','Japan'))
# 练习8-7
def make_album(singer,album_name):
    album = {'singer':singer,'album_name':album_name}
    return album
print(make_album('Taylor Swift', '1989'))
print(make_album('Adele', '21'))
print(make_album('薛之谦','天外来物'))

def make_album(singer,album_name,num_songs=None):
    album = {'singer':singer,'album_name':album_name}
    if num_songs is not None:
        album['num_songs'] = num_songs
    return album
print(make_album('Ed Sheeran', '+', num_songs=16))

def make_album(singer,album_name,num_songs=None):
    album = {'singer':singer,'album_name':album_name}
    if num_songs is not None:
        album['num_songs'] = num_songs
    return album

while True:
    singer = input("请输入歌手的名字（输入 'q' 退出）：")
    if singer == 'q':
        break
    album_name = input("请输入专辑的名称：")
    num_songs = input("请输入专辑中的歌曲数量（如果不清楚可以不输入，直接按回车键）：")
    if num_songs:
        print(make_album(singer, album_name, int(num_songs)))
    else:
        print(make_album(singer, album_name))
