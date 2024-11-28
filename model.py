def get_client_info(id):
    name = input("name: \n")
    adress = input("adress \n")
    total_spent = input("adress \n")
    return_dict = {
        "id": id,
        "name": name,
        "total_spent": total_spent,
        "address": adress
    }
    return return_dict


def delete_client(input_list):
    uuid = input("Enter user id that you want to delete: ")
    user_to_remove = None
    for element in input_list:
        if element["id"] == uuid:
            user_to_remove = element
    
    if user_to_remove == None:
        print("id did not match any client")
    else:
        print(f'User {user_to_remove["id"]} has been successfuly deleted')
        input_list.remove(user_to_remove)
