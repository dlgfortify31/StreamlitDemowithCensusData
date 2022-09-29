#import relevant packages
import pandas as pd
import streamlit as st  
import numpy as np
import base64
import os
import time
#Set the page layout for the application
st.set_page_config(layout="wide")
#Create 3 lines of white space
st.write("")
st.write("")
st.write("")
#Header and Subheader
st.header("Streamlit Example for DASP")
st.subheader("Census Data Example")

#Add in css file
with open('C:/Users/Gibson.Drake.L/Documents/myformat.css') as f:
    st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html= True)
#This is a streamlit form which sends batch submission of arguments 
with st.form(key = "Example For DASP"):
    with st.sidebar:
        #Header
        st.sidebar.header("Subset Table")
        #Text input for the State
        title = st.sidebar.text_input('State', '')
        #Dropdown menu to select if you want the whole file or a subset based on industry, race ethnicity,and firm sizes
        vars_name = st.sidebar.selectbox("Include Variables", ('All', 'Industry', 'Race', 'Ethnicity', 'Firm Sizes'))
        #If industry is selected above then select the relevant label
        if vars_name == 'Industry':
            ind_title = st.sidebar.selectbox('Industry', ('Accommodation and Food Services',
       'Administrative and Support and Waste Management and Remediation Services',
       'Agriculture, Forestry, Fishing and Hunting', 'All NAICS Sectors',
       'Arts, Entertainment, and Recreation', 'Construction',
       'Finance and Insurance', 'Information',
       'Management of Companies and Enterprises',
       'Mining, Quarrying, and Oil and Gas Extraction',
       'Other Services (except Public Administration)',
       'Professional, Scientific, and Technical Services',
       'Public Administration', 'Retail Trade',
       'Transportation and Warehousing', 'Utilities', 'Wholesale Trade'))
       #If race is selected above then select the relevant label
        if vars_name == 'Race':    
            r_title = st.sidebar.selectbox('Race', ('All Races', 'American Indian or Alaska Native Alone',
       'Asian Alone', 'Black or African American Alone',
       'Native Hawaiian or Other Pacific Islander Alone',
       'Two or More Race Groups', 'White Alone'))
        #If ethnicity is selected above then select the relevant label
        if vars_name == 'Ethnicity':
            eth_title = st.sidebar.selectbox('Ethinicity', ('All Ethnicities', 'Hispanic or Latino', 'Not Hispanic or Latino'))
        #If firm sizes is selected above then select the relevant label
        if vars_name == 'Firm Sizes':
            fs_title = st.sidebar.selectbox('Firm Sizes', ('0-19 Employees', '20-49 Employees', '250-499 Employees',
       '50-249 Employees', '500+ Employees', 'All Firm Sizes'))
        #Creates the submit button
        render_button = st.form_submit_button('Search')
