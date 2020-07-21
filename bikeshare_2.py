import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

def check_input(input_str,input_type):
    while True:
        input_read = input(input_str)
        try:
            if input_read in ['chicago','new york city','washington']and input_type == 1:
                break
            elif input_read in ['january','february','march','april','may','june','all'] and input_type ==2:
                break
            elif input_read in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'] and input_type ==3:
                break
            else:
                if input_type == 1:
                    print('wrong city')
                if input_type == 2:
                    print('wrong month')
                if input_type == 3:
                    print('wrong day')
        except ValueError:
            print('Sorry Error Input')
    return input_read

    city = check_input('chicago, new york city or washington',1)


    # TO DO: get user input for month (all, january, february, ... , june)
    month = check_input('please what is the month you need to filter',2)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input( 'please what is the day do you need to filter by ',3)


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

    df = pd.read_csv(CITY_DATA[city])

    #Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filter by month if applicable
    if month != 'all':
        #Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #Filter by month to create the new dataframe
        df = df[df['month'] == month]

    #Filter by day of week if applicable
    if day != 'all':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    #Returns the selected file as a dataframe (df) with relevant columns
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    print(f'the common month is:',common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    print(f'\ncommon day of week are:',common-day)

    #extract hour form start time column to ccreate an hour column
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]

    print(f'\ncommon start hour:', common_hour)


     #this code will display the perfoomance calcultion


    print(f"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print(f'this is common_start_station: ',common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print(f'this is common_end_station: ',common_end_station)

    #lets use str.cat to combine both start and end station
    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = DF['Start Station'].str.cat(df['End Station'], sep =' to ')
    Extremities = df['Start To End'].mode()[0]

    print(f'\nthe most frequent combination of trips are: ',Extremities)

    print(F"\nThis took {(time.time() - start_time)} seconds.")
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())


    print(f"\nThis took {(time.time() - start_time)} seconds")
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type:')
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if city != 'washington':
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print(df['Birth Year'].mode()[0])
    print(df['Birth Year'].max())
    print(df['Birth Year'].min())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   #function to display dataframe due to the request of user
def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    BIN_RESPONSE_LIST = ['yes', 'no']
    rdata = ''
    #counter variable is initialized as a tag to ensure only details from
    #a particular point is displayed
    counter = 0
    while rdata not in BIN_RESPONSE_LIST:
        print("\nDo you wish to view the raw data?")
        print("\nAccepted responses:\nYes or yes\nNo or no")
        rdata = input().lower()
        #the raw data from the df is displayed if user opts for it
        if rdata == "yes":
            print(df.head())
        elif rdata not in BIN_RESPONSE_LIST:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")

    #Extra while loop here to ask user if they want to continue viewing data
    while rdata == 'yes':
        print("Do you wish to view more raw data?")
        counter += 5
        rdata = input().lower()
        #If user opts for it, this displays next 5 rows of data
        if rdata == "yes":
             print(df[counter:counter+5])
        elif rdata != "yes":
             break

    print('-'*40)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
