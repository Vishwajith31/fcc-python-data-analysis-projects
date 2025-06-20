import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset?
    race_count = df['race'].value_cou
    nts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Advanced education: Bachelors, Masters, or Doctorate
    advanced = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(advanced)]
    lower_education = df[~df['education'].isin(advanced)]

    # Percentage with salary >50K
    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # Minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # Percentage of rich among those who work the fewest hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage_min_workers = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    # Country with highest percentage of people earning >50K
    country_counts = df['native-country'].value_counts()
    rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    rich_percentage_by_country = (rich_counts / country_counts * 100).dropna()

    highest_earning_country = rich_percentage_by_country.idxmax()
    highest_earning_country_percentage = round(rich_percentage_by_country.max(), 1)

    # Most popular occupation for those who earn >50K in India
    top_IN_occupation = df[
        (df['native-country'] == 'India') & (df['salary'] == '>50K')
    ]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage_min_workers}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
