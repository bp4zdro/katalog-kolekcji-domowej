from src.model.catalogue import Catalogue
from src.view.console_view import ConsoleView

def main() -> None:
    cat = Catalogue(entry_saver=None, entry_loader=None)
    ConsoleView(cat).enter()

main()