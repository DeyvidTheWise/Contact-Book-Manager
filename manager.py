import csv
import os


def main():
    while True:
        print_menu()
        user_input = input("Please enter the number of your choice (0 to exit): ")

        if user_input == "0":
            print("Exiting the program.")
            break
        elif user_input == "1":
            add_contact()
        elif user_input == "2":
            delete_contact()
        elif user_input == "3":
            update_contact()
        elif user_input == "4":
            search_contact()
        elif user_input == "5":
            create_group()
        elif user_input == "6":
            manage_reminders()
        elif user_input == "7":
            import_export_contacts()
        elif user_input == "8":
            print_contact_list()
        else:
            print("Invalid input. Please enter a number between 0 and 8.")


def print_menu():
    print("\nContact Book Manager Menu")
    print("1. Add a new contact")
    print("2. Delete a contact")
    print("3. Update contact details")
    print("4. Search for a contact")
    print("5. Create a contact group")
    print("6. Manage birthday reminders")
    print("7. Import/Export contacts")
    print("8. Print contact list")
    print("0. Exit the program")


def create_contact(
    name, mobile_phone, company={}, other_phones={}, emails={}, melody={}, other={}
):
    contact = {
        "name": name,
        "mobile_phone": mobile_phone,
        "company": {
            "name": company.get("name", None),
            "occupation": company.get("occupation", None),
            "address": company.get("address", None),
            "web_page": company.get("web_page", None),
        },
        "other_phones": {
            "mobile_phone_2": other_phones.get("mobile_phone_2", None),
            "mobile_phone_3": other_phones.get("mobile_phone_3", None),
            "home_phone": other_phones.get("home_phone", None),
            "office_phone": other_phones.get("office_phone", None),
        },
        "emails": {
            "private_email_1": emails.get("private_email_1", None) if emails else None,
            "private_email_2": emails.get("private_email_2", None) if emails else None,
            "office_email": emails.get("office_email", None) if emails else None,
        },
        "melody": melody,
        "other": {
            "address": other.get("address", None) if other else None,
            "birth_day": other.get("birth_day", None) if other else None,
            "notes": other.get("notes", None) if other else None,
            "spouse": {
                "name": other.get("spouse", {}).get("name", None),
                "birthday": other.get("spouse", {}).get("birthday", None),
                "notes": other.get("spouse", {}).get("notes", None),
            },
            "children": other.get("children", {}),
        },
    }
    return contact


def add_contact():
    pass


def delete_contact():
    pass


def update_contact():
    pass


def search_contact():
    pass


def create_group():
    pass


def manage_reminders():
    pass


def import_export_contacts():
    pass


def print_contact_list():
    pass


if __name__ == "__main__":
    main()
