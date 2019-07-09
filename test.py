import zing, vlc, processss
#data = input('Bạn muốn nghe: ')
process.maintain()
playlist = zing.zing_song(data)
#playlist,duration=mp3_links

#print (playlist)
inst = vlc.Instance()
player = inst.media_list_player_new()
mediaList = inst.media_list_new(playlist)
player.set_media_list(mediaList)
playing = set([1,2,3,4])
player.play()
if 'BÀI KẾ' in data or 'BÀI TIẾP THEO' in data: 
	player.next()
	print ('Đã phát bài kế tiếp')
elif 'BÀI TRƯỚC' in data:
	player.previous()
	print ('Đã phát bài kế trước')
elif 'DỪNG LẠI' in data:
	player.stop()
	print ('Đã dừng lại')