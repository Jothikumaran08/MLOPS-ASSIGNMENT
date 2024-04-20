from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

class PredictView(APIView):
    def get(self, request):
        return Response({'message': 'All ok'}, status=status.HTTP_200_OK)

    def post(self, request):
        # Get input values from the request data
        Gender = request.data.get('Gender')
        Age = request.data.get('Age')
        Occupation = request.data.get('Occupation')
        StressLevel = request.data.get('StressLevel')

        # Check if any input value is missing
        if Gender is None or Age is None or Occupation is None or StressLevel is None:
            return Response({'error': 'One or more input values are missing'}, status=status.HTTP_400_BAD_REQUEST)

        # Convert Age and StressLevel to float
        try:
            Age = float(Age)
            StressLevel = float(StressLevel)
        except ValueError:
            return Response({'error': 'One or more input values are not valid numbers'}, status=status.HTTP_400_BAD_REQUEST)

        # Convert Gender to numeric
        Gender_numeric = 0 if Gender.lower() == 'male' else 1

        # Convert Occupation to numeric based on mapping
        occupation_mapping = {
            'Doctor': 0,
            'Engineer': 1,
            'Professor': 2,
            'Student': 3,
            'Teacher': 4,
            # Add more mappings as needed
        }
        Occupation_numeric = occupation_mapping.get(Occupation, 5)  # Default value is 5 for other occupations

        # Use LabelEncoder to encode categorical variables
        data = pd.read_csv('D:\\sleep.csv')
        le = LabelEncoder()
        data["Occupation"] = le.fit_transform(data["Occupation"])
        data["Gender"] = le.fit_transform(data["Gender"])

        # Prepare input features (assuming columns 1, 2, 3, and 7 are relevant)
        x = data.iloc[:, [1, 2, 3, 7]]
        y = data.iloc[:, [5]]

        # Train a linear regression model
        rg = LinearRegression()
        rg.fit(x, y)

        # Predict the output based on input values
        out = rg.predict([[Gender_numeric, Age, Occupation_numeric, StressLevel]])

        # Process the output
        output_hours = round(float(out[0]), 2)  # Convert to float, round to 2 decimal places
        output_formatted = f'Quality of Sleep: {output_hours} Hours'  # Format output as "Quality of Sleep: [value] Hours"

        return Response({'output': output_formatted}, status=status.HTTP_200_OK)
