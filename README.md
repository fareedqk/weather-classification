# Weather Classification

This project integrates a custom Convolutional Neural Network (CNN) model for weather classification into a **Streamlit** app. Users can upload images, and the model will predict the weather condition as one of the following categories:

- **Sunrise**
- **Sunshine**
- **Rainy**
- **Cloudy**

## Features

- **Weather Classification**: Classifies images into one of four weather categories: sunrise, sunshine, rainy, or cloudy.
- **Streamlit Integration**: A user-friendly web interface where users can upload an image and get real-time predictions.
- **Custom CNN Model**: A custom-built CNN trained on a dataset of weather-related images.
- **Instant Feedback**: Provides classification results as soon as the user uploads an image.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/weather-classification-streamlit.git
    cd weather-classification-streamlit
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv weather-env
    source weather-env/bin/activate  # On Windows: weather-env\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Make sure Streamlit is installed:

    ```bash
    pip install streamlit
    ```

## How to Run the App

1. Run the Streamlit app using the following command:

    ```bash
    streamlit run app.py
    ```

2. The app will automatically open in your browser at `http://localhost:8501/`, where you can upload an image and get a weather classification.

## Usage

1. **Upload an Image**: Use the file uploader in the Streamlit app to upload a weather-related image (e.g., a photo of a rainy day, sunny day, etc.).
2. **View Prediction**: Once the image is uploaded, the custom CNN model will classify the weather condition, and the result will be displayed in the app.

## Model

- The custom CNN model has been designed and trained specifically for this weather classification task.
- The model has been trained on images of four weather types: **sunrise**, **sunshine**, **rainy**, and **cloudy**.
- The CNN architecture consists of several convolutional layers, max pooling, and fully connected layers, designed to learn weather-related features from the images.

### Model Architecture

1. **Input Layer**: Accepts input images of size 224x224x3.
2. **Convolutional Layers**: Extracts features from the images using filters.
3. **Pooling Layers**: Reduces the spatial dimensions while preserving important features.
4. **Fully Connected Layers**: Learns to classify the weather conditions based on the extracted features.
5. **Output Layer**: Softmax output for the four weather categories: sunrise, sunshine, rainy, and cloudy.

## Dataset

- The model has been trained on a dataset of images, each labeled as one of the four weather conditions.