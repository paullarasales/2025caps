import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class StudyDurationModel:
    def __init__(self):
        self.model = LinearRegression()
        self._train_model()

    def _train_model(self):
        data = {
            'difficulty': [1, 2, 3, 4],
            'duration': [1, 1.5, 2, 3]
        }
        df = pd.DataFrame(data)

        X = df[['difficulty']]
        y = df['duration']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        self.model.fit(X_train, y_train)
    
    def predict_duration(self, difficulty):
        input_data = pd.DataFrame({'difficulty': [difficulty]})
        return self.model.predict(input_data)[0]