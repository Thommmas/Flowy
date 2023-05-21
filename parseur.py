import bencodepy

def parse_torrent_file(torrent_file_path):
    with open(torrent_file_path, 'rb') as f:
        torrent_data = bencodepy.decode(f.read())
    print(torrent_data)
    info = torrent_data[b'info']
    announce = torrent_data[b'announce']
    file_name = info[b'name']
    file_size = info[b'length'] # if 'length' in info else sum(f['length'] for f in info[b'files'])
    piece_length = info[b'piece length']
    pieces = info[b'pieces']

    print('Torrent Information:')
    print('===================')
    print(f'Tracker: {announce}')
    print(f'File Name: {file_name}')
    print(f'File Size: {file_size} bytes')
    print(f'Piece Length: {piece_length} bytes')
    print(f'Number of Pieces: {len(pieces) // 20}')

    # You can add more code here to extract additional information if needed

# Usage example
parse_torrent_file('C:/Users/thoma/Downloads/311D839C204D5D527FDF1084C0906258DF936427.torrent')
