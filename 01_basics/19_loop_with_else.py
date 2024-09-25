# if False:
#     pass
# else:
#     pass

# when no break then it runs else


# for index in range(10):
#     if index == 5:
#         pass
#     print(index)
# else:
#     print("Loop break")


lectures = ["working",
            'working',
            'working',
            'working',
            'working']

# case 1 : watch the videos which are working


for status in lectures:
    if (status == 'fault'):
        break
    print("Watching the video")
else:
    print("Issue certificate")
