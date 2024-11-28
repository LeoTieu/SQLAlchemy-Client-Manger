# Install pip dependency manager
# python get-pip.py --user
# pip install faker
from view import print_clients
from model import get_client_info, delete_client
from uuid import uuid4
from time import sleep


list_of_clients = [
    {
        "id": "0",
        "name": "Leo",
        "total_spent": 2000000,
        "address": "123 banana street"
    },
    {
        "id": "1",
        "name": "Thea",
        "total_spent": 100,
        "address": "123 banana street"
    }
]

PAUSE_TIME_SECONDS = 2


if __name__ == '__main__':
    while True:
        print("""
    **************************
    Welcome to CliManager v1.0
    **************************
    
    Select the number of your choice to display screen
    [1] - Print my clients
    [2] - Add a client
    [3] - Delete a client
    [4] - Exit
    """)

        user_input = input()

        if user_input == "1":
            print_clients(list_of_clients)
        elif user_input == "2":
            list_of_clients.append(get_client_info(uuid4()))
        elif user_input == "3":
            delete_client(list_of_clients)
        else:
            exit()
        sleep(PAUSE_TIME_SECONDS)
