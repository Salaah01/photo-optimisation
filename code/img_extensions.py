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

extensions = []
type_and_extensions = []

for key in keys:
    extensions.append(formats[key]['extension'])
    type_and_extensions.append((key, "*" + formats[key]['extension']))

# Tuple with all the extentions (All Formats)
extensions_string = ""
for extension in extensions:
    extensions_string += f"*{extension} "

extensions_string = extensions_string.strip()

all_formats = [('All Supporetd Formats', extensions_string)] + type_and_extensions
