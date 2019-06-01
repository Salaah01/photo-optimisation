import tkinter as tk


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.window = master
        self.window.geometry('750x750')
        self.window.title('Image Optimisation')

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
        file_path = tk.StringVar()
        ent_file = tk.Entry(self.frame_file_upload, textvariable=file_path)
        ent_file.grid(
            row=0,
            column=0,
            padx=(0, 5),
            sticky='w, e'
            )

        # Browse Button
        browse_btn = tk.Button(
            self.frame_file_upload,
            text='Browse',
            width=12
            )
        browse_btn.grid(row=0, column=1)

    def file_list(self):
        files = tk.Listbox(self.frame_file_list, height=6, width=35)
        files.grid(
            row=0,
            column=0,
            sticky='w, e, n, s'
            )

    def optimise_opts(self):
        # Auto Optimise
        opt_auto = tk.Checkbutton(
                        self.frame_optimise_opts,
                        text="Auto Optimise"
                        )
        opt_auto.grid(
            row=0,
            column=0,
            pady=(0, 15),
            columnspan=4
            )

        # Quality
        lbl_quality = tk.Label(self.frame_optimise_opts, text='Quality')
        lbl_quality.grid(
            row=1,
            column=0,
            pady=(0, 0)
            )

        val_quality = tk.IntVar()
        opt_quality = tk.Scale(
            self.frame_optimise_opts,
            from_=0,
            to=100,
            orient='horizontal',
            variable=val_quality,
            )
        opt_quality.grid(
            row=1,
            column=1,
            pady=(0, 15),
            columnspan=3
            )

        # Resize
        val_resize_w = tk.StringVar()
        lbl_resize_w = tk.Label(self.frame_optimise_opts, text='W')
        lbl_resize_w.grid(
            row=3,
            column=0,
            pady=(0, 15)
            )
        opt_resize_w = tk.Entry(
            self.frame_optimise_opts,
            width=5,
            textvariable=val_resize_w
            )
        opt_resize_w.grid(
            row=3,
            column=1,
            pady=(0, 15)
            )

        val_resize_h = tk.StringVar()
        lbl_resize_h = tk.Label(self.frame_optimise_opts, text='H')
        lbl_resize_h.grid(
            row=3,
            column=2,
            pady=(0, 15)
            )
        opt_resize_h = tk.Entry(
                            self.frame_optimise_opts,
                            width=5,
                            textvariable=val_resize_h
                            )
        opt_resize_h.grid(
            row=3,
            column=3,
            pady=(0, 15)
            )

        # Convert
        val_convert = tk.StringVar()
        convert_opts = ['(none)', 'JPEG', 'PNG', 'GIF', 'BMP']
        val_convert.set(convert_opts[0])
        lbl_convert = tk.Label(self.frame_optimise_opts, text="Format")
        lbl_convert.grid(
            row=4,
            column=0,
            pady=(0, 15),
            columnspan=1
            )
        opt_convert = tk.OptionMenu(
                                self.frame_optimise_opts,
                                val_convert,
                                *convert_opts
                                )
        opt_convert.grid(
            row=4,
            column=1,
            pady=(0, 15),
            columnspan=3,
            sticky='w, e'
            )

        # Optimise Button
        btn_optimise = tk.Button(
            self.frame_optimise_opts,
            text='Optimse'
        )
        btn_optimise.grid(row=5, column=0, columnspan=4)

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
