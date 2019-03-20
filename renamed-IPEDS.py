import numpy as np
import pandas as pd

import matplotlib.pyplot as plt 
plt.style.use('seaborn')
import seaborn as sns

college = pd.read_csv("ipeds_data/2010_data.csv")


#Add column headers 
college.columns = columns = ["Index","Untid","Institution name", "State abbreviation", "Sector of institution", "Institution size Category", 
           "Degree of urbanization", "Year institution was deleted from IPEDS", "Undergraduate offering", 
           "Graduate offering",'Religious affiliation',
'Published in-state tuition and fees (current year)',
'Published out-of-state tuition and fees (current year)',
'Books and supplies (current year)',
'On campus, room and board (current year)',
'On campus, other expenses (current year)',
'Off campus (not with family), room and board (current year)',
'Off campus (not with family), other expenses (current year)',
'Off campus (with family), other expenses (current year)',
'Average net price-students awarded grant or scholarship aid',
'Percent of full-time first-time undergraduates awarded federal, state, local or institutional grant aid',
'Average amount of federal, state, local or institutional grant aid awarded',
'Percent of full-time first-time undergraduates awarded student loans',
'Average amount of student loans awarded to full-time first-time undergrad students',
'Total amount of grant and scholarship aid awarded, all income levels',
'Average amount of grant and scholarship aid awarded, all income levels',
'Number awarded grant and scholarship aid, income level (0-30,000)',
'Total amount of grant and scholarship aid awarded, income level (0-30,000)',
'Average amount of grant and scholarship aid awarded, income level (0-30,000',
'Number of students awarded grant and scholarship aid, income level (30,001-48,000)',
'Total amount of grant and scholarship aid awarded, income level (30,001-48,000)',
'Average amount of grant and scholarship aid awarded, income level (30,001-48,000)',
'Number awarded grant and scholarship aid, income level (48,001-75,000)',
'Total amount of grant and scholarship aid awarded, income level (48,001-75,000)',
'Average amount of grant and scholarship aid awarded, income level (48,001-75,000)',
'Number awarded grant and scholarship aid, income level (75,001-110,000)',
'Total amount of grant and scholarship aid awarded, income level (75,001-110,000)',
'Average amount of grant and scholarship aid awarded, income level (75,001-110,000)',
'Number awarded grant and scholarship aid, income level (110,001 or more)',
'Total amount of grant and scholarship aid awarded, income level (110,001 or more)',
'Average amount of grant and scholarship aid awarded, income level (110,001 or more)',
'Total entering students at the undergraduate level, fall of current year',
'Student-to-faculty ratio',
'Full-time retention rate',
'Revenues - Tuition and fees, after deducting discounts and allowances',
'Revenues - Gifts, including contributions from affiliated organizations',
'Revenues - Total operating revenues',
'Revenues - Investment income',
'Revenues - Capital grants and gifts',
'Total all revenues and other additions',
'Expenses - Instruction - Current year total',
'Expenses - Academic support - Current year total',
'Expenses - Research - Current year total',
'Expenses - Student services - Current year total',
'Total expenses and other deductions',
'Discounts and allowances applied to tuition and fees',
'Discounts and allowances applied to sales & services of auxiliary enterprises',
'Total discounts and allowances',
'Total current assets',
'Long term debt',
'Value of endowment assets at the beginning of the fiscal year',
'Value of endowment assets at the end of the fiscal year',
"Revised bachelor's degree-seeking cohort, (cohort year - current year - 8)",
"4-year Graduation rate - bachelor's degree within 100% of normal time",
"6-year Graduation rate - bachelor's degree within 150% of normal time",
'Fall Enrollment - Residents - American Indian or Alaska Native total',
'Fall Enrollment - Residents - Asian total',
'Fall Enrollment - Residents - Black or African American total',
'Fall Enrollment - Residents - Hispanic total',
'Fall Enrollment - Residents - Native Hawaiian or Other Pacific Islander total', 
'Fall Enrollment - Residents - White total',
'Fall Enrollment - Residents - Two or more races total',
'Fall Enrollment - Nonresident alien total',
'Fall Enrollment - Race/ethnicity unknown total']

college.tail()
#len(college.columns)

#convert all data type to float
college = college.convert_objects(convert_numeric=True)

#Correlation with heat map
import seaborn as sns
import matplotlib.pyplot as plt 
plt.figure(figsize=(15,10))
sns.heatmap(college[["Total current assets","Long term debt","Student-to-faculty ratio"]].corr(),annot=True,cmap='summer')
