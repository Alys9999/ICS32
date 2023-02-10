#Zhaoyang Lu
#zhaoyal5@ci.edu
#30735594

import tkinter as tk
from tkinter import ttk, filedialog
from Profile import Profile, Post
import ds_client as dsc
import ds_protocol as dsp

"""
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the body portion of the root frame.
"""
class Body(tk.Frame):
    def __init__(self, root, select_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._select_callback = select_callback

        # a list of the Post objects available in the active DSU file
        self._posts = [Post]
        
        # After all initialization is complete, call the _draw method to pack the widgets
        # into the Body instance 
        self._draw()
    
    """
    Update the entry_editor with the full post entry when the corresponding node in the posts_tree
    is selected.
    """
    def node_select(self, event):
        index = int(self.posts_tree.selection()[0])-1 #selections are not 0-based, so subtract one.
        entry = self._posts[index].entry
        self.set_text_entry(entry)
    
    """
    Returns the text that is currently displayed in the entry_editor widget.
    """
    def get_text_entry(self) -> str:
        return self.entry_editor.get('1.0', 'end').rstrip()

    """
    Sets the text to be displayed in the entry_editor widget.
    NOTE: This method is useful for clearing the widget, just pass an empty string.
    """
    def set_text_entry(self, text:str):
        # TODO: Write code to that deletes all current text in the self.entry_editor widget
        # and inserts the value contained within the text parameter.
        self.entry_editor.delete(0.0,"end")
        self.entry_editor.insert(0.0,text)
        
    
    """
    Populates the self._posts attribute with posts from the active DSU file.
    """
    def set_posts(self, posts:list):
        # TODO: Write code to populate self._posts with the post data passed
        # in the posts parameter and repopulate the UI with the new post entries.
        # HINT: You will have to write the delete code yourself, but you can take 
        # advantage of the self.insert_posttree method for updating the posts_tree
        # widget.
        self._posts=posts
        for i in range(len(self._posts)):
            self._insert_post_tree(i+1, self._posts[i])
            
        
            

    """
    Inserts a single post to the post_tree widget.
    """
    def insert_post(self, post: Post):
        self._posts.append(post)
        self._insert_post_tree(len(self._posts), post)

    """
    Resets all UI widgets to their default state. Useful for when clearing the UI is neccessary such
    as when a new DSU file is loaded, for example.
    """
    def reset_ui(self):
        self.set_text_entry("")
        self._posts = []
        for item in self.posts_tree.get_children():
            self.posts_tree.delete(item)

    """
    Inserts a post entry into the posts_tree widget.
    """
    def _insert_post_tree(self, id, post: Post):
        entry = post.entry
        # Since we don't have a title, we will use the first 24 characters of a
        # post entry as the identifier in the post_tree widget.
        if len(entry) > 25:
            entry = entry[:24] + "..."
        entry=entry.replace("\n",'')
        self.posts_tree.insert('', id, id, text=entry)

    
    """
    Call only once upon initialization to add widgets to the frame
    """
    def _draw(self):
        posts_frame = tk.Frame(master=self, width=250)
        posts_frame.pack(fill=tk.BOTH, side=tk.LEFT)
        self.posts_tree = ttk.Treeview(posts_frame)
        self.posts_tree.bind("<<TreeviewSelect>>", self.node_select)
        self.posts_tree.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)

        entry_frame = tk.Frame(master=self, bg="")
        entry_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        
        editor_frame = tk.Frame(master=entry_frame, bg="red")
        editor_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        
        scroll_frame = tk.Frame(master=entry_frame, bg="blue", width=10)
        scroll_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=False)
        
        self.entry_editor = tk.Text(editor_frame, width=10)
        self.entry_editor.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=0, pady=0)

        entry_editor_scrollbar = tk.Scrollbar(master=scroll_frame, command=self.entry_editor.yview)
        self.entry_editor['yscrollcommand'] = entry_editor_scrollbar.set
        entry_editor_scrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=False, padx=0, pady=0)

