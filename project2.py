import random
import string

pass_length = random.randint(8, 16)
charvalue = string.ascii_letters + string.digits + string.punctuation

password = "".join([random.choice(charvalue) for i in range(pass_length)])

print("your random password is: ", password)