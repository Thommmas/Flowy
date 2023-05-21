import bencodepy

def parse_torrent_file(torrent_file_path):
    with open(torrent_file_path, 'rb') as file:
        data = file.read()

    torrent_data = bencodepy.decode(data)

    print(torrent_data)
    info = torrent_data['info']
    announce = torrent_data['announce']
    piece_length = info['piece length']
    name = info['name']
    files = []
    is_private = False
    trackers = []
    comment = ""

    if 'comment' in torrent_data:
        comment = torrent_data['comment']

    if 'announce-list' in torrent_data:
        for tracker_list in torrent_data['announce-list']:
            for tracker in tracker_list:
                trackers.append(tracker.decode())

    if 'private' in torrent_data:
        is_private = bool(torrent_data['private'])

    if 'files' in info:
        for file_info in info['files']:
            file_path = '/'.join(file_info['path'])
            file_size = file_info['length']
            files.append({'path': file_path, 'size': file_size})

    return {
        'announce': announce,
        'piece_length': piece_length,
        'name': name,
        'files': files,
        'is_private': is_private,
        'trackers': trackers,
        'comment': comment
    }
# Example usage
torrent_file_path = r'C:\Users\thoma\Downloads\Le_Parisien_-_22_Mai_2023.pdf.torrent'
torrent_info = parse_torrent_file(torrent_file_path)
print(torrent_info)