"""
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the footer portion of the root frame.
"""
class Footer(tk.Frame):
    def __init__(self, root, save_callback=None, online_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._save_callback = save_callback
        self._online_callback=online_callback
        # IntVar is a variable class that provides access to special variables
        # for Tkinter widgets. is_online is used to hold the state of the chk_button widget.
        # The value assigned to is_online when the chk_button widget is changed by the user
        # can be retrieved using he get() function:
        # chk_value = self.is_online.get()
        self.is_online = tk.IntVar()
        # After all initialization is complete, call the _draw method to pack the widgets
        # into the Footer instance 
        self._draw()
    
    """
    Calls the callback function specified in the online_callback class attribute, if
    available, when the chk_button widget has been clicked.
    """
    def online_click(self):
        # TODO: Add code that implements a callback to the chk_button click event.
        # The callback should support a single parameter that contains the value
        # of the self.is_online widget variable.
        check=self.is_online.get()
        
        if self._online_callback is not None:
            self._online_callback(check)

    """
    Calls the callback function specified in the save_callback class attribute, if
    available, when the save_button has been clicked.
    """
    def save_click(self):
        if self._save_callback is not None:
            self._save_callback()

    """
    Updates the text that is displayed in the footer_label widget
    """
    def set_status(self, message):
        self.footer_label.configure(text=message)
    
    """
    Call only once upon initialization to add widgets to the frame
    """
    def _draw(self):
        save_button = tk.Button(master=self, text="Save Post", width=20)
        save_button.configure(command=self.save_click)
        save_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)

        self.chk_button = tk.Checkbutton(master=self, text="Online", variable=self.is_online)
        self.chk_button.configure(command=self.online_click) 
        self.chk_button.pack(fill=tk.BOTH, side=tk.RIGHT)

        self.footer_label = tk.Label(master=self, text="Ready.")
        self.footer_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=5)
        

"""
the sub class of tk.Frame that works all about the setting option window
"""
class Setting(tk.Frame):
    
    def __init__(self, root,profile: Profile,get_callback):
        tk.Frame.__init__(self, root)
        self.root = root
        self.profile=profile
        self._get_info=get_callback
        self._draw()
        

    
    def get_click(self):
        if self._get_info is not None:
            self._get_info()


#set the label of the window
    def set_lab(self):
        self.username_la=tk.Label(self.root, text="username: " + str(self.profile.username))
        self.password_la=tk.Label(self.root, text="password: " + str(self.profile.password))
        
        
    
    def _draw(self):

        
        sign1=tk.Label(self.root, text="Original setting")
        sign2=tk.Label(self.root, text="Input the info you want here")
        self.set_lab()


        self.username_input=tk.Text(self.root,height=1,width=30)
        self.password_input=tk.Text(self.root,height=1,width=30)
        
        self.save_info_button=tk.Button(master=self.root, text="Save Setting", width=20)
        self.save_info_button.configure(command=self.get_click)
        self.save_info_button.place(x=350,y=250)
        
        sign1.place(x=10,y=10)
        sign2.place(x=250,y=10)
        
        self.username_la.place(x=10,y=150)
        self.password_la.place(x=10,y=200)

        self.username_input.place(x=250,y=150)
        self.password_input.place(x=250,y=200)
        

"""
the sub class of tk.Frame that works all about the server option window
"""
class Server(tk.Frame):
    
    def __init__(self, root,profile: Profile,server_callback):
        tk.Frame.__init__(self, root)
        self.root = root
        self.profile=profile
        self._server_info=server_callback
        self._draw()
        

    
    def server_click(self):
        if self._server_info is not None:
            self._server_info()


#set the label of the window        
    def set_s_lab(self):
        self.server_la=tk.Label(self.root, text="server ip: " + str(self.profile.dsuserver))
        self.port_la=tk.Label(self.root, text="port: " + str(self.profile.port))

        
        
    
    def _draw(self):

        
        sign1=tk.Label(self.root, text="Original setting")
        sign2=tk.Label(self.root, text="Input the info you want here")
        self.set_s_lab()

        self.server_input=tk.Text(self.root,height=1,width=30)
        self.port_input=tk.Text(self.root,height=1,width=30)

        
        self.save_info_button=tk.Button(master=self.root, text="Save Setting", width=20)
        self.save_info_button.configure(command=self.server_click)
        self.save_info_button.place(x=350,y=250)
        
        sign1.place(x=10,y=10)
        sign2.place(x=250,y=10)
        
        self.server_la.place(x=10,y=50)
        self.port_la.place(x=10,y=100)

        
        self.server_input.place(x=250,y=50)
        self.port_input.place(x=250,y=100)
        
        
"""
the sub class of tk.Frame that works all about the bio option window
"""
class Bio(tk.Frame):
    
    def __init__(self, root,profile: Profile,bio_callback):
        tk.Frame.__init__(self, root)
        self.root = root
        self.profile=profile
        self._bio_callback=bio_callback
        self._draw()
        

#set the label of the window    
    def bio_click(self):
        if self._bio_callback is not None:
            self._bio_callback()

        
        
    
    def _draw(self):
        ori_frame = tk.Frame(master=self.root, height=250)
        ori_frame.pack(fill=tk.BOTH, side=tk.TOP)
        ori_la=tk.Label(ori_frame, text="original bio: " + str(self.profile.bio))
        ori_la.pack(fill=tk.BOTH, side=tk.LEFT,expand=True)

        inp_frame=tk.Frame(master=self.root, height=250)
        inp_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        self.bio_input=tk.Text(inp_frame,height=1,width=30)
        self.bio_input.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        click_frame=tk.Frame(master=self.root, height=50)
        click_frame.pack(fill=tk.BOTH, side=tk.BOTTOM)
        self.save_info_button=tk.Button(master=click_frame, text="Save Bio", width=20)
        self.save_info_button.configure(command=self.bio_click)
        self.save_info_button.pack(side=tk.RIGHT)
        





