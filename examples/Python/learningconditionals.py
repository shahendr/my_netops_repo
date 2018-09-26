my_integer = 443
if my_integer > 0:
    print("Hey, that looks like a positive number!")

my_integer = -443
if my_integer > 0:
    print("Hey, that looks like a positive number!")

# This block commented out to avoid a type error, provided for consistency with lab guide
# my_integer = 'mmmm tacos!'
# if my_integer > 0:
#    print("Hey, that looks like a positive number!")

''' This block commented out for posterity, moving to if/elif tasks below.
new_string = "you call that a string?"
if "?" in new_string:
    print("Yep, there is a ? in that string")

if ":" in new_string:
    print("Yep, there is a colon...")

if "string" in new_string:
    print("Yep, the word string is in there...")
'''

''' This block commented out for posterity, moving to else tasks below
new_string = "you call that a string?"
if "?" in new_string:
    print("Yep, there is a ? in that string")

elif ":" in new_string:
    print("Yep, there is a colon...")

elif "string" in new_string:
    print("Yep, the word string is in there...")
'''

new_string = "you call that a sentence!"
if "?" in new_string:
    print("Yep, there is a ? in that string")

elif ":" in new_string:
    print("Yep, there is a colon...")

elif "string" in new_string:
    print("Yep, the word string is in there...")
else:
    print("Whoa, we got a catch-all now!")
