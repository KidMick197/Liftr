import pandas as pd
import numpy as np 



df = pd.read_csv('WorkoutListClean.csv',  usecols=['Workout Name', 'Body Part', 'Equipment'])
bodyPartList = df['Body Part'].unique()
bodyParts=[]
workoutCount = 1




print(df.groupby('Body Part').size())
print('What are we workingout today?\n Enter DONE when complete')
bodyPart = input().title() or "Done"


while bodyPart != "Done":
    if bodyPart == "Full Body":
        bodyParts = bodyPartList.copy()
        bodyPart = "Done"
    elif bodyPart in bodyParts:
        print("You already said that")
        bodyPart = input().title() or "Done"
    elif bodyPart not in bodyPartList:
        print("Not in list")
        bodyPart = input().title() or "Done"
    else:
        bodyParts.append(bodyPart)
        bodyPart=""    
        bodyPart = input().title() or "Done"

workoutCount = int(input("Enter the number of workouts for today: "))

while workoutCount < 1:
   workoutCount = int(input("Must have atleast 1 workout: "))   

# ddf = df.loc[df['Body Part'].str.contains(bodyParts[0], case=False), 'Body Part']

ddf = pd.DataFrame(df[df['Body Part'].isin(bodyParts)])

todaysWorkout=ddf.sample(n=workoutCount)

print("Great! Have a fun working out!")
print(todaysWorkout)  




