import pandas as pd

# Load the dataset
df = pd.read_csv("path_to_your_data.csv")

# 1. People of each race
race_counts = df['race'].value_counts()

# 2. Average age of men
average_age_men = df[df['sex'] == 'Male']['age'].mean()

# 3. Percentage of people with a Bachelor's degree
bachelor_percentage = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100

# 4. Percentage of people with advanced education making more than 50K
advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
advanced_education_salary = advanced_education[advanced_education['salary'] == '>50K']
percentage_advanced_salary = (advanced_education_salary.shape[0] / advanced_education.shape[0]) * 100

# 5. Percentage of people without advanced education making more than 50K
no_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
no_advanced_education_salary = no_advanced_education[no_advanced_education['salary'] == '>50K']
percentage_no_advanced_salary = (no_advanced_education_salary.shape[0] / no_advanced_education.shape[0]) * 100

# 6. Minimum number of hours a person works per week
min_hours_per_week = df['hours-per-week'].min()

# 7. Percentage of people with the minimum number of hours working >50K
min_hours_salary = df[df['hours-per-week'] == min_hours_per_week]
min_hours_salary_50k = min_hours_salary[min_hours_salary['salary'] == '>50K']
percentage_min_hours_50k = (min_hours_salary_50k.shape[0] / min_hours_salary.shape[0]) * 100

# 8. Country with highest percentage of people earning >50K
country_salary = df[df['salary'] == '>50K'].groupby('native-country').size()
country_total = df.groupby('native-country').size()
percentage_country_50k = (country_salary / country_total) * 100
max_country = percentage_country_50k.idxmax()
max_percentage = percentage_country_50k.max()

# 9. Most popular occupation for people earning >50K in India
india_50k = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
popular_occupation_india = india_50k['occupation'].value_counts().idxmax()

# Print or return all the results
print(race_counts, average_age_men, bachelor_percentage, percentage_advanced_salary, 
      percentage_no_advanced_salary, min_hours_per_week, percentage_min_hours_50k, 
      max_country, max_percentage, popular_occupation_india)
