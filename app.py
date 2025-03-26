import streamlit as st 
import cv2
import numpy as np
from deepface import DeepFace
from PIL import Image, ImageDraw, ImageFont
import dlib
import os
import json

st.set_page_config(page_title="Ethnicity & Age Detection", layout="wide")
st.title("👤 Human Age, Gender, and Ethnicity Detection")

# Load dlib face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
landmark_model_path = "shape_predictor_68_face_landmarks.dat"

if os.path.exists(landmark_model_path):
    predictor = dlib.shape_predictor(landmark_model_path)
else:
    st.warning("⚠️ Landmark model not found. Please download 'shape_predictor_68_face_landmarks.dat' from http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2 and place it in the script directory.")
    predictor = None

# Function to analyze image
def analyze_image(image):
    try:
        result = DeepFace.analyze(image, actions=["age", "gender", "race"], enforce_detection=False)
        return result
    except Exception as e:
        return str(e)

# Function to overlay results on image
def overlay_results(image, analysis):
    draw = ImageDraw.Draw(image, "RGBA")
    font = ImageFont.truetype("arial.ttf", 20)  # Reduced font size
    
    for face in analysis:
        if "region" in face:
            region = face["region"]
            x, y, w, h = region.get("x", 0), region.get("y", 0), region.get("w", 0), region.get("h", 0)
            text = f"Age: {face['age']}\nGender: {face['dominant_gender']}\nEthnicity: {face['dominant_race']}"
            
            # Draw bounding box and overlay background
            draw.rectangle([(x, y), (x + w, y + h)], outline=(255, 255, 0, 200), width=3)
            draw.rectangle([(x, y - 50), (x + w, y)], fill=(0, 0, 0, 180))
            draw.text((x + 10, y - 45), text, font=font, fill="white")
            
            # Draw facial landmarks
            if predictor:
                gray = np.array(image.convert("L"))
                dets = detector(gray)
                for det in dets:
                    shape = predictor(gray, det)
                    for i in range(68):
                        point = (shape.part(i).x, shape.part(i).y)
                        draw.ellipse([point[0] - 3, point[1] - 3, point[0] + 3, point[1] + 3], fill=(0, 255, 0, 255))
    
    return image

# Function to save analysis report
def save_report(analysis):
    report_filename = "detection_report.json"
    with open(report_filename, "w") as f:
        json.dump(analysis, f, indent=4)
    return report_filename

# Layout for Streamlit UI
st.sidebar.header("📤 Upload an Image")
uploaded_file = st.sidebar.file_uploader("", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = image.resize((400, 400))  # Resize uploaded image
    
    st.image(image, caption="📷 Uploaded Image", use_column_width=False, width=400)
    
    # Convert PIL image to numpy array
    image_array = np.array(image)
    
    # Perform analysis
    st.subheader("🔍 Detection Results")
    st.write("Processing...")
    analysis = analyze_image(image_array)
    
    # Overlay results on image
    annotated_image = overlay_results(image.copy(), analysis)
    st.image(annotated_image, caption="🖼️ Processed Image", use_column_width=False, width=400)
    
    # Save and provide download link for report
    report_file = save_report(analysis)
    st.download_button(label="📥 Download Report", data=json.dumps(analysis, indent=4), file_name=report_file, mime="application/json")

# Live Camera Feed
st.sidebar.write("### 🎥 Live Camera Feed")

def process_frame(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    analysis = analyze_image(rgb_frame)
    pil_image = Image.fromarray(rgb_frame)
    return overlay_results(pil_image, analysis)

if "camera_running" not in st.session_state:
    st.session_state.camera_running = False

def start_camera():
    st.session_state.camera_running = True

def stop_camera():
    st.session_state.camera_running = False

st.sidebar.button("Start Camera", on_click=start_camera)
st.sidebar.button("Stop Camera", on_click=stop_camera)

if st.session_state.camera_running:
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 15)  # Reduce FPS to minimize lag
    stframe = st.empty()
    while st.session_state.camera_running and cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        processed_image = process_frame(frame)
        stframe.image(processed_image, caption="📡 Live Detection", use_column_width=False, width=400)
    cap.release()

# Video Upload Section
st.sidebar.write("### 🎬 Video Upload (Coming Soon)")
