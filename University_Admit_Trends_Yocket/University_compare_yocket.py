
# ######################################## #
# ###### University Admission Trends ##### #
# ######################################## #

# ## Fetch data from the website: (DATA SCRAPPING)

import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen
import pandas as pd
import matplotlib.pyplot as plt

def data_wrangling():
    li = []      # Defining lists
    li2 = []
    txt = ''
     
    for div in soup.find_all('div', class_ = 'panel panel-warning'):
        txt = div.text.strip('\n')
        li.append(txt)
   
    for i in li:
        new = i.split('\n')
        li2.append(new)
    
    li = []
    for i in li2:
        li.append([x for x in i if x not in ('','GRE','TOEFL','UNDERGRAD','WORK EX','IELTS','TOEFL/IELTS')])
    return li

# ## Page indices of yocket.com to be taken into considertion
num = [[48,21,15,1],[22,3,10,1],[10,3,7,1],[4,2,2,1],[26,14,17,1],[31,9,17,1],[38,14,14,1],[3,2,2,1]]

# ## Sample of 8 universities selected
url = ["https://yocket.in/applications-admits-rejects/248-arizona-state-university/",
       "https://yocket.in/applications-admits-rejects/44-texas-a-and-m-university-college-station/",
       "https://yocket.in/applications-admits-rejects/613-rutgers-university-new-brunswick/",
       "https://yocket.in/applications-admits-rejects/31946-george-mason-university/",
       "https://yocket.in/applications-admits-rejects/135-northeastern-university/",
       "https://yocket.in/applications-admits-rejects/129-state-university-of-new-york-at-stony-brook/",
       "https://yocket.in/applications-admits-rejects/124-state-university-of-new-york-at-buffalo/",
       "https://yocket.in/applications-admits-rejects/773-university-of-virginia/"]
univ = ["Arizona State University",
        "Texas A&M University",
        "Rutgers University, New Brunswick",
        "George Mason University",
        "Northeastern University",
        "State University of New York, Stony Brook",
        "State University of New York, Buffalo",
        "University of Virginia"]
stat = ['Applied','Admit','Reject','']
data = []
li = []
for i in range(len(url)):
    print("\n\n-------------------------------------------------------------------------------\n",univ[i],":")
    for statuspage in range(1,4):
        print("\n",stat[statuspage-1],":")
        for sitepage in range(1,num[i][statuspage-1]):
            print(sitepage, end=" ")
            siteurl = url[i]+str(statuspage)+"?page="+ str(sitepage)
            req = Request(siteurl, headers={'User-Agent': 'Mozilla/5.0'})
            sauce = urlopen(req).read()
            soup = bs.BeautifulSoup(sauce,'lxml')
            li = data_wrangling()
            data += li
print("\n",data)


# ## Convert csv to a Pandas DataFrame:
df = pd.DataFrame(data)
df.columns = ['name','university', 'term','status','gre','toefl_ilets','cgpa','work_ex']
#df = df.drop('extra', 1)    # 0 for row, 1 for column
df.to_csv('yocket_data.csv')
df


# ## Data Wrangling: 
# ### Convert 'strings' to 'floating point' numbers for calculations
df = pd.read_csv('yocket_data.csv')

def score_conv(df):
    ind = 0
    gre = []
    new_gre = []
    gre = df.gre.tolist()
    for i in gre:
        if i == 'N.A. ':
            i = i.replace('N.A. ','310')
        elif i == 'NA':
            i = i.replace('NA','100')
        new_gre.append(int(i.replace(' ','')))

    df.gre = new_gre
    toefl = []
    new_toefl = []
    toefl = df.toefl_ilets.tolist()
    for i in toefl:
        if i == 'N.A. ':
            i = i.replace('N.A. ','100')
        elif i == 'NA':
            i = i.replace('NA','100')
        elif i == 'N.A.':
            i = i.replace('N.A.','100')
        
        i = float(i.replace(' ',''))
        if i<10.0:
            i = 12*i
        if i == 0.0:
            i = 100
        new_toefl.append(i)
    df.toefl_ilets = new_toefl
    cgpa = []
    new_cgpa = []
    cgpa = df.cgpa.tolist()
    for i in cgpa:
        if i == 'N.A. ':
            i = i.replace('N.A. ','8.0')
        elif i == 'NA':
            i = i.replace('NA','8.0')
        elif i == 'N.A.':
            i = i.replace('N.A.','8.0')
        else:
            i = i.replace(' CGPA','')
            i = i.replace('CGPA','')
            i = i.replace(' %','')
            i = i.replace('%','')
            i = float(i)
            if i>10.0:
                i=i/10.0
            new_cgpa.append(i)
    df.cgpa = new_cgpa
    return df

df1 = score_conv(df)


# ### Put the pre-processed data into a new CSV file:
df1.to_csv('yocket_data_new.csv')


