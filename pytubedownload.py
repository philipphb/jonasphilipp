from pytube import YouTube

link = input("Enter the link of YouTube video you want to download:  ")
resolutiom = input("Welche Auflösung soll das Video haben?")
yt = YouTube(link)

print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)

ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()
print("Download completed!!")