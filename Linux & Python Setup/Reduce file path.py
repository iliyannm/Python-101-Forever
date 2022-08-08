def reduce_file_path(path):
    path = path.split('/')
    final_path = ['/']

    for i in range(len(path)):
        if path[i] == '.' or path[i] == '':
            continue

        elif path[i] == '..':
            if len(final_path) >= 1:
                final_path.pop()

        else:
            final_path.append(path[i] + '/')

    if not final_path:
        final_path = ['/']

    final_path = ''.join(final_path)

    if len(final_path) > 1:
        final_path = final_path[0:len(final_path) - 1]

    return final_path


tests = [
    ("/", "/"),
    ("/srv/../", "/"),
    ("/srv/www/htdocs/wtf/", "/srv/www/htdocs/wtf"),
    ("/srv/www/htdocs/wtf", "/srv/www/htdocs/wtf"),
    ("/srv/./././././", "/srv"),
    ("/etc//wtf/", "/etc/wtf"),
    ("/etc/../etc/../etc/../", "/"),
    ("//////////////", "/"),
    ("/../", "/")
]

for string, answer in tests:
    if answer == reduce_file_path(string):
        print(True)
    else:
        print(False)
