import csv
import os


def read_contacts_from_csv(filename="contacts.csv"):
    contacts = []
    contact_groups = {}

    if not os.path.exists(filename):
        return contacts, contact_groups

    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contacts.append(row)

                group_name = row.get("group")
                if group_name:
                    if group_name not in contact_groups:
                        contact_groups[group_name] = []
                    contact_groups[group_name].append(row)

    except Exception as e:
        print(f"Error reading from file: {e}")

    return contacts, contact_groups


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


def read_melodies_from_file(filename="melodies.txt"):
    melodies = []

    if not os.path.exists(filename):
        return melodies

    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            for line in file.readlines():
                melody_name, count = line.strip().split(",")
                melodies.append({"name": melody_name, "count": int(count)})
    except Exception as e:
        print(f"Error reading from file: {e}")

    return melodies


def write_melodies_to_file(melodies, filename="melodies.txt"):
    try:
        with open(filename, mode="w", encoding="utf-8") as file:
            for melody in melodies:
                file.write(f"{melody['name']},{melody['count']}\n")
    except Exception as e:
        print(f"Error writing to file: {e}")


def add_melody(melodies):
    if input_yes_no("Do you want to add a new melody? (y/n): ") == "y":
        melody_name = input("Enter the name of the new melody: ")
        melodies.append({"name": melody_name, "count": 0})
        write_melodies_to_file(melodies)
        print(f"Melody '{melody_name}' has been added.")
    else:
        print("Returning to main menu.")
    return melodies


def show_melodies(melodies):
    print("\nMelodies:")
    for index, melody in enumerate(melodies):
        print(f"{index + 1}. {melody['name']} (used by {melody['count']} contact(s))")
    print("\nPress Enter to return to the main menu.")

    while True:
        try:
            user_input = input()
            if user_input == "":
                break
            else:
                print("Please press Enter to return to the main menu.")
        except EOFError:
            print(
                "Unexpected input error. Please press Enter to return to the main menu."
            )


def delete_melody(melodies):
    if input_yes_no("Do you want to delete a melody? (y/n): ") == "y":
        print("Available melodies:")
        for index, melody in enumerate(melodies):
            print(f"{index + 1}. {melody['name']}")

        valid_input = False
        while not valid_input:
            try:
                melody_index = (
                    int(input("Enter the number of the melody you want to delete: "))
                    - 1
                )
                if 0 <= melody_index < len(melodies):
                    valid_input = True
                else:
                    print(
                        "Invalid input. Please enter a number corresponding to an available melody."
                    )
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except EOFError:
                print("Unexpected input error. Please try again.")

        melody = melodies[melody_index]

        if melody["count"] == 0:
            melodies.pop(melody_index)
            write_melodies_to_file(melodies)
            print(f"Melody '{melody['name']}' has been deleted.")
        else:
            print(
                f"Cannot delete melody '{melody['name']}'. {melody['count']} contact(s) are using it."
            )
    else:
        print("Returning to main menu.")

    return melodies


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
        elif user_input == "9":
            add_melody(melodies)
        elif user_input == "10":
            show_melodies(melodies)
        elif user_input == "11":
            delete_melody(melodies)
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


def input_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["y", "n"]:
            return answer
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")


def add_contact(contacts, contact_groups, melodies):
    print("Adding a new contact")
    name = input("Enter name: ")
    mobile_phone = input("Enter mobile phone: ")

    group = None
    if input_yes_no("Do you want to add a group? (y/n): ") == "y":
        group = input("Enter group: ")

    melody = None
    if input_yes_no("Do you want to add a melody? (y/n): ") == "y":
        print("Available melodies:")
        for index, melody in enumerate(melodies):
            print(f"{index + 1}. {melody['name']}")
        melody_index = int(input("Enter the number of the desired melody: ")) - 1
        melody = melodies[melody_index]["name"]
        melodies[melody_index]["count"] += 1

    company = {}
    if input_yes_no("Do you want to add company details? (y/n): ") == "y":
        company_name = input("Enter company name: ")
        occupation = input("Enter occupation: ")
        address = input("Enter company address: ")
        web_page = input("Enter company web page: ")
        company = {
            "name": company_name,
            "occupation": occupation,
            "address": address,
            "web_page": web_page,
        }

    # Add more fields and subgroups as needed

    contact = create_contact(
        name, mobile_phone, group=group, melody=melody, company=company
    )
    contacts.append(contact)

    if group:
        if group not in contact_groups:
            contact_groups[group] = []
        contact_groups[group].append(contact)

    return contacts, contact_groups


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
    contacts, contact_groups = read_contacts_from_csv()
    melodies = read_melodies_from_file()
    main()
