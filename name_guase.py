names = [
    "Aarav",
    "Ananya",
    "Bharat",
    "Bhavya",
    "Chirag",
    "Charu",
    "Dev",
    "Divya",
    "Eshan",
    "Esha",
    "Farhan",
    "Falguni",
    "Gaurav",
    "Gauri",
    "Harsh",
    "Harini",
    "Ishaan",
    "Isha",
    "Jai",
    "Jyoti",
    "Karan",
    "Kavya",
    "Laksh",
    "Lavanya",
    "Mohit",
    "Meera",
    "Nikhil",
    "Neha",
    "Om",
    "Ojasvi",
    "Pranav",
    "Pooja",
    "Qasim",
    "Qurat",
    "Rahul",
    "Riya",
    "Shubham",
    "Sneha",
    "Tarun",
    "Tanvi",
    "Uday",
    "Urvashi",
    "Vivek",
    "Vaishnavi",
    "Wasim",
    "Wamika",
    "Xavier",
    "Xenia",
    "Yash",
    "Yashika",
    "Zaid",
    "Zara",
]


def get_next_name(user_name):
    last_letter = user_name[-1].lower()

    for name in names:
        if name[0].lower() == last_letter:
            names.remove(name) 
            return name

    return None


while True:
    user_name = input("Enter a name (or 'exit' to quit): ")

    if user_name.lower() == "exit":
        print("Game Over!")
        break

    next_name = get_next_name(user_name)

    if next_name:
        print("Computer:", next_name)
    else:
        print("No matching name found.")
