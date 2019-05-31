formats = {
    'bmp': {
        'extension': '.bmp'
    },
    'jpeg': {
        'extension': '.jgp'
    },
    'png': {
        'extension': '.png'
    },
    'gif': {
        'extension': '.gif'
    },
    'ico': {
        'extension': '.ico'
    }
}
    
keys = list(formats.keys())

extentions = []

for key in keys:
    extentions.append(formats[key]['extension'])