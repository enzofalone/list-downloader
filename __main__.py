from zippyshare_downloader import extract_info, extract_info_coro

download_links = []
queue_file = open('queue.txt', 'r')

#open the file and read the first line
link = queue_file.readline()
download_links.append(link.strip())

#store all links in an array
while link:
    print('Received ' + link)
    link = queue_file.readline()
    download_links.append(link.strip())

queue_file.close()

for item in download_links:
    extract_info(item,download=True)