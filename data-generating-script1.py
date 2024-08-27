import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define the features
features = [ "gender", "study_time", "attendance", "quiz_score",
    "midterm_score", "final_score", "total_score",
    "average_score", "father_education", 
    "location", "schooling", "is_cleared", 
]

# Function to generate a row of data
def generate_row():
    father_education = random.choice(["1", "2", "3", "4", "5"])
    location = random.choice(["1", "2"])

    # Define study_time and attendance before using them in calculations
    study_time = random.randint(1, 18)
    attendance = random.randint(1, 30)

    # Introduce non-linear relationship between study_time and quiz/midterm scores
    quiz_score = random.randint(1, 10) + 2 * min(0, random.randint(1, 10) - study_time)
    midterm_score = round(random.randint(1, 100) + study_time * random.uniform(0.5, 1.5), 2)

    # Introduce linear relationship between attendance and final score
    final_score = round(random.randint(1, 100) + attendance * (random.random() + 0.5), 2)

    # Calculate total and average scores
    total_score = round(quiz_score + midterm_score + final_score , 2)
    average_score = round(total_score / 3, 2)

    # Determine if concept is cleared based on various factors
    is_cleared = random.choice(["1","2","3"])

    # Define schooling before using it in the return statement
    schooling = random.choice(["2", "3", "4", "5"])

    return [
        random.choice(["1", "2"]), # gender
        study_time, # study_time
        attendance, # attendance
        quiz_score, # quiz_score
        midterm_score, # midterm_score
        final_score, # final_score
        total_score, # total_score
        average_score, # average_score
        father_education, # father_education
        location, # location
        schooling, #scholling
        is_cleared, # is_cleared
    ]

# Generate the dataset
data = [generate_row() for _ in range(10000)]

# Create a DataFrame
df = pd.DataFrame(data, columns=features)

# Save to CSV
df.to_csv('new4.csv', index=False)
