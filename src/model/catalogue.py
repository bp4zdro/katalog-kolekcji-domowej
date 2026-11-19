from src.model.entry import Entry, EntryInfo

class Catalogue:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._entries = list()
    
    def add_entry(self, entry: Entry) -> None:
        if not entry in self._entries:
            self._entries.append(entry)

    def remove_entry(self, entry: Entry) -> None:
        self._entries.remove(entry)

    def clear_entries(self) -> None:
        self._entries.clear()

    def find_entry_by_title(self, title: str) -> Entry:
        for e in self._entries:
            if e.info.title == title:
                return e
    
