### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Creates the class, constructor and methods to for a new Email object.
class Email():

    has_been_read = False
    is_spam = False

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True


# --- Lists --- #
# Initialises an empty list to store the email objects.
inbox = []


# Initialises an empty list to store the spam email objects.
spam = []


# Initialises an empty list to store the deleted email objects.
email_bin = []


# --- Functions --- #
# Creates 3 sample emails and added them to the Inbox list.
def populate_inbox():
    new_email_1 = Email(
            "hyperiondev@gmail.com",
            "Course Progress",
            "You are currently on track with your bootcamp tasks.")
    new_email_2 = Email(
            "sarah.g@gmail.com",
            "Birthday Party!",
            "Hey! I hope you can make it to my party tomorrow!")
    new_email_3 = Email(
            "local_bank@gmail.com",
            "Interest Rate Increase",
            "Hello, This is an update to say your interest rate has doubled.")

    inbox.append(new_email_1)
    inbox.append(new_email_2)
    inbox.append(new_email_3)


# A function which prints the email’s subject_line, along with a corresponding number.
def list_emails():
    print("\nAll Emails:")
    for i, e in enumerate(inbox):
        disp_str = f"{i} "
        disp_str += f"{e.subject_line}"
        print(disp_str)


# A function which displays a selected email.
# And once displayed, the class method is called to set its 'has_been_read' variable to True.
# Also allows the user to delete or mark the email as spam.
def read_email(index):
    print()

    # Starts while and for loops to read the selected email
    while True:
        for i, t in enumerate(inbox):
            if i == index:
                disp_str = f"\nEmail: {i}\n"
                disp_str += f"From: {t.email_address}\n"
                disp_str += f"Subject: {t.subject_line}\n"
                disp_str += f"Content: {t.email_content}\n"
                print(disp_str)
                t.mark_as_read()
                print(f"\nEmail from {t.email_address} marked as read.\n")

        # Allows the user to delete or mark an email as spam
        edit_choice = input("Do you want to delete the email or mark it as spam? (or -1 to return to the main menu) (Delete/Spam): ")

        # Exits back to main menu loop
        if edit_choice == '-1':
            break

        # Deletes the selected email by removing it from the inbox and putting it in the bin list
        elif edit_choice.lower() == 'delete':
            email_bin.append(inbox.pop(index))
            print(f"\nEmail from {t.email_address} has been deleted.\n")
            break

        # Marks as Spam the selected email object, marks it as spam and puts it in the spam list
        elif edit_choice.lower() == 'spam':
            t.mark_as_spam()
            spam.append(inbox.pop(index))
            print(f"\nEmail from {t.email_address} marked as spam.\n")
            break

        else:
            print("Invalid input. Please choose either 'Delete' or 'Spam'.")


# --- Email Program --- #

# Calls the function to populate the Inbox for further use in the program.
populate_inbox()


# Creates menu with while loop
menu = True

while True:
    user_choice = int(input('''\n
Would you like to:
1. Read an email
2. View unread emails
3. Quit application

Enter selection: '''))

    if user_choice == 1:

        while True:
        # Lists all emails in inbox
            list_emails()

            # Calls the function to read an email by asking for user input
            email_choice = input("\nChoose the number of the email you'd like to read (or -1 to return to the main menu): ")

            # Returns to main menu if chosen
            if email_choice == '-1':
                break
            
            # Reads the selected email if chosen and provides for defensive coding
            else:
                try:
                    email_choice = int(email_choice)
                    if email_choice < 0 or email_choice > len(inbox):
                        print("\nInvalid email number. Please try again.")
                        continue
                except ValueError:
                    print("\nInvalid input. Please enter a number.")
                    continue
                read_email(email_choice)

    elif user_choice == 2:
        # For loop to view unread emails
        print("\nUnread Emails:")
        for i, e in enumerate(inbox):
            if e.has_been_read is False:
                print(f"{i} {e.subject_line}")


    elif user_choice == 3:
        # Function to quit appplication
        print('\nGoodbye!!!\n')
        exit()

    else:
        print("Oops - incorrect input.")