"""
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the main portion of the root frame. Also manages all method calls for
the Profile class.
"""
class MainApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root

        # Initialize a new Profile and assign it to a class attribute.
        self._current_profile = Profile()
        self._is_online=False
        self._profile_filename=None
        self.has_profile=False

        # After all initialization is complete, call the _draw method to pack the widgets
        # into the root frame
        self._draw()

    """
    Creates a new DSU file when the 'New' menu item is clicked.
    """
    def new_profile(self):
        filename = tk.filedialog.asksaveasfile(filetypes=[('Distributed Social Profile', '*.dsu')])
        if filename==None:
            return 
        while True:
            name=filename.name
            suff=name[-4:]
            if suff!= ".dsu":
                tk.messagebox.showinfo("warning", "Filename needs to end with .dsu")
            else:
                break
            
        self._profile_filename = filename.name
        self._current_profile=Profile()
        self.has_profile=True
        self.body.reset_ui()

        # TODO Write code to perform whatever operations are necessary to prepare the UI for
        # a new DSU file.
        # HINT: You will probably need to do things like generate encryption keys and reset the ui.
    
    """
    Opens an existing DSU file when the 'Open' menu item is clicked and loads the profile
    data into the UI.
    """
    def open_profile(self):
        filename = tk.filedialog.askopenfile(filetypes=[('Distributed Social Profile', '*.dsu')])
        if filename ==None:
            return
        # TODO: Write code to perform whatever operations are necessary to prepare the UI for
        # an existing DSU file.
        # HINT: You will probably need to do things like load a profile, import encryption keys 
        # and update the UI with posts.
        self._profile_filename=filename.name
        self._current_profile=Profile()
        self._current_profile.load_profile(self._profile_filename)
        self.has_profile=True
        self.body.reset_ui()
        p=self._current_profile.get_posts()
        self.body.set_posts(p)
        
    
    """
    Closes the program when the 'Close' menu item is clicked.
    """
    def close(self):
        self.root.destroy()

    """
    Saves the text currently in the entry_editor widget to the active DSU file.
    """
    def save_profile(self):
        # TODO: Write code to perform whatever operations are necessary to save a 
        # post entry when the user clicks the save_button widget.
        # HINT: You will probably need to do things like create a new Post object,
        # fill it with text, add it to the active profile, save the profile, and
        # clear the editor_entry UI for a new post.
        # This might also be a good place to check if the user has selected the online
        # checkbox and if so send the message to the server.
        
        message=self.body.get_text_entry()
        'have message'
        if message!="":
            post=Post(message)
            
            if self.has_profile==True:
                
                self.body.insert_post(post)
                self._current_profile.add_post(post)
                
                if self._is_online==1:
                    server=self._current_profile.dsuserver
                    port=self._current_profile.port
                    un=self._current_profile.username
                    pw=self._current_profile.password
                    bio=self._current_profile.bio

                    re=dsc.send(server,port,un,pw,message,bio)
                    if re:
                        tk.messagebox.showinfo("warning", re)
                    
                self._current_profile.save_profile(self._profile_filename)
                self.body.set_text_entry("")
            else:
                tk.messagebox.showinfo("warning", "please load or new a profile first")

    """
    A callback function for responding to changes to the online chk_button.
    """
    def online_changed(self, value:bool):
        # TODO: 
        # 1. Remove the existing code. It has been left here to demonstrate
        # how to change the text displayed in the footer_label widget and
        # assist you with testing the callback functionality (if the footer_label
        # text changes when you click the chk_button widget, your callback is working!).
        # 2. Write code to support only sending posts to the DSU server when the online chk_button
        # is checked.
        self._is_online=value
        #print(self._is_online)
        
        if value == 1:
            self.footer.set_status("Online")
        else:
            self.footer.set_status("Offline")
            
            
        """
        after the click of save button in setting, take the text entry and assign it to _current_profile, if the text is
        empty, the correspondent attribute in _current_profile does not change. close the window when everything down
        the next three function works similarly
        """
    def get_info(self):
        username_c=self.setted.username_input.get('1.0', 'end')
        username_c=username_c.replace("\n","")
        if username_c == '':
            username_c=self._current_profile.username
        password_c=self.setted.password_input.get('1.0', 'end')
        password_c=password_c.replace("\n","")
        if password_c == '':
            password_c=self._current_profile.password
        self._current_profile.renew_info(self._current_profile.dsuserver,self._current_profile.port,username_c,password_c)
        tk.messagebox.showinfo("Yes", "info set!")
        self.setting_window.destroy()
   
   
   
    def get_server(self):
        dsuserver_c=self.ser.server_input.get('1.0', 'end')
        dsuserver_c=dsuserver_c.replace("\n","")
        if dsuserver_c == '':
            dsuserver_c=self._current_profile.dsuserver
        port_c=self.ser.port_input.get('1.0', 'end')
        port_c=port_c.replace("\n","")
        if port_c == '':
            port_c=self._current_profile.port
        self._current_profile.renew_info(dsuserver_c,port_c,self._current_profile.username,self._current_profile.password)
        tk.messagebox.showinfo("Yes", "Server set!")
        self.server_window.destroy()
        

    def get_bio(self):
        bio_c=self.bio.bio_input.get('1.0', 'end')
        bio_c=bio_c.replace("\n","")
        if bio_c == '':
            bio_c=self._current_profile.dsuserver
        self._current_profile.add_bio(bio_c)
        tk.messagebox.showinfo("Yes", "Bio set!")
        self.bio_window.destroy()

            
            
        """
        have a top level window with the correspondent option
        """
    def current_setting(self):
        self.setting_window=tk.Toplevel(self.root)
        
        self.setted=Setting(self.setting_window,self._current_profile, get_callback=self.get_info)
        self.setting_window.geometry("600x300")
        self.setting_window.resizable(0,0)
        
        self.setting_window.update()
        self.setting_window.mainloop()

        'self._current_profile=Profile(self.setted.dsuserver,port,setted.username,setted.password)'

    def current_server(self):
        self.server_window=tk.Toplevel(self.root)
        
        self.ser=Server(self.server_window,self._current_profile, server_callback=self.get_server)
        self.server_window.geometry("600x300")
        self.server_window.resizable(0,0)
        
        self.server_window.update()
        self.server_window.mainloop()

        

    def open_bio(self):
        self.bio_window=tk.Toplevel(self.root)
        
        self.bio=Bio(self.bio_window,self._current_profile, bio_callback=self.get_bio)
        self.bio_window.geometry("600x600")
        self.bio_window.minsize(self.bio_window.winfo_width(), self.bio_window.winfo_height())
        
        self.bio_window.update()
        self.bio_window.mainloop()

        
            
    
    """
    Call only once, upon initialization to add widgets to root frame
    """
    def _draw(self):
        # Build a menu and add it to the root frame.
        menu_bar = tk.Menu(self.root)
        self.root['menu'] = menu_bar
        menu_file = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New', command=self.new_profile)
        menu_file.add_command(label='Open...', command=self.open_profile)
        menu_file.add_command(label='Close', command=self.close)
        menu_file.add_command(label="Setting", command=self.current_setting)
        menu_file.add_command(label="Server", command=self.current_server)
        menu_file.add_command(label="Bio", command=self.open_bio)
        # NOTE: Additional menu items can be added by following the conventions here.
        # The only top level menu item is a 'cascading menu', that presents a small menu of
        # command items when clicked. But there are others. A single button or checkbox, for example,
        # could also be added to the menu bar. 

        # The Body and Footer classes must be initialized and packed into the root window.
        self.body = Body(self.root, self._current_profile)
        self.body.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        
        
        
        # TODO: Add a callback for detecting changes to the online checkbox widget in the Footer class. Follow
        # the conventions established by the existing save_callback parameter.
        # HINT: There may already be a class method that serves as a good callback function!
        self.footer = Footer(self.root, save_callback=self.save_profile, online_callback=self.online_changed)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)

if __name__ == "__main__":
    # All Tkinter programs start with a root window. We will name ours 'main'.
    main = tk.Tk()

    # 'title' assigns a text value to the Title Bar area of a window.
    main.title("ICS 32 Distributed Social")

    # This is just an arbitrary starting point. You can change the value around to see how
    # the starting size of the window changes. I just thought this looked good for our UI.
    main.geometry("720x720")

    # adding this option removes some legacy behavior with menus that modern OSes don't support. 
    # If you're curious, feel free to comment out and see how the menu changes.
    main.option_add('*tearOff', False)

    # Initialize the MainApp class, which is the starting point for the widgets used in the program.
    # All of the classes that we use, subclass Tk.Frame, since our root frame is main, we initialize 
    # the class with it.
    MainApp(main)

    # When update is called, we finalize the states of all widgets that have been configured within the root frame.
    # Here, Update ensures that we get an accurate width and height reading based on the types of widgets
    # we have used.
    # minsize prevents the root window from resizing too small. Feel free to comment it out and see how
    # the resizing behavior of the window changes.
    main.update()
    main.minsize(main.winfo_width(), main.winfo_height())
    # And finally, start up the event loop for the program (more on this in lecture).
    main.mainloop()
