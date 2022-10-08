import time
import pickle
import numpy as np
import streamlit as st

st.title("Welcome....!")

with st.sidebar:
    st.header("Introduction:")
    st.write("This is a Machine Learning Project to Detect Heart Disease using Logstic Regression.")
    st.header("Conclusion")
    st.write("This Algorithm performed well, Here we had only 303 rows, it very less data to train a model on then too our model performed uite well we achieved above 85% accuracy on trainig data and 82% in testing data without getting overfitted.")
    st.write("Logistic regression provides a useful means for modelling the dependence of a binary response variable on one or more explanatory variables, where the latter can be either categorical or continuous. The fit of the resulting model can be assessed using a number of methods.")
    st.write("We created custom input and tested it, in Building Predictive System section it also worked properly.")

model = pickle.load(open('model.sav', 'rb'))
    
st.subheader("Select all the values and get the prediction")

age = st.slider('How old are you?', 1, 110, 25)

gender = st.radio("What's your gender",  ('Male', 'Female', 'Perfer not to specify'), index=2)

chest_pain = st.slider("What's the level of chest pain ?", 1, 4, 1)

bp = st.slider("What's the rest bp?",90,240,110)

chol = st.slider("What's the cholesterol level ?", 100,500,200)

fbs = st.radio("Do you have Fasting Blood Sugar?", ("Yes", "No"),index=1)

rest_ecg = st.slider("What's the Rest ECG Level?",1,3,1)

max_hr = st.slider("What's the Max hr level?",0,200,130)

exang = st.radio(" What's resting electrocardiographic result?",("Yes","No"),index=1)

oldpeek = st.slider(" What's ST depression induced by exercise-relative to rest",1,6,2)

slope = st.slider("What's the slope level",1,3,1)

ca = st.slider("What's the ca level",1,2,1)

thal = st.slider("What's the level of Thalassemia?",1,3,1)

prediction = st.radio("Are the above values provided correct?",
                      ("Yes","No"),index=1)

with st.spinner('Making the prediction...'):
    if prediction == "Yes":
        time.sleep(3)
        input_data=(68,1,4,144,193,1,0,1,0,3.4,2,2.0,3.0)
        #changing input tuple to numpy array
        data=np.asarray(input_data)
        #reshaping the numpy array as we are predicting for only  on instance
        new_data=data.reshape(1,-1)
        # predicting on new data
        new_predict=model.predict(new_data)
        # Printing predicting value
        if(new_predict[0]==0):
            st.success('The Person does not have Heart Disease!', icon="✅")
        else:
            st.error('The Person have Heart Disease')
        