#Cache the download link functions 
@st.cache
#Create the download link for the data file
def get_table_download_link_csv(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href = "data:file/csv;base64,{b64}" download="{title}.csv">Download File</a>'
    return href

#Submit the arguments in a batch to output the subset of data
if render_button:
   #Read in the csv file
    test = pd.read_csv("C:/Users/Gibson.Drake.L/Downloads/qwi_d2aadf847dfe4ffb9b9aa61a6eaf66a3/qwi_d2aadf847dfe4ffb9b9aa61a6eaf66a3.csv")
    #Create a markdown to display the state and variable the file will be subset on 
    st.markdown('{} {}'.format(title, vars_name),unsafe_allow_html=True)
    #Create a unique list for each column that has a variable label of interest
    valid_values = np.unique(test['geography_label.value']).tolist()
    valid_values_ind = np.unique(test['industry_label.value']).tolist()
    valid_values_r = np.unique(test['race_label.value']).tolist()
    valid_values_eth =np.unique(test['ethnicity_label.value'])
    valid_values_fs =np.unique(test['firmsize_label.value'])
    #Create a data frame from the state used in the text input
    output = test[test['geography_label.value'].str.startswith(title)]
    
    #If statement to show that if the state is in the geography label column then output the new data frame. 
    #If it is not, throw an error
    if  len(output) < 1:
        st.error("Invalid State. Please try again.")
    else:
        #If the state is in the file and the variable selected has a valid label, the file will be subset and 
        #outputted
        if title in valid_values :
            if vars_name == 'Industry' and ind_title in valid_values_ind:
                st.write(ind_title)
                newout = output[['periodicity_label.value','seasonadj_label.value',
             'geo_level_label.value','geography_label.value',
             'industry_label.value','ownercode_label.value',
             'sex_label.value','agegrp_label.value','race_label.value',
             'ethnicity_label.value', 'education_label.value',
             'firmage_label.value','firmsize_label.value','year',
             'quarter', 'Emp', 'HirA', 'HirN','HirR', 'Sep',
             'HirAS', 'TurnOvrS', 'FrmJbGn', 'FrmJbLs', 'FrmJbC',
             'HirAEndRepl', 'EarnS', 'EarnBeg', 'EarnSepS',
             'Payroll', 'sEmp', 'sHirA', 'sHirN', 'sHirR',
             'sSep', 'sHirAS', 'sTurnOvrS', 'sFrmJbGn',
             'sFrmJbLs', 'sFrmJbC', 'sHirAEndRepl',
             'sEarnS', 'sEarnBeg', 'sEarnSepS', 'sPayroll']].loc[output['industry_label.value'] == ind_title]
            
            if vars_name == 'Race' and r_title in valid_values_r:
                newout = output[['periodicity_label.value','seasonadj_label.value',
            'geo_level_label.value','geography_label.value',
            'industry_label.value','ownercode_label.value',
            'sex_label.value','agegrp_label.value','race_label.value',
            'ethnicity_label.value', 'education_label.value',
            'firmage_label.value','firmsize_label.value','year',
            'quarter', 'Emp', 'HirA', 'HirN','HirR', 'Sep',
            'HirAS', 'TurnOvrS', 'FrmJbGn', 'FrmJbLs', 'FrmJbC',
            'HirAEndRepl', 'EarnS', 'EarnBeg', 'EarnSepS',
            'Payroll', 'sEmp', 'sHirA', 'sHirN', 'sHirR',
            'sSep', 'sHirAS', 'sTurnOvrS', 'sFrmJbGn',
            'sFrmJbLs', 'sFrmJbC', 'sHirAEndRepl',
            'sEarnS', 'sEarnBeg', 'sEarnSepS', 'sPayroll']].loc[output['race_label.value'] ==  r_title]
            
            if vars_name == 'Ethnicity' and eth_title in valid_values_eth:
                newout = output[['periodicity_label.value','seasonadj_label.value',
            'geo_level_label.value','geography_label.value',
            'industry_label.value','ownercode_label.value',
            'sex_label.value','agegrp_label.value','race_label.value',
            'ethnicity_label.value', 'education_label.value',
            'firmage_label.value','firmsize_label.value','year',
            'quarter', 'Emp', 'HirA', 'HirN','HirR', 'Sep',
            'HirAS', 'TurnOvrS', 'FrmJbGn', 'FrmJbLs', 'FrmJbC',
            'HirAEndRepl', 'EarnS', 'EarnBeg', 'EarnSepS',
            'Payroll', 'sEmp', 'sHirA', 'sHirN', 'sHirR',
            'sSep', 'sHirAS', 'sTurnOvrS', 'sFrmJbGn',
            'sFrmJbLs', 'sFrmJbC', 'sHirAEndRepl',
            'sEarnS', 'sEarnBeg', 'sEarnSepS', 'sPayroll']].loc[output['ethnicity_label.value'] ==  eth_title]
            
            if vars_name == 'Firm Sizes' and fs_title in valid_values_fs:
                newout = output[['periodicity_label.value','seasonadj_label.value',
            'geo_level_label.value','geography_label.value',
            'industry_label.value','ownercode_label.value',
            'sex_label.value','agegrp_label.value','race_label.value',
            'ethnicity_label.value', 'education_label.value',
            'firmage_label.value','firmsize_label.value','year',
            'quarter', 'Emp', 'HirA', 'HirN','HirR', 'Sep',
            'HirAS', 'TurnOvrS', 'FrmJbGn', 'FrmJbLs', 'FrmJbC',
            'HirAEndRepl', 'EarnS', 'EarnBeg', 'EarnSepS',
            'Payroll', 'sEmp', 'sHirA', 'sHirN', 'sHirR',
            'sSep', 'sHirAS', 'sTurnOvrS', 'sFrmJbGn',
            'sFrmJbLs', 'sFrmJbC', 'sHirAEndRepl',
            'sEarnS', 'sEarnBeg', 'sEarnSepS', 'sPayroll']].loc[output['firmsize_label.value'] ==  fs_title]
            
            if vars_name == 'All':
             newout = output[['periodicity_label.value','seasonadj_label.value',
            'geo_level_label.value','geography_label.value',
            'industry_label.value','ownercode_label.value',
            'sex_label.value','agegrp_label.value','race_label.value',
            'ethnicity_label.value', 'education_label.value',
            'firmage_label.value','firmsize_label.value','year',
            'quarter', 'Emp', 'HirA', 'HirN','HirR', 'Sep',
            'HirAS', 'TurnOvrS', 'FrmJbGn', 'FrmJbLs', 'FrmJbC',
            'HirAEndRepl', 'EarnS', 'EarnBeg', 'EarnSepS',
            'Payroll', 'sEmp', 'sHirA', 'sHirN', 'sHirR',
            'sSep', 'sHirAS', 'sTurnOvrS', 'sFrmJbGn',
            'sFrmJbLs', 'sFrmJbC', 'sHirAEndRepl',
            'sEarnS', 'sEarnBeg', 'sEarnSepS', 'sPayroll']]
        else:
            #Throw an error
            st.error("Invalid phrase. Please Try Again")
    #Print out the data frame
    st.dataframe(newout)
    #print out the number of rows in the file
    st.markdown('**Number of Rows**: **{}**'.format(len(newout)), unsafe_allow_html=True)
    #Display a usable download link 
    st.markdown(get_table_download_link_csv(newout),unsafe_allow_html= True)
        
    #st.write(g)   
    #st.markdown('**State:** {} '.format(title), unsafe_allow_html= True)
    #st.dataframe(out)
    #st.write(type(g))
    #st.markdown(get_table_download_link_csv(out1),unsafe_allow_html= True)
    