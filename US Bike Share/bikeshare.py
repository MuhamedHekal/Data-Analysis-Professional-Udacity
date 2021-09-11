import time
import pandas as pd

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'w': 'washington.csv' }

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Input The City You Want To Filter ch - ny - w  \n ").lower()
    while city not in CITY_DATA.keys():
        city = input("Please Enter The Valid Input ch , ny , w \n ").lower()
      
        
    # get user input for month (all, january, february, ... , june)
    months = ["Jan","Feb","Ma","Ap","Ma","Ju","All"]
    month = input("input for month Jan - Feb - Ma - Ap - Ma - Ju - All\n").title()
    while month not in months :
        month = input("input a valid month Jan - Feb - Ma - Ap - Ma - Ju - All\n").title()
    
        
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["Mo","Tu","We","Th","Fr","Sa","Su","All"]
    day = input("input for day Mo - Tu - We - Th - Fr - Sa - Su - All \n").title()
    while day not in days :
        day = input("input a valid day Mo - Tu - We - Th - Fr - Sa - Su - All\n").title()
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load the data 
    df = pd.read_csv(CITY_DATA[city])
    df.drop('Unnamed: 0' , inplace = True , axis = 1)
    # convert the start time to date time format
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # make new col for month 
    df['month'] = df['Start Time'].dt.month_name()
    # make new col for days
    df['day'] = df['Start Time'].dt.day_name()
    #filter by month 
    if month != 'All':
        df = df[df['month'].str.startswith(month)]
    #filter by day
    if day != 'All':
        df = df[df['day'].str.startswith(day)]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The Most Common Month is " , df['month'].mode()[0])

    # display the most common day of week
    print("The Most Common Day Of Week is " , df['day'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The Most Common Start Hour is " , df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The Most Commonly used start station\n",df['Start Station'].mode()[0])

    # display most commonly used end station
    print("The Most Commonly used End station\n",df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Trip Path'] = "From " + df['Start Station'] + " To " + df['End Station']
    print("The Most Frequent Combination Of Start Station And End Station is \n" , df['Trip Path'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Travel Time " ,df['Trip Duration'].sum())

    # display mean travel time
    print("Average Travel Time " , df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        # Display counts of user types
        print("Counts Of User Type\n", df['User Type'].value_counts())
    
        # Display counts of gender
        print("Counts Of Gender\n", df['Gender'].value_counts())
    
        # Display earliest, most recent, and most common year of birth
        print("\nThe Earliest Year Of Birth: ", int(df['Birth Year'].min()))
        print("The Most Recent Year Of Birth: ", int(df['Birth Year'].max()))
        print("The Most Common Year Of Birth: ", int(df['Birth Year'].mode()[0]))
        
    except :
        
        print("Gender And Year Of Birth Not Available for Washington ")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):   
    """Displays Head Of Raw Data To The Users """
    try:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
        start_loc = 0
        while (view_data == 'yes'):
            print(df[['Start Time','End Time','Trip Duration','Start Station','End Station','User Type','Gender','Birth Year']].iloc[start_loc:start_loc +5])
            start_loc += 5
            view_data = input("Do you wish to continue?: yes or no\n").lower()
    except KeyError :
        while (view_data == 'yes'):
            print(df[['Start Time','End Time','Trip Duration','Start Station','End Station','User Type']].iloc[start_loc:start_loc +5])
            start_loc += 5
            view_data = input("Do you wish to continue?: yes or no\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
