from database import add_entry, get_entries, create_table, commit_changes, close_connection

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: 
"""

welcome = "Welcome to the programming diary!"

create_table()
commit_changes()

def prompt_new_entry():
    entry_content = input("What news you have today? ")
    entry_date = input("Enter the date: ")
    
    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"\n\n{entry["data"]}\n{entry["content"]}\n\n")


print(welcome)

while (user_input:=input(menu)) != '3':
    if user_input == '1':
        prompt_new_entry()
    if user_input == '2':
        view_entries(get_entries())
            
    else:
        print("Invalid option, Please try again...")