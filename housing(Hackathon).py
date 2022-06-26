#!/usr/bin/env python
# coding: utf-8

# In[77]:


import numpy as np
import pandas as pd


# In[80]:


bostonHouse=pd.read_csv("housing.csv")


# In[81]:


bostonHouse


# In[82]:


b=bostonHouse


# In[83]:


b


# In[84]:


b.head()


# In[85]:


b.tail()


# In[86]:


b["ST_NAME"].unique()


# In[ ]:





# In[104]:


b.isnull()


# In[105]:


b.isnull().sum()


# In[134]:


b1=b.drop(['CM_ID','U_AC','U_INT_FIN','U_INT_CND','U_VIEW','U_BTH_STYLE3','U_BTH_STYLE2','U_BTH_STYLE','U_HALF_BTH','U_KITCH_TYPE','U_KITCH_STYLE','U_HEAT_TYP','S_EXT_FIN','S_EXT_CND','S_UNIT_COM','S_UNIT_RC'],axis=1)


# In[135]:


b1.isnull().sum()


# In[226]:


b1=b.drop(['S_BLDG_STYL','S_UNIT_RES','UNIT_NUM','U_BTH_STYLE2','U_BTH_STYLE3','U_KITCH_TYPE','U_KITCH_STYLE','U_BTH_STYLE','U_HEAT_TYP','U_AC','U_CORNER','U_ORIENT','U_INT_CND','U_INT_FIN','U_VIEW','CM_ID','S_UNIT_RC','S_UNIT_COM','S_NUM_BLDG','R_VIEW','R_INT_FIN','R_INT_CND','S_EXT_FIN','S_EXT_CND','R_FPLACE','R_EXT_CND','R_OVRALL_CND','R_KITCH_STYLE3','R_HEAT_TYP','R_AC','R_KITCH','R_KITCH_STYLE','R_KITCH_STYLE2','R_BTH_STYLE','R_BTH_STYLE2','R_BTH_STYLE3','R_BDRMS','R_FULL_BTH' ,'R_HALF_BTH','R_ROOF_TYP' ,'ZIPCODE','R_EXT_FIN','R_TOTAL_RMS','U_TOT_RMS','STRUCTURE_CLASS','R_BLDG_STYL','ST_NAME_SUF'],axis=1)


# In[227]:


b1


# In[228]:


b1.isnull().sum()


# In[258]:


avg_fplace=np.mean(b1['U_FPLACE'])
avg_fplace


# In[259]:


b1['U_FPLACE'].fillna(avg_fplace,inplace=True)


# In[260]:


avg_halfb=np.mean(b1['U_HALF_BTH'])
avg_halfb


# In[261]:


b1['U_HALF_BTH'].fillna(avg_fplace,inplace=True)


# In[262]:


avg_fullb=np.mean(b1['U_FULL_BTH'])
avg_fullb


# In[263]:


b1['U_FULL_BTH'].fillna(avg_fullb,inplace=True)


# In[264]:


avg_drms=np.mean(b1['U_BDRMS'])
avg_drms


# In[265]:


b1['U_BDRMS'].fillna(avg_drms,inplace=True)


# In[266]:


avg_park=np.mean(b1['U_NUM_PARK'])
avg_park


# In[267]:


b1['U_NUM_PARK'].fillna(avg_park,inplace=True)


# In[268]:


avg_floor=np.mean(b1['U_BASE_FLOOR'])
avg_floor


# In[269]:


b1['U_BASE_FLOOR'].fillna(avg_floor,inplace=True)


# In[270]:


avg_numfloor=np.mean(b1['NUM_FLOORS'])
avg_numfloor


# In[271]:


b1['NUM_FLOORS'].fillna(avg_numfloor,inplace=True)


# In[272]:


avg_area=np.mean(b1['LIVING_AREA'])
avg_area


# In[273]:


b1['LIVING_AREA'].fillna(avg_area,inplace=True)


# In[274]:


avg_garea=np.mean(b1['GROSS_AREA'])
avg_garea


# In[275]:


b1['GROSS_AREA'].fillna(avg_garea,inplace=True)


# In[276]:


avg_remod=np.mean(b1['YR_REMOD'])
avg_remod


# In[277]:


b1['YR_REMOD'].fillna(avg_remod,inplace=True)


# In[278]:


avg_built=np.mean(b1['YR_BUILT'])
avg_built


# In[279]:


b1['YR_BUILT'].fillna(avg_built,inplace=True)


# In[280]:


avg_land=np.mean(b1['LAND_SF'])
avg_land


# In[281]:


b1['LAND_SF'].fillna(avg_land,inplace=True)


# In[282]:


b1.isnull().sum()


# In[283]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()


# In[284]:


b1


# In[321]:


b2=b1.drop(['ST_NAME','LU','OWN_OCC','OWNER','MAIL_ADDRESS','MAIL_ADDRESSEE','MAIL CS'],axis=1)


# In[331]:


b2

