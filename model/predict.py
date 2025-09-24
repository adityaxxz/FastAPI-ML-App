import pickle
import pandas as pd

#importing ml model...
with open('model/model.pkl','rb') as f:
    model = pickle.load(f)

MODEL_VERSION = '1.0.0'   #generally comes from MLFLow


def predict_output(user_input: dict):
    
    input_df = pd.DataFrame([user_input])

    prediction = model.predict(input_df)[0]

    return prediction
