from src.model.catalogue import Catalogue
from src.view.console_view import ConsoleView

def main() -> None:
    cat = Catalogue(entry_saver=None, entry_loader=None)
    view = ConsoleView(cat)

    while True:
        inpt = input('> ')
        try:
            view.process_input(inpt)
        except ValueError as e:
            print(e)


main()