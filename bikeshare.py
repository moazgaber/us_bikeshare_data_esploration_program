import time
import pandas as pd
import numpy as np  

CITY_DATA ={ 'chicago': 'chicago.csv',
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
    # TO DO: get user input for city 
    # (our_cites) for a valid input of citys --
    #  using whil to validate input 
    city = input("Would you like to see data for Chicago, New York city, or Washington?: " ).lower()
    our_cites = ['chicago','new york city','washington'] 
    while city.lower() not in our_cites:
         print('invalid city , try agin ')
         city = input('Would you like to see data for Chicago, New York city, or Washington? ').lower()
    

    # flilter data by day or monthe or both of them 
    # (our_filter) for our valid type of filters
    filter = input("Would you like to filter the data by month, day, or both or none: ").lower()
    our_filter = ['month', 'day', 'both', 'none']
    while filter.lower() not in our_filter:
         print('not valid filter , try agin')
         filter = input('Would you like to see data for Chicago, New York, or Washington? : ').lower()

    # if chose month or both will chose a month from (our_monthes)
    our_monthes = ['january', 'february', 'march', 'april', 'may', 'june']
    if filter == 'month' or filter == 'both':
        month = input(" Which month - January, February, March, April, May, or June : ").lower()
        while month.lower() not in our_monthes   :
            print('not valid month , try agin')
            month = input(" Which month - January, February, March, April, May, or June : ").lower()
        #if the filter was none  
    else:
        month = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    our_days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    if filter == 'day' or filter == 'both':
        day = input("Which day :Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday,or  : ").lower()
        while day.lower() not in our_days:
            print('not valid day , try agin')
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday : ").lower()
            
        #if the filter was none 
    else:
        day = 'all'
      
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
    # load the data from the data - using the dic (CITY_DATA) and get the key of city from <input user>
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime to use the data in analysis
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
     # filter by month 
    if month != 'all':
        #find the exact month by geting the index of month + 1 -- becouse index staret from 0 
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month
        df = df[df['month'] == month]
     # filter by day of week
    if day != 'all':

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # (the_months) > to get the name of the month not the number of it 
    # (popular_month-1) to get the month from (the_months) 
    the_months= ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    print('Most Popular month:', (the_months[popular_month-1]))

    # TO DO: display the most common day of week
    # get the mod of df to know the most common . it's already datetime 
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular day:', popular_day_of_week)

    # TO DO: display the most common start hour
    # get the mod of (hour) df . it's already datetime
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour:', popular_hour )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Start Station:', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most end Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # get the freqent by make union df of (start station ) and (end station) and get the mod of it 
    df['union'] = df['Start Station'] + ' <to> ' + df['End Station']
    most_of_union = df['union'].mode()[0]
    print('Most Start and end station:', most_of_union)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'Total Travel Time: {total_travel_time}  seconds ')
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'Mean Travel Time: {mean_travel_time}  seconds ')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print("user type count : " , user_types_count)
 
    # TO DO: Display counts of gender
    # if gender in df get data to make filter only on chicago and new york .>not washington
    if 'Gender' in(df.columns):
        gender = df['Gender'].value_counts()
        print(f"user gender count : {gender}")

    #  earliest year of birth
    # if birth year in df get data to make filter only on chicago and new york .>not washington
    if 'Birth Year' in(df.columns):
        earliest = df['Birth Year'].min()
        print(f"the earliest year of birth: {earliest:.0f}")

    #  most recent year of birth
    if 'Birth Year' in(df.columns):
        print(f"the most recent year of birth: {df['Birth Year'].max():.0f}")
    
    # and most common year of birth
    if 'Birth Year' in(df.columns):
        print(f"most common year of birth: {df['Birth Year'].mode()[0]:.0f} ")

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
# Ask the user if he wants to display the raw data and print 5 rows at time
def display_raw_data(df):
    rows =input("Would you like to diplay 5 raws from data? (yes/no) ").lower()
    while rows == "yes":
        print(df.sample(5))

        rows =input("Would you like to diplay 5 raws from data? (yes/no) ").lower()
    



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
