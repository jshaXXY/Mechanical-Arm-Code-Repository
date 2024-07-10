import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from joblib import dump

# 用于存储RGB值和标签的列表
X = []  # RGB值
y = []  # 颜色标签

# 读取文件并解析每一行
with open('RGBColorList.txt', 'r') as file:
    for line in file:
        parts = line.split()
        rgb = [int(value) for value in parts[:3]]  # 获取RGB值
        label = parts[3]  # 获取颜色标签
        X.append(rgb)
        y.append(label)

# 将列表转换为NumPy数组
X = np.array(X)
y = np.array(y)

# 将标签转换为整数编码
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=20)

# 创建并训练模型
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 预测测试集
y_pred = model.predict(X_test)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f'Model accuracy: {accuracy * 100:.2f}%')

# 保存模型和标签编码器
dump(model, 'model.joblib')
dump(label_encoder, 'label_encoder.joblib')