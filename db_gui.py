import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from tkinter import filedialog


def create_blood_string(blood_letter, rh):
    blood_string = "{}{}".format(blood_letter, rh)
    return blood_string


def id_number_verification(id_number):
    if 1 <= id_number <= 1000000:
        return True
    else:
        return False


def send_data_to_server(patient_name, id_number, blood_string,):
    patient = {"id": id_number,
               "name": patient_name,
               "blood_type": blood_string}
    r = requests.post("http://127.0.0.1:5000/new_patient", json=patient)
    return r.text


def check_and_upload_data(patient_name, id_number, blood_letter, rh,
                          donation_center):
    id_number = int(id_number)
    blood_string = create_blood_string(blood_letter, rh)
    if id_number_verification(id_number) is False:
        return "ID number is incorrect"
    msg = send_data_to_server(patient_name, id_number, blood_string)
    return msg


def set_up_window():

    def ok_btn_cmd():
        print("OK clicked")
        patient_name = name_value.get()
        patient_id = id_value.get()
        blood_letter = blood_letter_value.get()
        rh = rh_factor_value.get()
        donation_center = donation_value.get()
        msg = check_and_upload_data(patient_name, patient_id, blood_letter, rh,
                                    donation_center)
        status_label.configure(text=msg)
        id_entry.configure(state=tk.DISABLED)

    def cancel_btn_cmd():
        root.destroy()
        # id_entry.configure(state=tk.NORMAL)

    def change_label_color():
        current_color = top_label.cget('foreground')
        if current_color == "":
            color = 'white'
        else:
            color = current_color.string
        if color == 'white':
            new_color = 'red'
        else:
            new_color = 'white'
        top_label.configure(foreground=new_color)
        root.after(1000, change_label_color)

    def shuffle_choices():
        current_choices = list(donation_combobox.cget("values"))
        import random
        random.shuffle(current_choices)
        donation_combobox.configure(values=current_choices)

    def change_image_cmd():
        print("Run change image")
        filename = filedialog.askopenfilename(initialdir="Images")
        if filename == "":
            return
        new_image = Image.open(filename)
        current_size = new_image.size
        max_size = 100
        alpha = max_size / max(current_size)
        new_image = new_image.resize((round(alpha*current_size[0]),
                                      round(alpha*current_size[1])))
        tk_image = ImageTk.PhotoImage(new_image)
        image_label.configure(image=tk_image)
        image_label.image = tk_image

    root = tk.Tk()
    root.title("Donor Database GUI")
    # root.geometry("800x400")

    top_label = ttk.Label(root, text="Blood Donor Database")
    top_label.grid(column=0, row=0, columnspan=2, sticky=tk.W)

    name_label = ttk.Label(root, text="Name:")
    name_label.grid(column=0, row=1, sticky=tk.E)
    name_value = tk.StringVar()
    # name_value.set("Enter your name here")
    name_entry = ttk.Entry(root, textvariable=name_value)
    name_entry.grid(column=1, row=1, padx=5)

    id_label = ttk.Label(root, text="ID:")
    id_label.grid(column=0, row=2, sticky=tk.E)
    id_value = tk.StringVar()
    id_entry = ttk.Entry(root, textvariable=id_value)
    id_entry.grid(column=1, row=2, padx=5)

    ok_button = ttk.Button(root, text="OK", command=ok_btn_cmd)
    ok_button.grid(column=1, row=6)

    cancel_button = ttk.Button(root, text="Cancel", command=cancel_btn_cmd)
    cancel_button.grid(column=2, row=6)

    blood_letter_value = tk.StringVar()

    A_check = ttk.Radiobutton(root, text="A", variable=blood_letter_value,
                              value="A")
    A_check.grid(column=0, row=3, sticky=tk.W)

    B_check = ttk.Radiobutton(root, text="B", variable=blood_letter_value,
                              value="B")
    B_check.grid(column=0, row=4, sticky=tk.W)

    AB_check = ttk.Radiobutton(root, text="AB", variable=blood_letter_value,
                               value="AB")
    AB_check.grid(column=0, row=5, sticky=tk.W)

    O_check = ttk.Radiobutton(root, text="O", variable=blood_letter_value,
                              value="O")
    O_check.grid(column=0, row=6, sticky=tk.W)

    rh_factor_value = tk.StringVar()
    rh_factor_value.set("-")
    check_box_widget = ttk.Checkbutton(root, text="Rh Positive",
                                       variable=rh_factor_value,
                                       onvalue='+', offvalue='-')
    check_box_widget.grid(column=1, row=4)

    donation_label = ttk.Label(root, text="Closest Donation Center")
    donation_label.grid(column=2, row=0)
    donation_value = tk.StringVar()
    donation_combobox = ttk.Combobox(root, textvariable=donation_value)
    donation_combobox.grid(column=2, row=1)
    donation_combobox["values"] = ("Durham", "Apex", "Raleigh")
    donation_combobox.state(["readonly"])
    donation_combobox.configure(postcommand=shuffle_choices)

    status_label = ttk.Label(root, text="")
    status_label.grid(row=7, column=0, columnspan=10)

    pil_image = Image.open("Images/blank_pic.jpeg")
    pil_image = pil_image.resize((100, 100))
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label = ttk.Label(root, image=tk_image)
    image_label.grid(column=1, row=7)
    image_label.image = tk_image

    image_change_button = ttk.Button(root, text="Change Image",
                                     command=change_image_cmd)
    image_change_button.grid(column=2, row=7)

    root.after(3000, change_label_color)

    root.mainloop()


if __name__ == '__main__':
    set_up_window()
    print("end")
