from pytimedinput import timedInput
userText, timedOut = timedInput("Please, do enter something: ", timeout=10)
if(timedOut):
    print("Timed out when waiting for input.")
    print(f"User-input so far: '{userText}'")
else:
    print(f"User-input: '{userText}'")


# from pytimedinput import timedKey
# userText, timedOut = timedKey("Please, press 'y' to accept or 'n' to decline: ", allowCharacters="yn")
# if(timedOut):
#     print("Timed out when waiting for input. Pester the user later.")
# else:
#     if(userText == "y"):
#         print("User consented to selling their first-born child!")
#     else:
#         print("User unfortunately declined to sell their first-born child!")