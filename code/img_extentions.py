formats = {
    'BMP': {
        'extension': '.bmp'
    },
    'JPEG': {
        'extension': '.jpg'
    },
    'PNG': {
        'extension': '.png'
    },
    'GIF': {
        'extension': '.gif'
    },
    'ICO': {
        'extension': '.ico'
    }
}
    
keys = list(formats.keys())

extentions = []

for key in keys:
    extentions.append(formats[key]['extension'])