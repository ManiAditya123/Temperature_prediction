# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 
import pickle
import streamlit as st
import pandas as pd
 
# loading the trained model
pickle_in = open('reg.pkl', 'rb') 
reg = pickle.load(pickle_in)

 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(ambient, coolant,u_d,u_q, motor_speed, torque,i_d,stator_tooth):   
 
    # Making predictions 
    prediction = reg.predict( 
        [[ambient, coolant,u_d,u_q, motor_speed, torque,i_d,stator_tooth]])
     
    return prediction
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="padding:10px"> 
    <h1 style ="color:white;text-align:center;">Motor Temperature Prediction </h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    ambient = st.sidebar.number_input('Enter ambient temperature')
    coolant = st.sidebar.number_input("Enter coolant temperature")
    u_d = st.sidebar.number_input("Enter Voltage d-component")
    u_q = st.sidebar.number_input("Enter Voltage q-component")
    motor_speed = st.sidebar.number_input("Enter motor_speed")
    torque = st.sidebar.number_input("Enter torque")
    i_d = st.sidebar.number_input("Enter Current d-component")
    stator_tooth = st.sidebar.number_input('Enter stator_tooth temperature')     
    result =""
     

    st.write("\n\n\n")     
    dataframe=pd.DataFrame({'Ambient':[ambient],
                            'Coolant':[coolant],
                            'u_d':[u_d],
                            'u_q':[u_q],
                            'motor_speed':[motor_speed],
                            'torque':[torque],
                            'i_d':[i_d],
                            'stator_tooth':[stator_tooth]})
    st.write('Data entered is :', dataframe)
    
    st.write("\n\n\n")  
    
        # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        st.write("Result is predicted using Adaboost Regressor\n")
        result = prediction(ambient, coolant,u_d,u_q, motor_speed,torque,i_d,stator_tooth) 
        st.subheader('PM temperature is {}'.format(result))
        print(result)
     
if __name__=='__main__': 
    main()
