#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


tda = pd.read_excel('TDA.xlsx')


# In[3]:


#Defining The Column Names
tda.columns = ['UnpaidAmt','Ticket_No','Routing','InvoiceNoFromBDA','CC2FromBDA']


# In[4]:


# New Column to store Ticket No or PNR Values
ticket =pd.Series([])


# In[5]:


# loop to add values to ticket[i] based on the Routing and Ticket No
for i in range(len(tda)):
    if "Ticket No" in tda['Routing'][i]:
        new2 = tda['Routing'][i].replace('','')
        ticket[i] = new2[new2.find("Ticket No:")+10:]
        if ticket[i] == '          ':
            ticket[i] = 'Not Found'
        
        #ticket[i] = tda['Routing'][i][tda['Routing'][i].find("Ticket No:")+1:].split()[0]
    else:
        new1 = tda['Ticket_No'][i].replace(' ','')
        new = str(new1)
        if (len(new) == 16):
            ticket[i] = new[5:15]
        elif (len(new) == 13):
            ticket[i] = new[3:13]
        elif (len(new) == 15):
            ticket[i] = new[5:15]
        else:
            ticket[i] = "Not Found"


# In[6]:


# Add series ticket  as column to TDA
tda.insert(2, "Ticket", ticket)


# In[7]:


bda=pd.read_excel('BDA.xlsx')


# In[8]:


#Defining the column names for BDA
bda.columns = ["cc2", "Invoice_No", "TICKET", "Amount", "PNR"]


# In[9]:


tda.head()


# In[10]:


#Converting Ticket values in BDA to compare the  substrings 
for t in range(len(bda)):
    bda['TICKET'][t] = str(bda['TICKET'][t])


# In[12]:


# Comparing and Adding Fields from BDA to TDA
for j in range(len(tda)):
    pnr_ticket = tda['Ticket'][j]
    for i in range(len(bda)):
        if bda['TICKET'][i][0:10] == tda['Ticket'][j]:
            tda['CC2FromBDA'][j] = bda['cc2'][i]
            tda['InvoiceNoFromBDA'][j] = bda['Invoice_No'][i]
            break
        tda['InvoiceNoFromBDA'][j] = 'Not Found'
        tda['CC2FromBDA'][j] = 'Not Found'
        


# In[15]:


# Saving The Output in excel Format
tda.to_excel('TDA_Akash.xlsx')


# In[13]:


tda.head(+10)


# In[ ]:





# In[ ]:





# In[ ]:




