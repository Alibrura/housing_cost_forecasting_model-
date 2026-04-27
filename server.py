from flask import Flask, request, jsonify
import numpy as np
import pickle
import os 
import pandas as pd

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_func():
    data = request.json
    # путь модели
    model_path = data['model_path']
    # входящие данные
    input_df = pd.read_json(data['input_data'], orient='split')
    
    # преобразуем категориальные признаки
    for cat_col in ['zipcode', 'city', 'state']:
        if cat_col in input_df.columns:
            input_df[cat_col] = input_df[cat_col].astype('category')

    # поиск модели 
    if os.path.exists(model_path):
        # сериализируем модель
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        # прогнозирование цены
        prediction = model.predict(input_df)
        return jsonify({'prediction': prediction.tolist()})
    else:
        raise Exception("Модель не найдена")
    
if __name__ == '__main__':
    app.run('localhost', port=5000)