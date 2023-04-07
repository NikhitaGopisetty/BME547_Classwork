import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import base64
import requests

server = 'http://vcm-21170.vm.duke.edu'
filename = None
i = 4


def set_up_window():

    def main():
        global i
        filename = select_image()
        b64_image = convert_image_file_to_base64_string(filename)
        if filename == "":
            return
        print(b64_image)
        upload_base64_string_to_server(b64_image)
        b64_image_wm = download_image_from_server(1)
        print(b64_image_wm)
        new_file = 'duke_wm_{}.jpeg'.format(i)
        convert_base64_string_to_image_file(b64_image_wm, new_file)
        pil_image = Image.open(new_file)
        pil_image = pil_image.resize((100, 100))
        tk_image = ImageTk.PhotoImage(pil_image)
        image_label = ttk.Label(root, image=tk_image)
        image_label.grid(column=1, row=2)
        image_label.image = tk_image

    # Select image to upload
    def select_image():
        filename = filedialog.askopenfilename(initialdir="Images")
        return filename

    # Convert image file to base64 string
    def convert_image_file_to_base64_string(filename):
        with open(filename, "rb") as image_file:
            b64_bytes = base64.b64encode(image_file.read())
        b64_string = str(b64_bytes, encoding='utf-8')
        return b64_string

    # Upload base64 string to server
    def upload_base64_string_to_server(b64_string):
        image = {"image": b64_string, "net_id": 'nrg21', "id_no": i}
        r = requests.post(server + "/add_image", json=image)
        print(r.status_code)
        print(r.text)

    # Download watermarked image
    def download_image_from_server(id_no):
        r = requests.get(server + "/get_image/nrg21/{}".format(id_no))
        print(r.status_code)
        print(r.text)
        return r.text

    # Convert base64 string to image
    def convert_base64_string_to_image_file(b64_string, new_filename):
        image_bytes = base64.b64decode(b64_string)
        with open(new_filename, "wb") as out_file:
            out_file.write(image_bytes)
    
    root = tk.Tk()
    root.title("Image Encoding and Decoding")

    image_button = ttk.Button(root, text="Select Image",
                                     command=main)
    image_button.grid(column=1, row=1)

    root.mainloop()


if __name__ == '__main__':
    set_up_window()
    print("end")
