import csv


class Csv:
    def __init__(self, csv_file):
        self.reader = csv.reader(open(csv_file, newline=''), delimiter=',')

    def parse(self):
        parsed = []
        # Ignore the first line, 't is the header
        next(self.reader)
        for row in self.reader:
            secret = {
                'path': self.path(row[0], row[1]),
                'username': row[2],
                'password': row[3],
                'url': row[4],
                'notes': row[5]
            }
            parsed.append(secret)
        return parsed

    def path(self, path, title):
        path_a = path.split('/')
        if path_a[0] == 'Root':
            vault_path_a = path_a[1:]
        else:
            vault_path_a = path_a
        vault_path_a.append(title)
        return '/'.join(vault_path_a)
