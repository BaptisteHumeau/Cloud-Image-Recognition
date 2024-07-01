#-------------------------------------------------------------------------
#DEPENDENCIES
#-------------------------------------------------------------------------

import sys
import warnings
import logging
import numpy as np
import tensorflow as tf # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
from PIL import Image, ImageTk # type: ignore
import tkinter as tk
from tkinter import filedialog, messagebox

#-------------------------------------------------------------------------
#Functions
#-------------------------------------------------------------------------

def on_closing():
    root.destroy()
    sys.exit(0)

def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0 
    return img_array

def predict_image(img_path):
    try:
        img_array = preprocess_image(img_path)
        predictions = model.predict(img_array)
        predicted_class_index = np.argmax(predictions)
        predicted_class_label = class_indices[predicted_class_index]
        return predicted_class_label
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        predicted_label = predict_image(file_path)
        if predicted_label:
            result_label.config(text=f"Predicted Cloud Type: {predicted_label}")
            display_image(file_path)
        else:
            result_label.config(text="Prediction failed.")

def display_image(img_path):
    img = Image.open(img_path)
    img = img.resize((250, 250), resample=Image.BILINEAR) 
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo

#-------------------------------------------------------------------------
#Main 
#-------------------------------------------------------------------------

def main():
    global model, class_indices, root, result_label, image_label

    tf.get_logger().setLevel(logging.ERROR)
    warnings.filterwarnings('ignore', category=UserWarning, module='tensorflow')
    warnings.filterwarnings('ignore', category=FutureWarning, module='tensorflow')

    model_name = 'models/cloud_classification_model_simplified4.keras'
    try:
        model = tf.keras.models.load_model(model_name)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load model: {str(e)}")
        sys.exit(1)

    if 'simplified' in model_name:
        class_indices = {
            0: 'CIRRUS',
            1: 'CUMULUS',
            2: 'STRATUS'
        }
    else:
        class_indices = {
            0: 'CIRRUS', 1: 'CIRROSTRATUS', 2: 'CIRROCUMULUS', 
            3: 'ALTOCUMULUS', 4: 'ALTOSTRATUS', 5: 'CUMULUS', 
            6: 'CUMULONIMBUS', 7: 'NIMBOSTRATUS', 8: 'STRATOCUMULUS', 
            9: 'STRATUS', 10: 'CONTRAIL'
        }

    class_labels = {v: k for k, v in class_indices.items()}

    root = tk.Tk()
    root.title("Cloud Type Classifier: using  " + model_name.split('_')[-1].split('.')[0].upper())
    root.geometry("600x500")

    browse_button = tk.Button(root, text="Browse Image", command=browse_file)
    browse_button.pack(pady=20)

    result_label = tk.Label(root, text="Predicted Cloud Type: ")
    result_label.pack(pady=10)

    image_label = tk.Label(root)
    image_label.pack(pady=20)

    root.protocol("WM_DELETE_WINDOW", on_closing) 

    root.mainloop()

#-------------------------------------------------------------------------
#RUN
#-------------------------------------------------------------------------

if __name__ == "__main__":
    main()
