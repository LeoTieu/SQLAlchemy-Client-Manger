from rich.console import Console
from rich.table import Table


def print_clients(list_of_clients):
    table = Table(title="Client Table")
    table.add_column("ID", justify="center", style="blue", no_wrap="True")
    table.add_column("Name", justify="center", style="blue", no_wrap="True")
    table.add_column("Adress", justify="center", style="blue", no_wrap="True")
    table.add_column("Total spent in sek", justify="center", style="blue", no_wrap="True")


    for client in list_of_clients:
        temp_list = [str(value) for value in client.values()]
        table.add_row(*temp_list)
    console = Console()
    console.print(table)
