#question C

import matplotlib.pyplot as plt 

Languages = ['Python', 'Java', 'C++', 'JavaScript', 'Ruby']
Popularity = [30,25,20,15,10]

plt.figure()
plt.pie(Popularity , labels=Languages, startangle=90, autopct='%1.1f%%')
plt.axis('equal')
plt.show()