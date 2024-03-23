import pandas as pd
import matplotlib.pyplot as plt
#Reading dataset
data = pd.read_csv("C:/Users/June Gemini/library-management-system/LibraryManagementSystem/motor_data11-14lats.csv")

#Inspecting data set
print(data.head(10))

#records for 'make' and 'usage' for 'seats_num' that are more than 40
print(data[["MAKE","USAGE"]][data["SEATS_NUM"]>40])

#graph showing effective_yr on y axes and carrying capacity
data.plot(y = 'CARRYING_CAPACITY', x = 'EFFECTIVE_YR')
plt.ylabel('EFFECTIVE_YR')
plt.xlabel('CARRYING_CAPACITY')
plt.title('EFFECTIVE_YR VS CARRYING_CAPACITY')
plt.show()