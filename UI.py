import tkinter as tk
from tkinter import ttk
import pandas as pd
def eingabe():
    fields = ['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 
              'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 
              'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth', 
              'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 
              'Income']
    field_label = {
    'HighBP': 'High Blood Pressure',
    'HighChol': 'High Cholesterol',
    'CholCheck': 'Cholesterol Check in Last 5 Years',
    'BMI': 'Body Mass Index',
    'Smoker': 'Smoked at Least 100 Cigarettes in Lifetime',
    'Stroke': 'History of Stroke',
    'HeartDiseaseorAttack': 'Coronary Heart Disease (CHD) or MI',
    'PhysActivity': 'Physical Activity in Past 30 Days (Not Including Job)',
    'Fruits': 'Consume Fruit 1 or More Times per Day',
    'Veggies': 'Consume Vegetables 1 or More Times per Day',
    'HvyAlcoholConsump': 'Heavy Alcohol Consumption',
    'AnyHealthcare': 'Have Any Kind of Health Care Coverage',
    'NoDocbcCost': 'Could Not See Doctor Due to Cost in Past 12 Months',
    'GenHlth': 'General Health (1=Excellent to 5=Poor)',
    'MentHlth': 'Days Mental Health Not Good (Past 30 Days)',
    'PhysHlth': 'Amount of days with bad Physical Health (Past 30 Days)',
    'DiffWalk': 'Serious Difficulty Walking or Climbing Stairs',
    'Sex': 'Sex',
    'Age': '13-Level Age Category',
    'Education': 'Education Level (1=No School, 6=College Graduate)',
    'Income': 'Income Level'  
}


    global entries
    entries = []

    # Main container
    fenster = tk.Tk()
    fenster.title("Prediction of Diabetes")

    # Frame for the canvas and scrollbar
    container = ttk.Frame(fenster)
    container.pack(fill="both", expand=True)

    # Canvas for scrolling
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Title
    tk.Label(scrollable_frame, text="Prediction of Diabetes", font=("Architects Daughter", 16)).pack()
    tk.Label(scrollable_frame, text="", font=("Architects Daughter", 30)).pack()

    for field in fields:
        if field == 'Sex':
            sex = tk.StringVar()

            row = ttk.Frame(scrollable_frame)
            lab = ttk.Label(row, width=47, text=field_label[field], anchor='w')
            radiobutton1 = ttk.Radiobutton(row, text='Male', variable=sex, value='male')
            radiobutton2 = ttk.Radiobutton(row, text='Female', variable=sex, value='female')

            row.pack(side=tk.TOP, fill="x", padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            radiobutton1.pack(side=tk.RIGHT, expand=tk.YES)
            radiobutton2.pack(side=tk.RIGHT, expand=tk.YES)
            entries.append((field, sex))

        elif field in ['HighBP', 'HighChol','NoDocbcCost', 'CholCheck', 'Smoker', 'Stroke','HvyAlcoholConsump', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies','AnyHealthcare']:
            var = tk.IntVar()

            row = ttk.Frame(scrollable_frame)
            lab = ttk.Label(row, width=50, text=field_label[field], anchor='w')
            radiobutton1 = ttk.Radiobutton(row, text='Yes', variable=var, value=1)
            radiobutton2 = ttk.Radiobutton(row, text='No', variable=var, value=0)

            row.pack(side=tk.TOP, fill="x", padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            radiobutton2.pack(side=tk.RIGHT, expand=tk.YES)
            radiobutton1.pack(side=tk.RIGHT, expand=tk.YES)
            entries.append((field, var))

        elif field in ['BMI', 'GenHlth', 'MentHlth', 'PhysHlth', 'Age']:
            row = ttk.Frame(scrollable_frame)
            lab = ttk.Label(row, width=50, text=field_label[field], anchor='w')
            ent = ttk.Entry(row)

            row.pack(side=tk.TOP, fill="x", padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES)
            entries.append((field, ent))

        elif field == 'DiffWalk':
            var = tk.IntVar()
            row = ttk.Frame(scrollable_frame)
            lab = ttk.Label(row, width=50, text=field_label[field], anchor='w')
            radiobutton1 = ttk.Radiobutton(row, text='Yes', variable=var, value=1)
            radiobutton2 = ttk.Radiobutton(row, text='No', variable=var, value=0)

            row.pack(side=tk.TOP, fill="x", padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            radiobutton2.pack(side=tk.RIGHT, expand=tk.YES)
            radiobutton1.pack(side=tk.RIGHT, expand=tk.YES)
            
            entries.append((field, var))

        elif field == 'Education':
            var = tk.StringVar()
            options = ['No High School', 'High School Graduate', 'Some College', 'Associate Degree', 'Bachelor’s Degree', 'Graduate or Professional Degree']

            row = ttk.Frame(scrollable_frame)
            lab = ttk.Label(row, width=50, text=field_label[field], anchor='w')
            dropdown = ttk.OptionMenu(row, var, *options)

            row.pack(side=tk.TOP, fill="x", padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            dropdown.pack(side=tk.RIGHT, expand=tk.YES)
            entries.append((field, var))
    
        elif field == 'Income':
            var = tk.StringVar()
            options = ['< $10,000', '$10,000 - $14,999', '$15,000 - $19,999', '$20,000 - $24,999', '$25,000 - $29,999',
                       '$30,000 - $34,999', '$35,000 - $39,999', '$40,000 - $44,999', '$45,000 - $49,999', '$50,000 - $59,999',
                       '$60,000 - $74,999', '$99,999 and above']

            row = ttk.Frame(scrollable_frame)
            lab = ttk.Label(row, width=50, text=field_label[field], anchor='w')
            dropdown = ttk.OptionMenu(row, var, *options)

            row.pack(side=tk.TOP, fill="x", padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            dropdown.pack(side=tk.RIGHT, expand=tk.YES)
            entries.append((field, var))

        else:
            row = ttk.Frame(scrollable_frame)
            lab = ttk.Label(row, width=50, text=field_label[field], anchor='w')
            ent = ttk.Entry(row)

            row.pack(side=tk.TOP, fill="x", padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES)
            entries.append((field, ent))
    button_row = tk.Frame(scrollable_frame)
    button_row.pack(side=tk.TOP, padx=5, pady=5)
    message_label = tk.Label(scrollable_frame, text="", font=("Architects Daughter", 12), fg="green")
    message_label.pack()
    message_label.pack_forget()  # hide
    ttk.Button(button_row, text="Analyze", command=lambda: save(entries,message_label)).pack(side=tk.LEFT, padx=5)
    ttk.Button(button_row, text="Exit", command=fenster.destroy).pack(side=tk.RIGHT, padx=5)


    fenster.mainloop()

def save(entries,message_label):
    # Logic to save entries
    income_scale = {
    '< $10,000': 1,
    '$10,000 - $14,999': 1,
    '$15,000 - $19,999': 2,
    '$20,000 - $24,999': 2,
    '$25,000 - $29,999': 3,
    '$30,000 - $34,999': 3,
    '$35,000 - $39,999': 4,
    '$40,000 - $44,999': 4,
    '$45,000 - $49,999': 5,
    '$50,000 - $59,999': 5,
    '$60,000 - $74,999': 6,
    '$99,999 and above': 8,
    
}
    education_level_map = {
    'No High School': 1,
    'High School Graduate': 2,
    'Some College': 3,
    'Associate Degree': 4,
    'Bachelor’s Degree': 5,
    'Graduate or Professional Degree': 6
}

    data = {}

    # Extract values from the entries
    for key, var in entries:
        if isinstance(var, tk.IntVar):
            data[key] = var.get()
        elif isinstance(var, tk.StringVar):
            value = var.get()
            if key == 'Education':
                data[key] = education_level_map.get(value, None)
            elif key == 'Income':
                data[key] = income_scale.get(value, None)
            else:
                data[key] = value
        elif isinstance(var, tk.Entry):
            data[key] = var.get()

    # Create a Pandas DataFrame from the extracted values
    df = pd.DataFrame([data])
    
    #TODO Make model input here


    print("Entries saved")
    message_label.config(text="Patient has a risk of 38% to have diabetes.")
    message_label.pack()

# Run the function
eingabe()
