# Write a program to calculate the time to run 5 miles, 10 miles, half marathon, and full marathon if you can run at a constant speed. The distance of a half marathon is 13.1 miles and that of a full marathon is 26.2 miles. Report the time in the format of hours and minutes. Your program will prompt for your running speed (mph) as an integer.

# pompt usr to enter running speed
speed_str = input('Enter the running speed in mph: ')
# convert to int
speed = int(speed_str)

# calculate time take to run 5 miles
time = (5/speed)*60
if(time < 60):
    print('Time taken to run 5 miles: ', int(time), 'minutes')
else:
    hours = time/60
    minutes = time % 60
    print('Time taken to run 5 miles: ', int(
        hours), 'hours', int(minutes), 'minutes')

# calculate time in minutes to run 10 miles
time = (10/speed)*60
if(time < 60):
    time = (5/speed)*60
    print('Time taken to run 10 miles: ', int(time), 'minutes')
else:
    hours = time/60
    minutes = time % 60
    print('Time taken to run 10 miles: ', int(
        hours), 'hours', int(minutes), 'minutes')

# calculate time in minutes to run half marathon
time = (13.1/speed)*60
if(time < 60):
    time = (5/speed)*60
    print('Time taken to run half marathon: ', int(time), 'minutes')
else:
    hours = time/60
    minutes = time % 60
    print('Time taken to run half marathon: ', int(
        hours), 'hours', int(minutes), 'minutes')

# calculate time in minutes to run full marathon
time = (26.2/speed)*60
if(time < 60):
    time = (5/speed)*60
    print('Time taken to run full marathon: ', int(time), 'minutes')
else:
    hours = time/60
    minutes = time % 60
    print('Time taken to run full marathon: ', int(
        hours), 'hours', int(minutes), 'minutes')
