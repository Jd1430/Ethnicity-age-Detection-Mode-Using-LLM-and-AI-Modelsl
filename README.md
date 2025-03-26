# 👤 Human Age, Gender, and Ethnicity Detection

This project is a **Streamlit-based web app** that detects a person's **age, gender, and ethnicity** from an uploaded image or live camera feed. It leverages **DeepFace** for facial analysis and **dlib** for facial landmarks.

## 🚀 Features
- 📸 **Upload an Image** for detection
- 🎥 **Live Camera Feed** for real-time detection
- 🏷️ **Facial Landmark Detection** using dlib
- 📜 **Downloadable JSON Report** of the analysis
- 🔍 **DeepFace-powered Predictions** for age, gender, and ethnicity

## 🛠️ Installation

Clone the repository and navigate into the project folder:

```bash
git clone https://github.com/yourusername/human-age-gender-ethnicity-detection.git
cd human-age-gender-ethnicity-detection
```

### Install Dependencies

Ensure you have **Python 3.7+** installed, then run:

```bash
pip install -r requirements.txt
```

### Download dlib Landmark Model

Download the **`shape_predictor_68_face_landmarks.dat`** file from [dlib.net](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2), extract it, and place it in the project directory.

## ▶️ Running the App

Launch the Streamlit app with:

```bash
streamlit run app.py
```

## 📂 File Structure

```
📂 human-age-gender-ethnicity-detection
│── app.py                 # Main Streamlit application
│── requirements.txt        # Dependencies
│── shape_predictor_68_face_landmarks.dat  # Dlib model (Needs to be downloaded)
```

## 🖼️ Usage

### 1️⃣ Upload an Image
- Click **Upload an Image** in the sidebar.
- Select an image (JPG/PNG/JPEG format).
- The app will analyze the image and overlay the predictions.

### 2️⃣ Live Camera Feed
- Click **Start Camera** to activate real-time detection.
- The app will process the frames and display real-time results.
- Click **Stop Camera** to end the session.

### 3️⃣ Download Report
- After analysis, a **JSON report** can be downloaded with detailed results.

## 📜 Example Output
![Screenshot 2025-03-26 142355](https://github.com/user-attachments/assets/aa8cf1cc-32c0-41f2-8c4d-ea5b6337c7a7)

![Screenshot 2025-03-26 142640](https://github.com/user-attachments/assets/fb04be00-a31e-47a5-984d-7295f520a717)

```
{
  "age": 25,
  "dominant_gender": "Male",
  "dominant_race": "Asian",
  "region": { "x": 100, "y": 50, "w": 150, "h": 150 }
}
```
## 🔗 Contact
For any questions or collaborations, feel free to reach out:
- **GitHub**: [Jd1430](https://github.com/Jd1430)
- **Email**: jayanthdevarajgowda@gmail.com

---
💡 **Contributions are welcome!** Feel free to fork this repository and submit pull requests. 🚀
