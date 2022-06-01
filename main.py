from pytube import Youtube

link = input("Enter Youtube link: ")
yt = Youtube(link)

ys = yt.streams.get_highest_resolution()
ys.download()
print("Download Successful")