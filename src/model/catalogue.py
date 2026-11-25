from src.model.entry import Entry, EntryInfo

"""desc
    
Args:
    arg (type): desc

Returns:
    (type): desc

Raises:
    Error: desc
"""

class Catalogue:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._entries = list()
    
    def __str__(self):
        s = ""
        for i in range(len(self._entries)):
            s += str(self._entries[i])
            if not i == len(self._entries)-1:
                s += '\n'
        return s

    def add_entry(self, entry: Entry) -> None:
        """Dodaje wpis do katalogu

        Args:
            entry (Entry): Wpis do dodania
        """

        if not entry in self._entries:
            self._entries.append(entry)

    def remove_entry(self, entry: Entry) -> None:
        """Usuwa pierwszy pasujący wpis z katalogu

        Args:
            entry (Entry): Wpis do dodania

        Raises:
            ValueError: Katalog nie posiada wpisu
        """
        
        self._entries.remove(entry)

    def clear_entries(self) -> None:
        """Usuwa wszystkie wpisy z katalogu
        """

        self._entries.clear()

    def find_entry_by_title(self, title: str) -> Entry:
        """Zwraca pierwszy pasujący wpis z katalogu, lub (None) jeżeli nie występuje

        Args:
            title (str): Tytuł szukanego wpisu

        Returns:
            (Entry): Pierwszy wpis z pasującym tytułem
        """

        for e in self._entries:
            if e.info.title == title:
                return e
        return None
    
