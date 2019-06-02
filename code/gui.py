import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import img_extentions
import optimise_img
import os
# from gui_controls import Controls


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.window = master
        self.window.geometry('750x750')
        self.window.title('Image Optimisation')

    #  GUI CONTROLS

    def get_list_items(self):
        """
        Retrive all items from the list
        """
        self.list_items = self.files.get(0,tk.END)

    def ctrl_browse_btn(self):
        """
        When the browse button is selected, the user will be able to select multiple files.
        When the user confirms their selection, the listbox is populate with the filepaths of the selection.
        """
        filenames = tk.filedialog.askopenfilenames()
        for filename in filenames:
            if not(filename in self.list_items):
                self.files.insert(0, filename)
        self.get_list_items()

    def selected_file(self, evt):
        """
        If the user selects an item from the list, update the selected item
        """
        try:
            self.selected = self.files.get(self.files.curselection())
            self.file_path.set(self.selected)
            self.get_list_items()
        except IndexError:
            pass
        except tk.TclError:
            pass

    def ctrl_add_btn(self):
        """
        If the user presses add, then add filepath in the textbox into the list if it exists
        """
        file_to_add = self.ent_file.get()
        self.get_list_items()

        if not(file_to_add in self.list_items):
            if os.path.isfile(self.ent_file.get()):
                self.files.insert(0, self.ent_file.get())
            else:
                self.file_path.set('FILE DOES NOT EXIST')

        self.get_list_items()

    def ctrl_remove_btn(self):
        """
        If the user presses remove, then it will remove the selected file form the list"
        """
        for f in range(len(self.list_items)):
            if self.ent_file.get() == self.list_items[f]:
                self.files.delete(f)
                break

        self.get_list_items()

    def ctrl_optimise_btn(self):
        """
        Get the save directory and run the optimisation for each file in the list using the user's settings
        """
        save_dir = tk.filedialog.askopenfilenames()

    def ctrl_optimise_opts_opt_auto(self):
        if self.val_auto.get():
            self.opt_quality.config(state='disabled')
            self.opt_resize_h.config(state='disabled')
            self.opt_resize_w.config(state='disabled')
            self.opt_convert.config(state='disabled')
        else:
            self.opt_quality.config(state='normal')
            self.opt_resize_h.config(state='normal')
            self.opt_resize_w.config(state='normal')
            self.opt_convert.config(state='normal')
    
    def ctrl_btn_optimise(self):
        save_loc = tk.filedialog.askdirectory()
        
        if save_loc:
            
            # Create sub-directory
            sub_dir = 'optimised'
            target_dir = os.path.join(save_loc, sub_dir)

            # Check if this directory exists, if so create a new sub-directroy
            if os.path.isdir(target_dir):
                target_dir_exists = True
                counter = 0

                while target_dir_exists:
                    counter += 1

                    try_target_dir = f"{target_dir} ({counter})"

                    if not(os.path.isdir(try_target_dir)):
                        target_dir_exists = False
                        target_dir = try_target_dir
            
            # Create the sub-directory
            os.mkdir(target_dir)

            if self.val_auto.get():

                for file in self.list_items:
                    optimise_img.run_optimisation(
                        img_file=file,
                        save_dir=target_dir,
                        quality=80
                    )
            
            else:
                
                if self.val_convert.get() == "(default)":
                    for file in self.list_items:
                        optimise_img.run_optimisation(
                            img_file=file,
                            save_dir=target_dir,
                            quality=self.opt_quality.get(),
                            resize=(self.opt_resize_w.get(), self.opt_resize_h.get())
                        )
                
                else:
                    for file in self.list_items:
                        optimise_img.run_optimisation(
                            img_file=file,
                            save_dir=target_dir,
                            quality=self.opt_quality.get(),
                            resize=(int(self.opt_resize_w.get()), int(self.opt_resize_h.get())),
                            new_format=self.val_convert.get()
                        )
                print(self.opt_quality.get(), self.opt_resize_w.get(), self.opt_resize_h.get(), self.val_convert.get())
        
    # GUI LAYOUT

    def frame_layouts(self):
        # File Uplaod Section (Top)
        self.frame_file_upload = tk.Frame(self.window)
        self.frame_file_upload.grid(
            row=0,
            column=0,
            pady=(5, 10),
            padx=(5, 0),
            sticky='w, e'
            )

        # File List
        self.frame_file_list = tk.Frame(self.window)
        self.frame_file_list.grid(
            row=1,
            column=0,
            padx=(5, 0),
            pady=(0, 5),
            sticky='w, e, n, s')

        # Optimise Options
        self.frame_optimise_opts = tk.Frame(self.window)
        self.frame_optimise_opts.grid(
            row=1,
            column=1,
            padx=20
            )

    def file_upload(self):
        # Input
        self.file_path = tk.StringVar()
        self.ent_file = tk.Entry(self.frame_file_upload, textvariable=self.file_path)
        self.ent_file.grid(
            row=0,
            column=0,
            padx=(0, 5),
            sticky='w, e'
            )

        # Browse Button
        browse_btn = tk.Button(
            self.frame_file_upload,
            text='Browse',
            width=12,
            command=self.ctrl_browse_btn
            )
        browse_btn.grid(row=0, column=1)

        # Add Button
        add_btn = tk.Button(
            self.frame_file_upload,
            text='Add',
            command=self.ctrl_add_btn,
            width=12
        )
        add_btn.grid(row=0, column=2)

        # Remove Button
        remove_btn = tk.Button(
            self.frame_file_upload,
            text='Remove',
            width=12,
            command=self.ctrl_remove_btn
        )
        remove_btn.grid(row=0, column=3)

    def file_list(self):
        self.files = tk.Listbox(self.frame_file_list, height=6, width=35)
        self.files.grid(
            row=0,
            column=0,
            sticky='w, e, n, s'
            )
        self.files.bind('<<ListboxSelect>>', self.selected_file)
        
        self.get_list_items()   # Run method to popluate list items

    def optimise_opts(self):
        # Auto Optimise
        self.val_auto = tk.IntVar()
        self.opt_auto = tk.Checkbutton(
            self.frame_optimise_opts,
            text="Auto Optimise",
            variable=self.val_auto,
            command=self.ctrl_optimise_opts_opt_auto
            )
        self.opt_auto.grid(
            row=0,
            column=0,
            pady=(0, 10),
            columnspan=4,
            )

        # Quality
        lbl_quality = tk.Label(self.frame_optimise_opts, text='Quality')
        lbl_quality.grid(
            row=1,
            column=0,
            pady=(0, 0)
            )

        self.val_quality = tk.IntVar()
        self.opt_quality = tk.Scale(
            self.frame_optimise_opts,
            from_=0,
            to=100,
            orient='horizontal',
            variable=self.val_quality,
            )
        self.opt_quality.set(80)
        self.opt_quality.grid(
            row=1,
            column=1,
            pady=(0, 15),
            columnspan=3
            )

        # Resize
        self.val_resize_w = tk.StringVar()
        lbl_resize_w = tk.Label(self.frame_optimise_opts, text='W')
        lbl_resize_w.grid(
            row=3,
            column=0,
            pady=(0, 10)
            )
        self.opt_resize_w = tk.Entry(
            self.frame_optimise_opts,
            width=5,
            textvariable=self.val_resize_w
            )
        self.opt_resize_w.grid(
            row=3,
            column=1,
            pady=(0, 10)
            )

        self.val_resize_h = tk.StringVar()
        lbl_resize_h = tk.Label(self.frame_optimise_opts, text='H')
        lbl_resize_h.grid(
            row=3,
            column=2,
            pady=(0, 10)
            )
        self.opt_resize_h = tk.Entry(
            self.frame_optimise_opts,
            width=5,
            textvariable=self.val_resize_h
            )
        self.opt_resize_h.grid(
            row=3,
            column=3,
            pady=(0, 10)
            )

        # Convert
        self.val_convert = tk.StringVar()
        convert_opts = ['(default)'] + img_extentions.keys
        self.val_convert.set(convert_opts[0])
        lbl_convert = tk.Label(self.frame_optimise_opts, text="Format")
        lbl_convert.grid(
            row=4,
            column=0,
            pady=(0, 10),
            columnspan=1
            )
        self.opt_convert = tk.OptionMenu(
            self.frame_optimise_opts,
            self.val_convert,
            *convert_opts
            )
        self.opt_convert.grid(
            row=4,
            column=1,
            pady=(0, 10),
            columnspan=3,
            sticky='w, e'
            )

        # Optimise Button
        self.btn_optimise = tk.Button(
            self.frame_optimise_opts,
            command=self.ctrl_btn_optimise,
            text='Optimse'
        )
        self.btn_optimise.grid(row=5, column=0, columnspan=4)

    def build(self):

        # Call Layounds
        self.frame_layouts()

        # Call Sections
        self.file_upload()
        self.file_list()
        self.optimise_opts()

        # Layout Rules to Fit Screen on Resize
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.frame_file_upload.rowconfigure(0, weight=1)
        self.frame_file_upload.columnconfigure(0, weight=1)
        self.frame_file_list.rowconfigure(0, weight=1)
        self.frame_file_list.columnconfigure(0, weight=1)
        self.frame_optimise_opts.rowconfigure(0, weight=1)
        self.frame_optimise_opts.columnconfigure(0, weight=1)        
        self.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root).build()
