from datetime import datetime, date

date1 = datetime(2006, 5, 20)
date2 = datetime(2006, 5, 20)
date3 = datetime(2023, 5, 27)

users = [{'name': "Ivan",
        'birthday' : date1},
        {'name': "Igor",
        'birthday' : date2},
        {'name': 'Jack',
        'birthday': date3}]

def get_birthdays_per_week(users):

    result_list = []
    set_of_days = set()
    today = datetime.now()
    date_today = datetime(year=today.year, month=today.month, day=today.day).timestamp()
    deadline = datetime.now().timestamp() + 7 * 24 * 60 * 60 # Час через тиждень 

    # print(datetime.fromtimestamp(deadline), ' :deadline')
    for dicts in users:

        birthday_date = dicts['birthday'].replace(year=date.today().year)
        birthday_date_timestamp = birthday_date.timestamp()
        # print(birthday_date, ' :birthday_date')

        if deadline - birthday_date_timestamp > -1 and date_today - birthday_date_timestamp <= 0:

            
            day = datetime.strftime(dicts['birthday'], '%A')
            # today_day_of_week = datetime.strftime(today, '%A')
            timedelta = dicts['birthday'] - today 
            if day in ['Saturday', 'Sunday'] and timedelta.days > 2:
                day = 'Monday (in one week)'
            elif day in ['Saturday', 'Sunday']:
                day = 'Monday'
            
            result_list.append([day, dicts['name']])
            set_of_days.add(day)
    
    list_for_sort = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Monday (in one week)']
    set_of_days = list(set_of_days)
    set_of_days.sort(key=list_for_sort.index)

    for days in set_of_days:

        names_for_day = ', '.join([lists[1] for lists in result_list if lists[0] == days])
        
        print(f'{days}: {names_for_day}')

    




if __name__ == "__main__":
    get_birthdays_per_week(users)