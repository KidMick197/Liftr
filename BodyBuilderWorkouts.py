from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import selenium.common.exceptions as selexcept
import pandas as pd
import numpy as np
import time
import re




with webdriver.Chrome() as driver:
    driver.get("https://www.bodybuilding.com/exercises/finder/index")
    buttonCheck = True
    start_time= time.time()
# ---------This clicks through workout check list-------    
    # time.sleep(2)
    # levelchecks = driver.find_elements_by_xpath("//input[contains(@name,'level[]')]")
    # checkList = driver.find_element_by_xpath("//input[contains(@name,'level[]')]")
    # time.sleep(2)

    # for count in range(len(levelchecks)):
        # if (levelchecks[count].is_selected()) != True:
        #     # diff =levelchecks[count].get_attribute('value')
        #     # difficulty = f"'{diff.title()}'"
        #     # pathString = "//span[contains(text(),'Expert)']"

        #     driver.find_element_by_xpath("//span[contains(text(),'Expert')]").click()
        #     time.sleep(3)
            
        # time.sleep(3)  
        # levelchecks = driver.find_elements_by_xpath("//input[contains(@name,'level[]')]") 
        # print(levelchecks[count].get_attribute('value'))
        # driver.find_element_by_class_name("ExLoadMore-btn").click()
        # time.sleep(3)
# ---------This clicks through workout check list-------

    while (buttonCheck is True):
        try:
            driver.find_element_by_class_name("ExLoadMore-btn").click()
            time.sleep(1)
        except selexcept.NoSuchElementException:
            buttonCheck = False
        
    
    workoutList=[['Workout Name','', 'Body Part', '','Equipment']]
    workouts=driver.find_elements_by_xpath("//div[contains(@class,'ExResult-cell--nameEtc')]") 

    for index, workoutNum in enumerate(workouts):
        workoutList.append( re.split(': |, |\*|\n',workouts[index].text))
    
    for item, items in enumerate(workoutList):
        del workoutList[item][1], workoutList[item][2]
        

    colName= workoutList.pop(0)
    df= pd.DataFrame(workoutList,columns = colName)
    df = df[~df['Body Part'].isin(['Forearms', 'Neck', 'Calves', 'Shoulders'])]
   
    df.reset_index(drop=True, inplace = True, )
    df.index = np.arange(1, len(df) + 1)

    df.loc[df['Body Part'].str.contains('Lats|Middle Back|Lower Back', case=False), 'Body Part'] = 'Back'
    df.loc[df['Body Part'].str.contains('Traps', case=False), 'Body Part'] = 'Shoulders'
    df.loc[df['Body Part'].str.contains('Abdominals', case=False), 'Body Part'] = 'Abs'
    df.loc[df['Body Part'].str.contains('Quadriceps|Hamstrings|Glutes|Adductors|Abductors', case=False), 'Body Part'] = 'Legs'
    df.fillna("Other")


    df.to_csv('WorkoutListClean.csv')
    print ("My program took", time.time() - start_time, "to run")






        