# ### Extract data only for the years 2016 and 2017:
# #### (To get the latest trends)
df1 = df[(df.term=='Fall 2017 ') | (df.term=='Fall 2016 ')]
df1.status.value_counts()


# ## Extracting data for Applied, Admits and Rejects separately:
status = ['Admit','Reject','Applied']
univ_list = ['Arizona State University Computer Science','Texas A&M University, College Station Computer Science',
             'Rutgers University - New Brunswick Computer Science','George Mason University Computer Science',
             'Northeastern University Computer Science','State University of New York at Stony Brook Computer Science',
             'State University of New York at Buffalo Computer Science','University of Virginia Computer Science']

#asu_reject,tamu_reject,rutgers_reject,gmu_reject,neu_reject,stony_reject,buffalo_reject,uva_reject = pd.DataFrame(df1)
univ_admit = ['asu_admit','tamu_admit','rutgers_admit','gmu_admit','neu_admit','stony_admit','buffalo_admit','uva_admit']
univ_reject = ['asu_reject','tamu_reject','rutgers_reject','gmu_reject','neu_reject','stony_reject','buffalo_reject','uva_reject']
univ_applied = ['asu_applied','tamu_applied','rutgers_applied','gmu_applied','neu_applied','stony_applied','buffalo_applied','uva_applied']
for i in status:
    for j in range(len(univ_list)-1):
        if i=='Admit':
            univ_admit[j] = df1[(df1.status==i) & (df1.university==univ_list[j])]
        elif i=='Reject':
            univ_reject[j] = df1[(df1.status==i) & (df1.university==univ_list[j])]
        elif i == 'Applied':
            univ_applied[j] = df1[(df1.status==i) & (df1.university==univ_list[j])]


# ## Plot graphs for each university:
for i in range(len(univ_list)-1):
    
    total = 0
    total = univ_admit[i].gre.count() + univ_reject[i].gre.count() + univ_applied[i].gre.count()
    print("\n\n\n",univ_list[i]," - FALL 2016-2017 ADMIT TRENDS:\n--------------------------------------------------------\n")
    print("APPLIED:",univ_applied[i].gre.count())
    print("ADMITS:",univ_admit[i].gre.count())
    print("REJECTS:",univ_reject[i].gre.count())
    print("--------------------\nTOTAL: ",total,"\n")
    print("Mean GRE for admits:",int(univ_admit[i].gre.mean()),"\t\t\t\t","Mean TOEFL for admits:",int(univ_admit[i].toefl_ilets.mean()),"\n")
    print("Minimum GRE for admits:",int(univ_admit[i].gre.min()),"\t\t\t\t","Minimum TOEFL for admits:",int(univ_admit[i].toefl_ilets.min()),"\n")
    print("Maximum GRE for admits:",int(univ_admit[i].gre.max()),"\t\t\t\t","Mmaximum TOEFL for admits:",int(univ_admit[i].toefl_ilets.max()),"\n")

    fig = plt.figure(figsize=(8,6))
    bins = [300,305,310,320,325,330,335,340]
    
    ax1 = fig.add_subplot(221)
    ax1.hist(univ_admit[i].gre.tolist(),bins,histtype='bar',rwidth=0.5,color='g',alpha=1,label='Admitted')
    ax1.hist(univ_applied[i].gre.tolist(),bins,histtype='bar',rwidth=0.5,color='b',alpha=0.2, label='Applied')
    ax1.set_title("Admits based on GRE Fall' 16-17")
    ax1.set_xlabel('Gre Score Range')
    ax1.set_ylabel('No. of students admitted')
    ax1.legend()

    ax2 = fig.add_subplot(222)
    ax2.hist(univ_reject[i].gre.tolist(),bins,histtype='bar',rwidth=0.5,color='b',alpha=1, label='Rejected')
    ax2.hist(univ_applied[i].gre.tolist(),bins,histtype='bar',rwidth=0.5,color='r',alpha=0.2, label='Applied')
    ax2.set_title("Rejects based on GRE Fall' 16-17")
    ax2.set_xlabel('Gre Score Range')
    ax2.set_ylabel('No. of students admitted')
    ax2.legend()
    
    ax3 = fig.add_subplot(223)
    ax3.scatter(univ_admit[i].gre.tolist(),univ_admit[i].toefl_ilets.tolist(),color = 'g',s = 5)
    ax3.set_title("Admits [GRE vs TOEFL]")
    ax3.set_xlabel('GRE')
    ax3.set_ylabel('TOEFL')
    
    ax4 = fig.add_subplot(224)
    ax4.scatter(univ_reject[i].gre.tolist(),univ_reject[i].toefl_ilets.tolist(),color = 'r',s = 5)
    ax4.set_title("Rejects [GRE vs TOEFL]")
    ax4.set_xlabel('GRE')
    ax4.set_ylabel('TOEFL')
    
    
    fig.tight_layout()
    plt.show()
    print("______________________________________________________________________________________________________")



