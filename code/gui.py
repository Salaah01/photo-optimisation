import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import img_extensions
import optimise_img
import gui_controls


import time

class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.window = master
        self.window.geometry('790x350')
        try:
            try:
                # Windows
                self.window.iconbitmap(default=resource_path('logo.ico'))
            except:
                # Mac
                pass
        except tk.TclError:
            cwd = os.path.dirname(os.path.realpath(__file__))
            logo = os.path.join(os.path.dirname(os.path.realpath(__file__)), "logo.ico")
            try:
                # Windows
                self.window.iconbitmap(default=resource_path('code\\logo.ico'))
            except:
                # Mac
                pass
        except:
            pass
        self.window.title('MiniPics')
        self.invalid_files = []

    #  GUI CONTROLS

    def get_list_items(self):
        """
        Retrive all items from the list
        """
        self.list_items = self.files.get(0,tk.END)

        # Update invalid files
        self.invalid_files = []
        for file in self.list_items:
            if "<<INVALID FILETYPE>> " in file:
                self.invalid_files.append(file)

        invalid_files = len(self.invalid_files)
        # If there are any invalid files, then update the label with the error.
        if invalid_files == 0:
            self.info_label.config(text='')
        elif invalid_files == 1:
            self.info_label.config(text=f"{invalid_files} invalid file")
            self.info_label.config(fg='red')
        else:
            self.info_label.config(text=f"{invalid_files} invalid files")
            self.info_label.config(fg='red')

    def ctrl_browse_btn(self):
        """
        When the browse button is selected, the user will be able to select multiple files.
        When the user confirms their selection, the listbox with populate with the filepaths in selection.
        """
        filenames = tk.filedialog.askopenfilenames(title="Select Pictures to Import", filetypes=img_extensions.all_formats)
        gui_controls.insert_files(filenames, self.files, self.list_items)
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
        gui_controls.insert_single_file(filename=file_to_add, listbox=self.files, listbox_items=self.list_items, info_label=self.info_label, entry_box_field=self.file_path)
        self.get_list_items()

    def ctrl_remove_btn(self):
        """
        If the user presses remove, then it will remove the selected file form the list"
        """
        for f in range(len(self.list_items)):
            if self.ent_file.get() == self.list_items[f]:
                self.files.delete(f)
                # Mark the file in index-1 as the selected file.
                if f == 0:
                    self.files.select_set(0)
                else:
                    self.files.select_set(f-1)
                self.selected = self.files.get(self.files.curselection())
                self.file_path.set(self.selected)
                break

        self.get_list_items()

    def ctrl_optimise_opts_opt_auto(self):
        if self.val_auto.get():
            self.opt_quality.config(state='disabled')
            self.opt_resize_h.config(state='disabled')
            self.opt_resize_w.config(state='disabled')
        else:
            self.opt_quality.config(state='normal')
            self.opt_resize_h.config(state='normal')
            self.opt_resize_w.config(state='normal')

    def ctrl_disable_all_options(self):
        """
        Disable all options (for when the optimisation is taking place)
        """
        self.ent_file.config(state='disabled')
        self.browse_btn.config(state='disabled')
        self.add_btn.config(state='disabled')
        self.remove_btn.config(state='disabled')
        self.opt_auto.config(state='disabled')
        self.opt_quality.config(state='disabled')
        self.opt_resize_h.config(state='disabled')
        self.opt_resize_w.config(state='disabled')
        self.opt_convert.config(state='disabled')
        self.btn_optimise.config(state='disabled')

    def ctrl_enable_all_options(self):
        """
        Enable all options (for when the optimisation has finished).
        ollowing this, run self.ctrl_optimise_opts_auto to disable the respective files when the Auto Optimise button is selected.
        """
        self.ent_file.config(state='normal')
        self.browse_btn.config(state='normal')
        self.add_btn.config(state='normal')
        self.remove_btn.config(state='normal')
        self.opt_auto.config(state='normal')
        self.opt_quality.config(state='normal')
        self.opt_resize_h.config(state='normal')
        self.opt_resize_w.config(state='normal')
        self.opt_convert.config(state='normal')
        self.btn_optimise.config(state='normal')
        self.ctrl_optimise_opts_opt_auto()
    
    def ctrl_btn_optimise(self):
        if self.list_items:
            save_loc = tk.filedialog.askdirectory(title='Select Folder to Save Pictures')
            
            if save_loc:

                self.ctrl_disable_all_options()

                def optimisation_method(img_file, save_dir, **kwargs):
                    """
                    Will pass the optimisation methods.
                    """
                    # SET THE VALUES

                    # Quality
                    if 'quality' in kwargs:
                        quality = int(kwargs['quality'])
                    else:
                        quality = 100
                    
                    # Resize
                    if 'resize' in kwargs:
                        resize_w = kwargs['resize'][0]
                        resize_h = kwargs['resize'][1]
                        resize = (resize_w, resize_h)
                    else:
                        resize = (0, 0)

                    # Change Format
                    if 'new_format' in kwargs:
                        new_format = kwargs['new_format']
                        if new_format == "(default)": new_format = None
                    else:
                        new_format = None

                    # RUN THE OPTIMISATION
                    
                    if optimise_img.run_optimisation(img_file = img_file, save_dir = save_dir, quality = quality, resize = resize, new_format = new_format) == False:
                        return False
                    else:
                        return True

                def update_progress(progress_bar, label_elem, processed, current_val, skipped, success):
                    total_size = len(self.list_items)
                    progress_bar['value'] = current_val/total_size * 100
                    progress_bar.update()
                    label_elem.config(text=f"{processed} of {total_size} files processed. {skipped} files skipped.")
                    if success:
                        self.files.itemconfig(current_val, {'fg': 'green'})
                    else:
                        self.files.itemconfig(current_val, {'fg': '#e67e22'})
                        if skipped == 1:
                            self.info_label.config(text="1 file skipped", fg="#e67e22")
                        elif skipped > 1:
                            self.info_label.config(text=f"{skipped} files skipped", fg="#e67e22")
                
                # Change the format of resize to work with the program
                if self.opt_resize_h.get() == "":
                    resize_h = 0
                else:
                    try:
                        resize_h = int(self.opt_resize_h.get())
                    except:
                        resize_h = 0
                
                if self.opt_resize_w.get() == "":
                    resize_w = 0
                else:
                    try:
                        resize_w = int(self.opt_resize_w.get())
                    except:
                        resize_w = 0

                # Create Progress Bar
                progress_bar = ttk.Progressbar(self.frame_file_upload, maximum=100)
                progress_bar.grid(
                    row=1,
                    column=0,
                    pady=10,
                    sticky='w, e'
                    )
                
                progress_bar_info = tk.Label(self.frame_file_upload, text="", fg='green')
                progress_bar_info.grid(
                    row=1,
                    column=1,
                )

                # If user has chosesn "auto optimise"
                if self.val_auto.get():
                    processed = 0
                    skipped = 0
                    for i, file in enumerate(self.list_items):

                        if not("<<INVALID FILETYPE>> ") in file:
                            processed += 1
                            if not(optimisation_method(img_file = file, save_dir = save_loc, quality = 80, new_format = self.val_convert.get()) == False):
                                success = True
                            else:
                                success = False
                                skipped += 1

                            update_progress(progress_bar = progress_bar, label_elem = progress_bar_info, current_val = i, processed = processed, success=success, skipped=skipped)
                  
                else:
                    processed = 0
                    skipped = 0
                    for i, file in enumerate(self.list_items):
                        if not("<<INVALID FILETYPE>> ") in file:
                            processed += 1
                            if not(optimisation_method(img_file = file, save_dir = save_loc, quality = self.opt_quality.get(), resize=(resize_w, resize_h), new_format = self.val_convert.get()) == False):
                                success = True
                            else:
                                success = False
                                skipped += 1

                            update_progress(progress_bar = progress_bar, label_elem = progress_bar_info, current_val = i, processed = processed, success=success, skipped=skipped)
                
                # Progress Bar 100% and remove
                progress_bar['value'] = 100
                progress_bar.update()
                time.sleep(0.5)
                progress_bar.grid_forget()

                self.ctrl_enable_all_options()

                # os.startfie does not work on all OS.
                try:
                    os.startfile(save_loc)
                except:
                    pass
        else:
            self.info_label.config(text="Please add files", fg='red')
    
    # FRAME LAYOUTS

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

        # Info Section
        self.frame_info = tk.Frame(self.window)
        self.frame_info.grid(
            row=0,
            column=1,
            columnspan=2,
            pady=(5, 10),
            padx=(5, 0),
            )

        # File List
        self.frame_file_list = tk.Frame(self.window, width=50)
        self.frame_file_list.grid(
            row=1,
            column=0,
            padx=(5, 0),
            pady=(0, 5),
            sticky='w, e n, s'
            )

        # Optimise Options
        self.frame_optimise_opts = tk.Frame(self.window)
        self.frame_optimise_opts.grid(
            row=1,
            column=1,
            padx=20,
            )

    def file_upload(self):
        # Input
        self.file_path = tk.StringVar()
        self.ent_file = tk.Entry(self.frame_file_upload, width=1000, textvariable=self.file_path)
        self.ent_file.grid(
            row=0,
            column=0,
            padx=(0, 5),
            sticky='w'
            )

        # Browse Button
        self.browse_btn = tk.Button(
            self.frame_file_upload,
            text='Browse',
            width=12,
            command=self.ctrl_browse_btn
            )
        self.browse_btn.grid(
            row=0,
            column=1,
            padx=(10, 0)
            )

        # Add Button
        self.add_btn = tk.Button(
            self.frame_file_upload,
            text='Add',
            command=self.ctrl_add_btn,
            width=12
        )
        self.add_btn.grid(
            row=0,
            column=2,
            padx=(10, 0)
            )

        # Remove Button
        self.remove_btn = tk.Button(
            self.frame_file_upload,
            text='Remove',
            width=12,
            command=self.ctrl_remove_btn
        )
        self.remove_btn.grid(
            row=0,
            column=3,
            padx=(10, 15)
            )

    def info(self):
        self.info_label = tk.Label(
            self.frame_info,
            text="testing",
            font=("Arial", 15)
        )
        self.info_label.grid(
            row=0,
            column=0,
            sticky='e',
            padx=30
            )

    #  WIDGETS

    def file_list(self):
        self.files = tk.Listbox(self.frame_file_list, height=6, width=25)
        self.files.grid(
            row=0,
            column=0,
            sticky='w, e, n, s'
            )
        self.files.bind('<<ListboxSelect>>', self.selected_file)
        
        self.get_list_items()   # Run method to popluate list items

        scrollbar_y = tk.Scrollbar(self.frame_file_list, orient="vertical")
        scrollbar_y.config(command=self.files.yview)
        scrollbar_y.grid(row=0, column=1, sticky='n, s')

        self.files.config(yscrollcommand=scrollbar_y.set)

        scrollbar_x = tk.Scrollbar(self.frame_file_list, orient="horizontal")
        scrollbar_x.config(command=self.files.xview)
        scrollbar_x.grid(row=1, column=0, sticky='w, e')

        self.files.config(xscrollcommand=scrollbar_x.set)

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
        lbl_quality = tk.Label(self.frame_optimise_opts, text='QUALITY')
        lbl_quality.grid(
            row=1,
            column=0,
            columnspan=4,
            pady=(0, 0)
            )

        self.val_quality = tk.IntVar()
        self.opt_quality = tk.Scale(
            self.frame_optimise_opts,
            from_=1,
            to=100,
            orient='horizontal',
            variable=self.val_quality,
            )
        self.opt_quality.set(100)
        self.opt_quality.grid(
            row=2,
            column=0,
            pady=(0, 15),
            columnspan=4
            )

        # Resize
        lbl_resize=tk.Label(self.frame_optimise_opts, text="RESIZE (PX)")
        lbl_resize.grid(
            row=4,
            column=0,
            columnspan=4,
        )

        lbl_resize=tk.Label(self.frame_optimise_opts, text="(Leave W or H blank")
        lbl_resize.grid(
            row=5,
            column=0,
            columnspan=4,
            pady=(0, 0),
        )

        lbl_resize=tk.Label(self.frame_optimise_opts, text="to keep aspect ratio)")
        lbl_resize.grid(
            row=6,
            column=0,
            columnspan=4,
            pady=(0, 10),
        )

        self.val_resize_w = tk.StringVar()
        lbl_resize_w = tk.Label(self.frame_optimise_opts, text='W')
        lbl_resize_w.grid(
            row=7,
            column=0,
            pady=(0, 10)
            )
        self.opt_resize_w = tk.Entry(
            self.frame_optimise_opts,
            width=5,
            textvariable=self.val_resize_w
            )
        self.opt_resize_w.grid(
            row=7,
            column=1,
            pady=(0, 10)
            )

        self.val_resize_h = tk.StringVar()
        lbl_resize_h = tk.Label(self.frame_optimise_opts, text='H')
        lbl_resize_h.grid(
            row=7,
            column=2,
            padx=(15, 0),
            pady=(0, 10)
            )
        self.opt_resize_h = tk.Entry(
            self.frame_optimise_opts,
            width=5,
            textvariable=self.val_resize_h
            )
        self.opt_resize_h.grid(
            row=7,
            column=3,
            padx=(15, 10),
            pady=(0, 10)
            )

        # Convert
        self.val_convert = tk.StringVar()
        convert_opts = ['(default)'] + img_extensions.keys
        self.val_convert.set(convert_opts[0])
        lbl_convert = tk.Label(self.frame_optimise_opts, text="Format")
        lbl_convert.grid(
            row=8,
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
            row=8,
            column=1,
            pady=(0, 10),
            columnspan=3,
            sticky='w, e'
            )

        # Optimise Button
        self.btn_optimise = tk.Button(
            self.frame_optimise_opts,
            command=self.ctrl_btn_optimise,
            width=10,
            text='Run'
        )
        self.btn_optimise.grid(
            row=9,
            column=0,
            columnspan=4
            )

    def build(self):

        # Call Layounds
        self.frame_layouts()

        # Call Sections
        self.file_upload()
        self.info()
        self.file_list()
        self.optimise_opts()

        # Layout Rules to Fit Screen on Resize
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.frame_file_upload.rowconfigure(0, weight=1)
        self.frame_file_upload.columnconfigure(0, weight=1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        self.frame_file_list.rowconfigure(0, weight=1)
        self.frame_file_list.columnconfigure(0, weight=1)
        self.frame_optimise_opts.rowconfigure(0, weight=1)
        self.frame_optimise_opts.columnconfigure(0, weight=1)        
        self.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root).build()
