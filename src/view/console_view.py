from src.model.catalogue import Catalogue
from src.model.entry import *

class ConsoleView:
    def __init__(self, catalogue: Catalogue, *args, **kwargs) -> None:
        self.catalogue = catalogue

    def enter(self) -> None:
        while True:
            inpt = input('> ')
            try:
                if self.process_input(inpt):
                    break
            except ValueError as e:
                print(e)

    def process_input(self, input: str) -> bool:
        tokens = input.split(' ')

        match tokens[0]:
            case "EXIT":
                return True

            case "LIST":
                print(self.catalogue)
            
            case "ADD":
                info = EntryInfo("type", "title", "desc", "authors", "year")
                entry = PhysicalEntry(info)
                self.catalogue.add_entry(entry)
            
            case "DEL":
                if len(tokens) < 2:
                    raise ValueError("Not enough input arguments")
                
                entry = self.catalogue.find_entry_by_title(tokens[1])
                try:
                    self.catalogue.remove_entry(entry)
                except ValueError:
                    print("Entry not found")
                else:
                    print(f"Entry \"{tokens[1]}\" removed")
            
            case _:
                raise ValueError("Unknown input command")
        
        return False