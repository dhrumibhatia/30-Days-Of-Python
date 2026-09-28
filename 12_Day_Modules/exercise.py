# level 1
# 1
import random 
import string


def rand_di_char(count=6):
    """Return ``count`` random upper- or lowercase ASCII characters."""
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(count))

print(rand_di_char())

#2
def user_id_gen_by_user():
    """Generate a user ID based on user input for number of characters and IDs."""
    num_chars = int(input("Enter the number of characters for the user ID: "))
    num_ids = int(input("Enter the number of user IDs to generate: "))
    return [rand_di_char(num_chars) for _ in range(num_ids)]
# print(user_id_gen_by_user())

#3
import random

def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return red, green, blue


red, green, blue = rgb_color_gen()

print(f"RGB value: rgb({red}, {green}, {blue})")

print(
    f"\033[48;2;{red};{green};{blue}m"
    f"          "
    f"\033[0m"
)

# Level 3
# 1
def shuffle_list(lst):
    """Shuffle the elements of a list in place."""
    random.shuffle(lst)
    return lst
print(shuffle_list([1, 2, 3, 4, 5]))

# 2
def random_int(start, end):
    """Return a random integer between start and end (inclusive)."""
    li = []
    while len(li) < 7:
        li.append(random.randint(start, end))
    return li
print(random_int(0,9))