import os
import re
# Custom context manager


class QueryFileWriter:
    def __init__(self, query, folder="output"):
        self.query = self._sanitize_filename(query)
        self.folder = folder
        os.makedirs(folder, exist_ok=True)  # Create folder if not exists
        self.filepath = os.path.join(folder, f"{self.query}.txt")
        self.file = None

    def _sanitize_filename(self, name):
        return re.sub(r'[\\/*?:"<>|]', "_", name)

    def __enter__(self):
        # overwrite if exists
        self.file = open(self.filepath, "w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
