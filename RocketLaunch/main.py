'''
Write a program to ask a rocket launch controller to input a number of hours as an integer between

50 and 100. Convert this to days and hours and print the results in the following format:

“Launch in xx days, xx hours.”
'''

def TimeFinder():
    launch = False
    global time
    while launch == False:
        time = input('Enter how many hours left till launch: ')
        while time.lower() != 'end':
            try:
                int(time)
            except ValueError:
                print(time, 'Is not a integer. Enter a integer.')
                break
            else:
                if int(time) in range(50,101):
                    launch = True
                    break
                elif int(time) <50:
                    print('Invalid time enter a time above 50Hours. ')
                    launch = False
                    break
                elif int(time) >100:
                    print('Invalid time enter a time below 100Hours. ')
                    launch = False
                    break
    #Turns hours into minutes
    time = int(time)*60
    #Turns minutes into seconds
    time = int(time)*60
    #Calculates amount of days
    day = int(time) // (24 * 3600)
    #Calculates left over hours after the days
    time = int(time) % (24 * 3600)
    #Turns Minutes into hours
    hour = int(time) // 3600
    time %= 3600
    
    print('The Rocket will launch in ',day,' Days,',hour,' Hours.')

def programcycle():
    cycle = True
    while cycle == True:
        continueprogram = str(input('Do you want to set a timer for launch y/n: '))
        if continueprogram.lower() == 'y':
            TimeFinder()
        elif continueprogram.lower() == 'n':
            print('Thank You for using the Rocket Launch Program.')
            cycle = False

print('----------------------------------------')
print('           Rocket Launch Program        ')
print('----------------------------------------')

programcycle()