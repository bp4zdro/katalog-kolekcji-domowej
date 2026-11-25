from src.model.catalogue import Catalogue
from src.model.entry import *

class ConsoleView:
    def __init__(self, catalogue: Catalogue, *args, **kwargs) -> None:
        self.catalogue = catalogue

    def process_input(self, input: str) -> str:
        tokens = input.split(' ')

        match tokens[0]:
            case "LIST":
                print(self.catalogue.list_entries())
            
            case "ADD":
                info = EntryInfo("type", "desc", "authors", "year")
                entry = PhysicalEntry(info)
                self.catalogue.add_entry(entry)
            
            case "DEL":
                if len(tokens) < 1:
                    raise ValueError("Not enough input arguments")
                
                entry = self.catalogue.find_entry_by_title(tokens[1])
                self.catalogue.remove_entry(entry)
            
            case _:
                raise ValueError("Unknown input command")