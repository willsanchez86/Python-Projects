from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)

    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get().upper()
    user = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            'email/username': user,
            'password': password
        }
    }

    if len(website) < 1 or len(user) < 1 or len(password) < 1:
        messagebox.showerror(title='OOPS', message='Please don\'t leave any fields blank!')
    else:
        try:
            with open('data.json', 'r') as file:
                #Reading old data
                data = json.load(file)
                #Updating old data with new data
                data.update(new_data)

        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)

        else:
            #Updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as file:
                #Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0,END)
            password_input.delete(0,END)
            messagebox.showinfo(title=website, message=f'Your credentials for {website} have been saved successfully!')

# ---------------------------- SEARCH CREDENTIALS ------------------------------- #
def search():
    website = website_input.get().upper()

    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            user = data[website]['email/username']
            password = data[website]['password']

    except FileNotFoundError:
        messagebox.showerror(title='Oops', message='You do not have any saved credentials.')

    except KeyError:
        messagebox.showerror(title='Oops', message=f'You have no credentials saved for {website}. '
                                                   '\nPlease check your spelling and try again.')
    else:
        messagebox.showinfo(title=website, message=f'Email/Username: {user}'
                                                   f'\nPassword: {password}')



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white', highlightthickness=0)

#Create Canvas Logo
canvas = Canvas(width=200, height=200, bg='white')
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text='Website:', bg='white')
website_label.grid(column=0, row=1)

username_label = Label(text='Email/Username:', bg='white')
username_label.grid(column=0, row=2)

password_label = Label(text='Password:', bg='white')
password_label.grid(column=0, row=3)

#Entry Boxes
website_input = Entry(width=32)
website_input.grid(column=1, row=1)
website_input.focus()

username_input = Entry(width=52)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, 'willsanchez86@gmail.com')

password_input = Entry(width=32)
password_input.grid(column=1, row=3)


#Buttons
search_button = Button(text='Search', bg='blue', fg='white', highlightthickness=0, width=16, command=search)
search_button.grid(column=2, row=1)

generate_password_button = Button(text='Generate Password', bg='white', highlightthickness=0, width=16, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text='Add', bg='white', highlightthickness=0, width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()