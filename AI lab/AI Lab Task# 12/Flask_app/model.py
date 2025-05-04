import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# Load data
df = pd.read_csv('cleaned-data.csv')

# Fill missing values
for col in df.columns:
    if df[col].dtype == 'O':
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].mean())

# Encode categorical columns
label_encoders = {}
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Features and target
X = df.drop('Survived', axis=1)
y = df['Survived']

# Train model
model = SVC()
model.fit(X, y)

# Define prediction function
def predict_survival(input_data):
    input_df = pd.DataFrame([input_data])
    for col, le in label_encoders.items():
        input_df[col] = le.transform(input_df[col])
    prediction = model.predict(input_df)[0]
    return 'Survived' if prediction == 1 else 'Not Survived'
