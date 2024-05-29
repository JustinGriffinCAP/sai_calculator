import streamlit as st
import numpy as np
import pandas as pd
#saiLogo = 'C:\\Users\\Justin Griffin\\Documents\\CollegeAidPro\\VS_Code\\SAI_Calc.jpg'
#capLogo = 'C:\\Users\\Justin Griffin\\Documents\\CollegeAidPro\\VS_Code\\CAP_logo.png'
#st.image('CAP_logo.png')

#SAI Explanation
# Click here to learn more about how SAI is calculated
st.header("College Aid Pro's Student Aid Index Calculator")
st.subheader("Education")


tab1, tab2 = st.tabs(["What is the Student Aid Index?",'How is the Student Aid Index calculated?'])

with tab1:
     st.text("The Student Aid Index.......")
with tab2:
     st.text("SAI is calculated by taking the Parent Contribution from income plus........")
     #st.image('SAI_Calc.jpg')


#st.sidebar.radio('test',['Household Information','Income','Assets','Results'])

st.subheader("Family Information")
tab1, tab2, tab3 = st.tabs(["Household Info","Income","Assets"])
                   
with tab1:
    f_size = st.slider("Family Size",2,10)
    m_status = st.selectbox("Marital Status",("Married","Single","Divorced/Separated"))
    state = st.selectbox("State of Residency",("AK","AL","AR","AZ","CA"))
    students = st.checkbox("Will you have multiple students in college?")
    if students:
         multiple_students = st.slider("How many students will be attending college next year?",2,10)

with tab2:
    
    #Married
    if m_status=="Married":
               m_agi = st.slider("Parents Adjusted Gross Income",0,500000,50000,5000)
               m_tax =  st.slider("Income Tax Paid",0,100000,5000,1000)
               m_untaxed = st.slider("Untaxed Income Earned",0,250000,0,1000)

    #Single
    if m_status=="Single":
        s_agi = st.number_input("Parent Adjusted Gross Income")
        s_tax =  st.number_input("Income Tax Paid")
        s_untaxed = st.number_input("Untaxed Income Earned")

    #Divorced/Separated
    if m_status=="Divorced/Separated":
         st.subheader("Custodial Parent")
         
         d_agi = st.number_input("Custodial Parent Adjusted Gross Income")
         d_tax =  st.number_input("Custodial Income Tax Paid")
         d_untaxed = st.number_input("Custodial Untaxed Income Earned")  

         st.subheader("Non-Custodial Parent")      
         d_agi_2 = st.number_input("Non-Custodial Parent Adjusted Gross Income")
         d_tax_2 =  st.number_input("Non-Custodial Income Tax Paid")
         d_untaxed_2 = st.number_input("Non-Custodial Untaxed Income Earned")

with tab3:
     #Married 
     if m_status=="Married":
          m_cash =  st.slider("Cash, Checkings, and Savings",0,250000,15000,5000)
          m_investments = st.slider("Investments",0,250000,5000,5000)
          m_equity = st.slider("Home Equity",0,2000000,250000,10000)
     #Single
     if m_status=="Single":
          s_cash =  st.number_input("Cash, Checkings, and Savings")
          s_investments = st.number_input("Investments")
          s_equity = st.number_input("Home Equity")
     #Divorced/Separated
     if m_status=="Divorced/Separated":
          st.subheader("Custodial Parent")
          d_cash =  st.number_input("Cash, Checkings, and Savings ")
          d_investments = st.number_input("Investments ")
          d_equity = st.number_input("Home Equity ")
          st.subheader("Non-Custodial Parent")
          d_cash_2 =  st.number_input("Cash, Checkings, and Savings")
          d_investments_2 = st.number_input("Investments")
          d_equity_2 = st.number_input("Home Equity")



# Notes
## Change slider color https://discuss.streamlit.io/t/how-to-change-st-sidebar-slider-default-color/3900/5


st.header("Ready for your Federal and Institutional SAI calculation? Simply input your email below.")
st.text_input("Email:")
