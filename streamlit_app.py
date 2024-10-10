import streamlit as st
import cv2
import numpy as np
from PIL import Image
from keras.models import load_model

st.sidebar.markdown("**🎯 Let's Connect**")
st.sidebar.markdown(
        "- [LinkedIn](https://www.linkedin.com/in/fareedqk/)\n"
        "- [GitHub](https://github.com/fareedqk/)\n"
        "- [X](https://twitter.com/fareedcodes/)\n"
    )

# Load the pretrained model
model = load_model('weather_model.h5')

# Define labels
labels = {0: 'sunrise', 1: 'sunshine', 2: 'rain', 3:'cloudy'}

st.title("Weather Image Classification")

# Upload image
image = st.file_uploader("Choose an image...", type=["jpg", "png"])

if image is not None:

    # Convert to OpenCV format
    file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    # Reshape and preprocess
    opencv_image = cv2.resize(opencv_image, (64,64))
    opencv_image = np.expand_dims(opencv_image, axis=0)

    # Make prediction
    prediction = model.predict(opencv_image)  
    predicted_label = labels[np.argmax(prediction)].upper()

    # Display image and result
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write(f"Predicted Label: **{predicted_label}**")
    predicted_label = predicted_label.lower().strip()
    
    if predicted_label == 'sunrise':
        st.write(":sunrise:")
    elif predicted_label == 'sunshine':
        st.write(":sunny:")
    elif predicted_label == 'rain':
        st.write(":umbrella:")
    else:
        st.write(":cloud:")