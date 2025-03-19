from randomuser import RandomUser
import pandas as pd

# First, we will create a random user object, r.
r = RandomUser()

some_list = r.generate_users(10)

name = r.get_full_name()
# loop through the users
for user in some_list:
    print(user.get_full_name(), " ", user.get_email())

# print photos of the users
for user in some_list:
    print(user.get_picture)


def get_users():
    """function without parameter"""
    users = []

    for user in RandomUser.generate_users(10):
        users.append(
            {
                "Name": user.get_full_name(),
                "Gender": user.get_gender(),
                "City": user.get_city(),
                "State": user.get_state(),
                "Email": user.get_email(),
                "DOB": user.get_dob(),
                "Picture": user.get_picture(),
            }
        )

    return pd.DataFrame(users)


get_users()

df1 = pd.DataFrame(get_users())
print(df1)