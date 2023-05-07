import csv
import os


def read_contacts_from_csv(filename="contacts.csv"):
    contacts = []

    if not os.path.exists(filename):
        return contacts

    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contacts.append(row)
    except Exception as e:
        print(f"Error reading from file: {e}")

    return contacts


def write_contacts_to_csv(contacts, filename="contacts.csv"):
    if not contacts:
        return

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for contact in contacts:
                flattened_contact = flatten_contact(contact)
                writer.writerow(flattened_contact)
            csvfile.flush()
    except Exception as e:
        print(f"Error writing to file: {e}")


def flatten_contact(contact):
    flattened_contact = {}

    for key, value in contact.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                flattened_key = f"{key}_{sub_key}"
                flattened_contact[flattened_key] = sub_value
        else:
            flattened_contact[key] = value

    return flattened_contact


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
    name,
    mobile_phone,
    group=None,
    company={},
    other_phones={},
    emails={},
    melody={},
    other={},
):
    contact = {
        "name": name,
        "mobile_phone": mobile_phone,
        "group": group,
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
