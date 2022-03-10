# Display the appropriate message as per 
# the colour of signal at the road crossing

msg = str(input("Enter colour of signal: "))
if msg == "red" or msg == "RED":
    print("STOP")

elif msg == "orange" or msg == "ORANGE" or msg == "yellow" or msg == "YELLOW":
    print("Go Slow!")

elif msg == "GREEN" or msg == "green":
    print("GO !")

else:
    print("Invalid input")
    