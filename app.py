import sklearn
import streamlit as st
import pickle 
pickle_in = open("heart-disease.pkl","rb")
clf = pickle.load(pickle_in)

def prediction(age,sex,cp,trestbps,serum,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    prediction = clf.predict([[age,sex,cp,trestbps,serum,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if(prediction == 1):
        print("Yes, The Person has heart disease")
    else:
        print("No, The person doesn't have heart disease")
    return prediction







def main():
    st.title("Heart-Disease Predictor")
    age = st.number_input("Age")
    se = st.text_input("Sex")
    if (se=='Male'):
        sex = 1
    if(se=='Female'):
        sex = 0
    st.subheader("Chest Pain")
    st.text("1 - Typical Angina")
    st.text("2 - Atypical Angina")
    st.text("3 - Non-Anginal Pain")
    st.text("4 - Asymptomatic")
    cp = st.number_input("Enter the value of chest pain you experience")
    trestbps = st.number_input("Resting Blood Pressure")
    serum = st.number_input("Serum levels")
    fbs_levels = st.number_input("Enter the value of Fasting Blood Sugar level")
    if (fbs_levels > 120):
        fbs = 1
    else:
        fbs = 0
    st.subheader("Resting electrocardiographic results")
    st.text("0 - Normal")
    st.text("1 - Having ST-T wave abnormality")
    st.text("2 - Showing Probable or definite left ventricular hypertrophy")
    restecg = st.number_input("Enter the value of your Resting Electrocardiographic levels")
    thalach = st.number_input("Maximum Heart rate achieved")
    exan = st.text_input("Exercise Induced Angina Pain")
    if(exan == 'Yes'):
        exang = 1
    if(exan == 'No'):
        exang = 0
    oldpeak = st.number_input("ST depression induced by exercise relative to rest")
    st.subheader("Slope")
    st.text("1 - Upsloping")
    st.text("2 - Flat")
    st.text("3 - Downsloping")
    slope = st.number_input("Enter the value of the slope you experience")
    ca = st.number_input("Number of vessels coloured by Flouroscopy")
    st.subheader("Thalasemmia")
    st.text("3 = Normal")
    st.text("6 = Fixed Defect")
    st.text("7 = Reversable Defect")
    thal = st.number_input("Enter the Thalasemmia level you have")

    if st.button("Predict"):
        result = prediction(age,sex,cp,trestbps,serum,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
        if(result == 1):
            st.success("The Person has heart-disease")
        else:
            st.success("The person doesn't have heart-disease")

if __name__ =='__main__':
    main()