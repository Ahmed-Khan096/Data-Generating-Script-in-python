import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define the features
features = [
    "gender","midterm_easy", "midterm_medium", "midterm_hard", "midterm_score",
    "final_easy", "final_medium", "final_hard", "final_score",
    "total_score", "mother_education", "father_education",
    "location", "is_cleared", "schooling"
]

# Function to generate a row of data
def generate_row():
    mother_education = random.choice(["1", "2", "3", "4", "5"])
    father_education = random.choice(["1", "2", "3", "4", "5"])
    
    location = random.choice(["1", "2"])
    



    # Generate midterm scores for easy, medium, and hard questions
    midterm_easy = random.randint(0, 15)
    midterm_medium = random.randint(0, 20)
    midterm_hard = random.randint(0, 15)
    midterm_score = midterm_easy + midterm_medium + midterm_hard

    # Generate final scores for easy, medium, and hard questions
    final_easy = random.randint(0, 15)
    final_medium = random.randint(0, 20)
    final_hard = random.randint(0, 15)
    final_score = final_easy + final_medium + final_hard

    # Calculate total score
    total_score = midterm_score + final_score

    # Determine if concept is cleared based on various factors
    is_cleared = random.randint(0, 2) # 0 for not cleared, 1 for cleared, 2 for average

    # Define schooling before using it in the return statement
    schooling = random.choice(["1", "2", "3", "4"])

    return [
        random.choice(["1", "2"]), # gender

        midterm_easy, # midterm_easy
        midterm_medium, # midterm_medium
        midterm_hard, # midterm_hard
        midterm_score, # midterm_score
        final_easy, # final_easy
        final_medium, # final_medium
        final_hard, # final_hard
        final_score, # final_score
        total_score, # total_score
        mother_education, # mother_education
        father_education, # father_education
        location, # location
        is_cleared, # is_cleared
        schooling, # schooling
 
    ]

# Generate the dataset
data = [generate_row() for _ in range(50000)]

# Create a DataFrame
df = pd.DataFrame(data, columns=features)

# Save to CSV
df.to_csv('loop5.csv', index=False)
