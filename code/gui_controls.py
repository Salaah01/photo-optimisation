import img_extentions
import os

def insert_files(filenames, listbox, listbox_items):
    """
    Function will insert files when user either browses or adds files manually.
    """
    invalid_files = []
    for filename in filenames:

        # Only add files which are not already in the list
        if not(filename in listbox_items):

            # If the file is valid add it to the list, if the file is not valid then append it to invalid files an add it to the list at the end with the respective information.
            if os.path.splitext(filename)[1].lower() in img_extentions.extentions:
                listbox.insert(0, filename)
            else:
                invalid_files.append('<<INVALID FILETYPE>> ' + filename)
            
    # Append the invalid list items to the list

    for invalid_file in invalid_files:
        listbox.insert(0, invalid_file)
        listbox.itemconfig(0, {'fg': 'red'})

    return invalid_files

def insert_single_file(filename, listbox, listbox_items, info_label, entry_box_field):
    """
    Function will insert a file when user adds a file manaully
    """
    # If file is already in the list, then do not return and ouput a message.
    if filename:
        if filename in listbox_items:
            info_label.config(text="File has already been imported", fg='red')

        # If it is not in the list and exists the continue
        elif os.path.isfile(filename):

            # If the file is a valid filetype add it to the list, otherwise add it with an error prefix
            if os.path.splitext(filename)[1].lower() in img_extentions.extentions:
                listbox.insert(0, filename)
            else:
                listbox.insert(0, '<<INVALID FILETYPE>> ' + filename)
                listbox.itemconfig(0, {'fg': 'red'})
        
        # File path does not exist
        else:
            entry_box_field.set('FILE DOES NOT EXIST')
    