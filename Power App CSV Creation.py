#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv


# In[34]:


#new FY
fiscalyear = "23"
nextYear = "24"

ty = 'FY'+fiscalyear
ny = 'FY'+nextYear

#open a new csv file to write to that is empty
with open('FY23List.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    
    rowHeaders = ['Created Date','Title',
                  'How many incremental HC does this investment include?', 
                  'Is this investment stated on the SOB slide in the QBC deck',
                  'IOE Decision Cycle',
                  'A16 Area',
                  'Geo',
                  'Investment Type',
                  'Corp Decision',
                  'Investment Description',
                  'Solution Area - Product',
                  'Segment',
                  'Is this a request matching funds already approved?',
                  'Will Spend and/or Revenue Continue into FY'+nextYear+'?',
                  ty+'-Q1 People Opex',
                  ty+'-Q2 People Opex',
                  ty+'-Q3 People Opex',
                  ty+'-Q4 People Opex',
                  
                  ty+'-Q1 People COGS',
                  ty+'-Q2 People COGS',
                  ty+'-Q3 People COGS',
                  ty+'-Q4 People COGS',
                  
                  ty+'-Q1 Marketing',
                  ty+'-Q2 Marketing',
                  ty+'-Q3 Marketing',
                  ty+'-Q4 Marketing',
                  
                  ty+'-Q1 ECIF',
                  ty+'-Q2 ECIF',
                  ty+'-Q3 ECIF',
                  ty+'-Q4 ECIF',
                  
                  ty+'-Q1 External Resources',
                  ty+'-Q2 External Resources',
                  ty+'-Q3 External Resources',
                  ty+'-Q4 External Resources',
                  
                  ty+'-Q1 RDO',
                  ty+'-Q2 RDO',
                  ty+'-Q3 RDO',
                  ty+'-Q4 RDO',
                  
                  ty+'-Q1 Rev Adjustments',
                  ty+'-Q2 Rev Adjustments',
                  ty+'-Q3 Rev Adjustments',
                  ty+'-Q4 Rev Adjustments',
                  
                  ty+'-Q1 Projected Revenue',
                  ty+'-Q2 Projected Revenue',
                  ty+'-Q3 Projected Revenue',
                  ty+'-Q4 Projected Revenue',
                  
                  ny+'-Q1 People Opex',
                  ny+'-Q2 People Opex',
                  ny+'-Q3 People Opex',
                  ny+'-Q4 People Opex',
                  
                  ny+'-Q1 People COGS',
                  ny+'-Q2 People COGS',
                  ny+'-Q3 People COGS',
                  ny+'-Q4 People COGS',
                  
                  ny+'-Q1 Marketing',
                  ny+'-Q2 Marketing',
                  ny+'-Q3 Marketing',
                  ny+'-Q4 Marketing',
                  
                  ny+'-Q1 ECIF',
                  ny+'-Q2 ECIF',
                  ny+'-Q3 ECIF',
                  ny+'-Q4 ECIF',
                  
                  ny+'-Q1 External Resources',
                  ny+'-Q2 External Resources',
                  ny+'-Q3 External Resources',
                  ny+'-Q4 External Resources',
                  
                  ny+'-Q1 RDO',
                  ny+'-Q2 RDO',
                  ny+'-Q3 RDO',
                  ny+'-Q4 RDO',
                  
                  ny+'-Q1 Rev Adjustments',
                  ny+'-Q2 Rev Adjustments',
                  ny+'-Q3 Rev Adjustments',
                  ny+'-Q4 Rev Adjustments',
                  
                  ny+'-Q1 Projected Revenue',
                  ny+'-Q2 Projected Revenue',
                  ny+'-Q3 Projected Revenue',
                  ny+'-Q4 Projected Revenue',
                  
                  ty+'-Q1 Approved People Opex',
                  ty+'-Q2 Approved People Opex',
                  ty+'-Q3 Approved People Opex',
                  ty+'-Q4 Approved People Opex',
                  
                  ty+'-Q1 Approved People COGS',
                  ty+'-Q2 Approved People COGS',
                  ty+'-Q3 Approved People COGS',
                  ty+'-Q4 Approved People COGS',
                  
                  ty+'-Q1 Approved Marketing',
                  ty+'-Q2 Approved Marketing',
                  ty+'-Q3 Approved Marketing',
                  ty+'-Q4 Approved Marketing',
                  
                  ty+'-Q1 Approved ECIF',
                  ty+'-Q2 Approved ECIF',
                  ty+'-Q3 Approved ECIF',
                  ty+'-Q4 Approved ECIF',
                                    
                  ty+'-Q1 Approved External Resources',
                  ty+'-Q2 Approved External Resources',
                  ty+'-Q3 Approved External Resources',
                  ty+'-Q4 Approved External Resources',
                  
                  ty+'-Q1 Approved RDO',
                  ty+'-Q2 Approved RDO',
                  ty+'-Q3 Approved RDO',
                  ty+'-Q4 Approved RDO',
                  
                  ty+'-Q1 Approved Rev Adjustments',
                  ty+'-Q2 Approved Rev Adjustments',
                  ty+'-Q3 Approved Rev Adjustments',
                  ty+'-Q4 Approved Rev Adjustments',
                  
                  ty+'-Q1 Planned Revenue (for Approved Spend)',
                  ty+'-Q2 Planned Revenue (for Approved Spend)',
                  ty+'-Q3 Planned Revenue (for Approved Spend)',
                  ty+'-Q4 Planned Revenue (for Approved Spend)',
                  
                  ny+'-Q1 Approved People Opex',
                  ny+'-Q2 Approved People Opex',
                  ny+'-Q3 Approved People Opex',
                  ny+'-Q4 Approved People Opex',
                  
                  ny+'-Q1 Approved People COGS',
                  ny+'-Q2 Approved People COGS',
                  ny+'-Q3 Approved People COGS',
                  ny+'-Q4 Approved People COGS',
                  
                  ny+'-Q1 Approved Marketing',
                  ny+'-Q2 Approved Marketing',
                  ny+'-Q3 Approved Marketing',
                  ny+'-Q4 Approved Marketing',
                  
                  ny+'-Q1 Approved ECIF',
                  ny+'-Q2 Approved ECIF',
                  ny+'-Q3 Approved ECIF',
                  ny+'-Q4 Approved ECIF',

                  ny+'-Q1 Approved External Resources',
                  ny+'-Q2 Approved External Resources',
                  ny+'-Q3 Approved External Resources',
                  ny+'-Q4 Approved External Resources',
                  
                  ny+'-Q1 Approved RDO',
                  ny+'-Q2 Approved RDO',
                  ny+'-Q3 Approved RDO',
                  ny+'-Q4 Approved RDO',

                  ny+'-Q1 Approved Rev Adjustments',
                  ny+'-Q2 Approved Rev Adjustments',
                  ny+'-Q3 Approved Rev Adjustments',
                  ny+'-Q4 Approved Rev Adjustments',

                  ny+'-Q1 Planned Revenue (for Approved Spend)',
                  ny+'-Q2 Planned Revenue (for Approved Spend)',
                  ny+'-Q3 Planned Revenue (for Approved Spend)',
                  ny+'-Q4 Planned Revenue (for Approved Spend)',

                 ]
    
    thewriter.writerow(rowHeaders)
    


# In[ ]:




