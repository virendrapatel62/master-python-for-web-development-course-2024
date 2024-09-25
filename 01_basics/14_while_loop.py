is_recording = True

while is_recording:
    print("I Am recording Videos.")
    ans = input("Do you want to record more : ")
    is_recording = ans == 'Yes'  # True , False


print("End..")
