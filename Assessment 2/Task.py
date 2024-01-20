import requests
import tkinter as tk
from tkinter import ttk
from urllib.parse import quote

class StyledMealApp:
    def __init__(self, master):
        #the main window
        self.master = master
        self.master.title("Styled Meal Information App")
        self.master.geometry("700x900")  #the fixed size for the window

        #settting a background color for main window
        self.master.configure(bg="aquamarine")

        #setting a custom style for theme
        style = ttk.Style(self.master)
        style.theme_use("clam")

        #creating a frame for the input and buttons
        self.styled_frame = ttk.Frame(master, padding=(20, 10), style='TFrame')
        self.styled_frame.grid(row=0, column=0, pady=20, padx=20)

        #labeling for meal name input
        self.label_styled_meal_name = ttk.Label(self.styled_frame, text="Enter Meal Name:", font=('Arial', 14), style='TLabel')
        self.label_styled_meal_name.grid(row=0, column=0, pady=10, padx=10)

        #input for the meal name input
        self.entry_styled_meal_name = ttk.Entry(self.styled_frame, width=30, font=('Arial', 12))
        self.entry_styled_meal_name.grid(row=0, column=1, pady=10, padx=10)

        #button to get the meal information
        self.button_get_styled_meal_info = ttk.Button(self.styled_frame, text="Get Meal Info", command=self.get_styled_meal_info, style='TButton.Font.TButton')
        self.button_get_styled_meal_info.grid(row=0, column=2, pady=10, padx=10)

        #creating a frame for the displaying results
        self.result_styled_frame = ttk.Frame(master, padding=(20, 10), style='TFrame')
        self.result_styled_frame.grid(row=1, column=0, pady=20, padx=20)

        #labeling for displaying the meal information
        self.result_styled_label = ttk.Label(self.result_styled_frame, text="", wraplength=500, justify="left", font=('Arial', 12), style='TLabel')
        self.result_styled_label.grid(row=0, column=0, pady=20, padx=10)

    def get_styled_meal_info(self):
        #a function to retrieve and display the meal information based on the user input
        styled_meal_name = self.entry_styled_meal_name.get()
        styled_meal_name_encoded = quote(styled_meal_name)

        if styled_meal_name:
            api_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={styled_meal_name_encoded}"

            try:
                styled_meal_data = self.get_data_from_api(api_url)
                if "meals" in styled_meal_data and styled_meal_data["meals"]:
                    self.display_styled_meal_info(styled_meal_data["meals"][0])
                else:
                    self.result_styled_label.config(text="Meal not found.")
            except requests.RequestException as e:
                self.result_styled_label.config(text=f"Error: {str(e)}")
        else:
            self.result_styled_label.config(text="Please enter a meal name.")

    def get_data_from_api(self, api_url):
        #function to retrieve the data from the API
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data

    def display_styled_meal_info(self, styled_meal_info):
        #function to display meal information in the result label
        info_text = f"Meal Name: {styled_meal_info['strMeal']}\n"
        info_text += f"Instructions: {styled_meal_info['strInstructions']}"
        self.result_styled_label.config(text=info_text)


if __name__ == "__main__":
    #run the application
    root = tk.Tk()
    app = StyledMealApp(root)
    root.mainloop()
