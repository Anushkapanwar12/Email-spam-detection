# 📧 Email Spam Detection using Machine Learning 

![Spam Detection Banner](https://www.easyspace.com/blog/wp-content/uploads/2019/03/spam-1.png)

<font size="1">Image Courtesy: EasySpace Blog</font>

---

## 🧩 Problem Statement

Spam or junk messages continue to flood inboxes with unwanted and sometimes malicious content. These messages can contain scams, advertisements, or phishing attempts designed to trick users.  

The goal of this project is to build a **machine learning model** that can automatically detect whether an email/message is **Spam** or **Not Spam (Ham)** using text classification.

---

## 🎯 Project Objectives

1. **Data Preprocessing:** Clean and prepare the dataset by handling missing values, duplicates, and irrelevant data.  
2. **Text Feature Engineering:** Use **TF-IDF Vectorization** to convert textual data into numerical form suitable for ML models.  
3. **Model Training:** Train a **Logistic Regression model** to identify patterns between words and message labels (spam/ham).  
4. **Model Evaluation:** Evaluate performance using **accuracy, precision, recall, and F1-score**.  
5. **Confusion Matrix Visualization:** Use `matplotlib` to visualize spam vs ham predictions.  
6. **Frontend-Backend Integration:** Build a simple **Flask web app** for real-time spam detection.  
7. **Deployment:** Make the model accessible locally via Flask.

---

## 🧠 Project Summary

This project implements a **Flask-based web application** that predicts if an entered message/email is spam.  
The model is trained on the **SMS Spam Collection Dataset** containing over 5,000 labeled messages.  

**Highlights:**  
- Used **TF-IDF vectorizer** for converting text into feature vectors.  
- Applied **Logistic Regression** for spam classification.  
- Achieved **96% accuracy** on test data.  
- Created a simple Flask app with HTML frontend for user testing.  
- Saved model as `spam_model.pkl` and `vectorizer.pkl`.

---

## ⚙️ Implementation Workflow

### Step 1: Data Preprocessing
- Removed duplicates and null values  
- Renamed columns for clarity  
- Converted spam/ham labels into binary (1 = Spam, 0 = Ham)

### Step 2: Feature Extraction
- Used `TfidfVectorizer(stop_words='english', max_df=0.7)`

### Step 3: Model Training
- Algorithm: Logistic Regression  
- Train-test split: 80%-20%

### Step 4: Evaluation
- **Accuracy:** 96.4%  
- **Precision:** 0.98  
- **Recall:** 0.86  
- **F1-Score:** 0.92  

---

## 🧾 Confusion Matrix

| Actual \ Predicted | Ham | Spam |
|--------------------|------|------|
| **Ham** | 887 | 2 |
| **Spam** | 35 | 110 |

---

## 💻 Flask Web Application

The web app allows users to input a message or email text.  
The model (`spam_model.pkl`) and vectorizer (`vectorizer.pkl`) classify it as Spam or Ham in real-time.


---

## 🚀 How to Run the Project

1. Clone or download this repository.  
2. Install dependencies:
   ```bash
   pip install flask scikit-learn joblib pandas

Run the app:
python app.py

Open in browser:
http://127.0.0.1:5000/

## 🧩 Key Insights

- Around **13–14%** of all messages in the dataset were spam, while most were normal (ham).  
- Common spam words like **“free”**, **“win”**, **“offer”**, **“click”**, and **“call now”** appeared very often in spam messages.  
- Using **TF-IDF Vectorizer**, the text data was changed into numbers so the model could understand it better.  
- The **Logistic Regression** model gave the best results with about **96% accuracy**.  
- The model can correctly identify both spam and non-spam messages most of the time.  
- A simple **Flask web app** was created to let users enter any message and instantly check if it’s spam or not.

---

## 🏁 Conclusion

This project helps to automatically detect **spam messages or emails** using **machine learning**.  
It makes our inbox safer by filtering out unwanted and fake messages.

We used **TF-IDF** to convert text into useful features and **Logistic Regression** to train the model.  
The system can now predict whether a message is **spam** or **ham (not spam)** with high accuracy.

The project also includes a **web app made with Flask**, so anyone can easily test messages in real time.  
It shows how machine learning can be used in simple, practical ways to solve real-world problems.

✨ **In short:**  
This project successfully builds a smart spam detector that helps keep your inbox **clean, safe, and spam-free!**


## 🧾 Reference  
- [Kaggle – SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)  
- [Scikit-learn](https://scikit-learn.org/)  
- [Flask Framework](https://flask.palletsprojects.com/)  
- [Python](https://www.python.org/)    


---

## 👩‍💻 Author

**Anushka Panwar**  
💌 [LinkedIn](https://www.linkedin.com/in/anushka-739195324) | [GitHub](https://github.com/Anushkapanwar12/Anushka-Panwar)
