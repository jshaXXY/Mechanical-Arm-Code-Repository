from joblib import load
import numpy as np

loaded_classifier = load('model.joblib')
loaded_label_encoder = load('label_encoder.joblib')

# 定义函数来预测颜色
def predict_color(rgb_value):
    rgb_value = rgb_value.astype(np.uint8)
    color_code = loaded_classifier.predict([rgb_value])[0]
    return loaded_label_encoder.inverse_transform([color_code])[0]
