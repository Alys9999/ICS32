#Zhaoyang Lu
#zhaoyal5@ci.edu
#30735594

import tkinter as tk
from tkinter import ttk, filedialog
import ds_protocol as dsp
from ds_messenger import DirectMessage as DM
from ds_messenger import DirectMessenger as DMer
import time

"""
raise when the friend already exist
"""
class FriendAlreadyExist(Exception):
    pass


"""
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the body portion of the root frame.
"""
class Body(tk.Frame):
    def __init__(self, root, dsmer=None, get_mess_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._ds_mer = dsmer
        self._users=[]
        # After all initialization is complete, call the _draw method to pack the widgets
        # into the Body instance 
        self._draw()
        
    #take in the index as a attribut
    def node_index(self):
        i=self.friend_tree.selection()[0].replace('I','')
        self.index = int(i) -1#selections are not 0-based, so subtract one.
    
    #take in the self.index and make selection
    def node_select(self, event):
        self.show_box.delete(0.0,"end")
        self.node_index()
        entry=self._ds_mer.pairing_dict.values()
        entry_list=[]
        for x in entry:
            entry_list.append(x)
        for y in entry_list[self.index]:
            date_time=y['timestamp']
            try:
                text=str('sent at:'+date_time+' by '+y['sender']+'\n'+y['entry']+"\n\n")
                self.show_box.insert(0.0,text)
            except TypeError:
                pass



    
    def get_message(self) -> str:
        """
        Returns the text that is currently displayed in the input frame widget.
        """
        return self.entry_editor.get('1.0', 'end').rstrip()
    
    """
    Sets the text to be displayed in the entry_editor widget.
    NOTE: This method is useful for clearing the widget, just pass an empty string.
    """
    def set_text_entry(self,text:str):
        # TODO: Write code to that deletes all current text in the self.entry_editor widget
        # and inserts the value contained within the text parameter.
        
        self.show_box.delete(0.0,"end")
        self.show_box.insert(0.0,text)
        
    def delete_fri_tree(self):
        # delete the whole tree
        for x in self.friend_tree.get_children():
            self.friend_tree.delete(x)        
        
    def insert_friend(self):
        #insert friends in the pairing_dict
        k=list(self._ds_mer.pairing_dict.keys())
        for x in k:
            self.insert_friend_tree(len(k),x)
        

       
            
    def insert_friend_tree(self,id,message):
        #the actual insert function
        try:
            self.friend_tree.insert('',id,id,text=message)
        except tk._tkinter.TclError:
            raise FriendAlreadyExist()

    
    """
    Call only once upon initialization to add widgets to the frame
    """
    def _draw(self):
        """
        the left part
        """
        friend_frame = tk.Frame(master=self, width=250)
        friend_frame.pack(fill=tk.BOTH, side=tk.LEFT)
        self.friend_tree = ttk.Treeview(friend_frame)
        self.friend_tree.bind("<<TreeviewSelect>>", self.node_select)
        self.friend_tree.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5, pady=5)
        #the frame for the whole right part
        entry_frame = tk.Frame(master=self, bg="")
        entry_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        #the frame for the input box
        editor_frame = tk.Frame(master=entry_frame, bg="grey")
        editor_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=5, pady=5)
        #the frame for the show box
        show_frame = tk.Frame(master=editor_frame, bg="white")
        show_frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        #the widget for the input
        input_frame = tk.Frame(master=editor_frame, bg="white")
        input_frame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=False, padx=5, pady=5)
        
        scroll_frame = tk.Frame(master=show_frame, bg="blue", width=10)
        scroll_frame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=False)
        
        self.show_box=tk.Text(master=show_frame)
        self.show_box.bind("<Key>", lambda e: "break")
        self.show_box.pack(fill=tk.BOTH,side=tk.LEFT, expand=True, padx=5)
        
        self.entry_editor = tk.Text(input_frame, height=5)
        self.entry_editor.pack(fill=tk.X, side=tk.BOTTOM, expand=False, padx=0, pady=0)

        entry_editor_scrollbar = tk.Scrollbar(master=scroll_frame, command=self.entry_editor.yview)
        self.entry_editor['yscrollcommand'] = entry_editor_scrollbar.set
        entry_editor_scrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=False, padx=0, pady=0)
        

"""
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the footer portion of the root frame.
"""
class Footer(tk.Frame):
    def __init__(self, root, online_callback=None, send_callback=None, add_callback=None):
        tk.Frame.__init__(self, root)
        self.root = root
        self._send_callback = send_callback
        self._add_callback=add_callback
        self._online_callback=online_callback
        
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
    Updates the text that is displayed in the footer_label widget
    """
    def set_status(self, message):
        self.footer_label.configure(text=message)


    """
    Calls the callback function specified in the save_callback class attribute, if
    available, when the save_button has been clicked.
    """
    def send_click(self):
        if self._send_callback is not None:
            self._send_callback()
            
    def add_user(self):
        if self._add_callback is not None:
            self._add_callback()

    
    """
    Call only once upon initialization to add widgets to the frame
    """
    def _draw(self):
        send_button = tk.Button(master=self, text="Send", width=20)
        send_button.configure(command=self.send_click)
        send_button.pack(fill=tk.BOTH, side=tk.RIGHT, padx=5, pady=5)
        
        self.add_user_button = tk.Button(master=self, text="Add Friend", width=15)
        self.add_user_button.configure(command=self.add_user) 
        self.add_user_button.pack(fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)
        
        self.chk_button = tk.Checkbutton(master=self, text="Online", variable=self.is_online)
        self.chk_button.configure(command=self.online_click) 
        self.chk_button.pack(fill=tk.BOTH, side=tk.RIGHT)

        self.footer_label = tk.Label(master=self, text="Ready.")
        self.footer_label.pack(fill=tk.BOTH, side=tk.LEFT, padx=5)

        

"""
the sub class of tk.Frame that works all about the setting option window
"""
class Setting(tk.Frame):
    
    def __init__(self, root,DMer,get_callback):
        tk.Frame.__init__(self, root)
        self.root = root
        self._DMer=DMer
        #callback
        self._get_info=get_callback
        #draw
        self._draw()
        

    
    def get_click(self):
        if self._get_info is not None:
            self._get_info()


    #set the label of the window
    def set_lab(self):
        self.username_la=tk.Label(self.root, text="username: " + str(self._DMer.username))
        self.password_la=tk.Label(self.root, text="password: " + str(self._DMer.password))
        
        
    
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
the window is working but I cannot test the send operation for there is no other ip
"""

class Server(tk.Frame):
    
    def __init__(self, root,dsMer:DMer,server_callback):
        tk.Frame.__init__(self, root)
        self.root = root
        self._account=dsMer
        self._server_info=server_callback
        self._draw()

    #set the label of the window        
    def set_s_lab(self):
        self.server_la=tk.Label(self.root, text="server ip: " + str(self._account.dsuserver))
        
    def server_click(self):
        if self._server_info is not None:
            self._server_info()
    
    def _draw(self):

        
        sign1=tk.Label(self.root, text="Original setting")
        sign2=tk.Label(self.root, text="Input the info you want here")
        self.set_s_lab()

        self.server_input=tk.Text(self.root,height=1,width=30)
        
        self.save_info_button=tk.Button(master=self.root, text="Save Setting", width=20)
        self.save_info_button.configure(command=self.server_click)
        self.save_info_button.place(x=350,y=250)
        
        sign1.place(x=10,y=10)
        sign2.place(x=250,y=10)
        
        self.server_la.place(x=10,y=50)
        
        self.server_input.place(x=250,y=50)
        
class Add_user(tk.Frame):
    
    def __init__(self, root,dsMer:DMer,add_U_callback):
        tk.Frame.__init__(self, root)
        self.root = root
        self._account=dsMer
        self._add_friend=add_U_callback
        self._draw()
        
    def _add_friend_click(self):
        if self._add_friend is not None:
            self._add_friend()
    
    def _draw(self):

        
        sign1=tk.Label(self.root, text="Add a friend here:")

        self.friend_input=tk.Text(self.root,height=1,width=30)
        
        self.save_info_button=tk.Button(master=self.root, text="Add Friend", width=20)
        self.save_info_button.configure(command=self._add_friend_click)
        self.save_info_button.place(x=350,y=250)
        
        sign1.place(x=10,y=10)
        
        self.friend_input.place(x=250,y=10)
       
        

"""
A subclass of tk.Frame that is responsible for drawing all of the widgets
in the main portion of the root frame. Also manages all method calls for
the Profile class.
"""
class MainApp(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self._current_account=DMer()
        self._is_online=False
        self.showing=self._current_account.retrieve_all()
        self._draw()
        
    def add_friend_button(self):
        #for the window of the add friend
        self.add_user_window=tk.Toplevel(self.root)
        
        self.add_user=Add_user(self.add_user_window,self._current_account, add_U_callback=self.add_friend)
        self.add_user_window.geometry("600x300")
        self.add_user_window.resizable(0,0)
        
        self.add_user_window.update()
        self.add_user_window.mainloop()
        
    def add_friend(self):
        '''
        send username get from class Add_user to Body class, or callback the method to do it in mainapp
        '''
        if self._is_online==1:
            try:
                new_friend_input=self.add_user.friend_input.get('1.0', 'end')
                new_friend_input=new_friend_input.replace('\n','')
                new_friend=DM(sender=new_friend_input, recipient=self._current_account.username)

                self._current_account._friend_message.append(new_friend)
                self._current_account.make_pair()
                k=list(self._current_account.pairing_dict.keys())
                self.body.insert_friend_tree(len(k),k[-1])
                self.add_user_window.destroy()
            except FriendAlreadyExist:
                tk.messagebox.showinfo("Warning", "The Friend You Want to Add Already Exist.")
        else:
            tk.messagebox.showinfo("Warning", "Add a friend after you are online!")

        
       
    def send_mess(self):
        #send message
        if self._is_online==1:
            ind = self.body.index
            entry=self.body.get_message()
            i=list(self._current_account.pairing_dict.keys())
            recipient=i[ind]
            r=self._current_account.send(entry,recipient)
            self.body.entry_editor.delete(0.0,"end")
        else:
            pass
        
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
        
        if value == 1:
            self.footer.set_status("Online")
            self._current_account.join()
            self._current_account.retrieve_all()
            self._current_account.make_pair()
            self.body.insert_friend()
                
        else:
            self._current_account._friend_message=[]
            self._current_account.pairing_dict=[]
            self.body.delete_fri_tree()
            self.body.set_text_entry('')
            self.footer.set_status("Offline")
            
    def get_server(self):
        #the operation for have server info changed
        dsuserver_c=self.ser.server_input.get('1.0', 'end')
        dsuserver_c=dsuserver_c.replace("\n","")
        if dsuserver_c == '':
            dsuserver_c=self._current_account.dsuserver
        port_c=self.ser.port_input.get('1.0', 'end')
        port_c=port_c.replace("\n","")
        if port_c == '':
            port_c=self._current_account.port
        self._current_account.renew_info(dsuserver_c,self._current_account.username,self._current_account.password)
        tk.messagebox.showinfo("Yes", "Server set!")
        self.server_window.destroy()
                
                
    def get_info(self):
        #the operation for have info changed
        username_c=self.setted.username_input.get('1.0', 'end')
        username_c=username_c.replace("\n","")
        if username_c == '':
            username_c=self._current_account.username
        password_c=self.setted.password_input.get('1.0', 'end')
        password_c=password_c.replace("\n","")
        if password_c == '':
            password_c=self._current_account.password
        self._current_account.renew_info(self._current_account.dsuserver,username_c,password_c)
        self.body.set_text_entry('')
        self.body.delete_fri_tree()
        tk.messagebox.showinfo("Yes", "info set!")
        self.setting_window.destroy()        
        

        """
        have a top level window with the correspondent option
        """
    def current_setting(self):
        self.setting_window=tk.Toplevel(self.root)
        
        self.setted=Setting(self.setting_window,self._current_account, get_callback=self.get_info)
        self.setting_window.geometry("600x300")
        self.setting_window.resizable(0,0)
        
        self.setting_window.update()
        self.setting_window.mainloop()



    def current_server(self):
        self.server_window=tk.Toplevel(self.root)
        
        self.ser=Server(self.server_window,self._current_account, server_callback=self.get_server)
        self.server_window.geometry("600x300")
        self.server_window.resizable(0,0)
        
        self.server_window.update()
        self.server_window.mainloop()

    """
    Call only once, upon initialization to add widgets to root frame
    """
    def _draw(self):
        # Build a menu and add it to the root frame.
        menu_bar = tk.Menu(self.root)
        self.root['menu'] = menu_bar
        menu_file = tk.Menu(menu_bar)
        menu_bar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label="Setting", command=self.current_setting)
        # NOTE: Additional menu items can be added by following the conventions here.
        # The only top level menu item is a 'cascading menu', that presents a small menu of
        # command items when clicked. But there are others. A single button or checkbox, for example,
        # could also be added to the menu bar. 

        # The Body and Footer classes must be initialized and packed into the root window.
        self.body = Body(self.root, self._current_account)
        self.body.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
        
        
        
        # TODO: Add a callback for detecting changes to the online checkbox widget in the Footer class. Follow
        # the conventions established by the existing save_callback parameter.
        # HINT: There may already be a class method that serves as a good callback function!
        self.footer = Footer(self.root, online_callback=self.online_changed, send_callback=self.send_mess, add_callback=self.add_friend_button)
        self.footer.pack(fill=tk.BOTH, side=tk.BOTTOM)

if __name__ == "__main__":
    # All Tkinter programs start with a root window. We will name ours 'main'.
    main = tk.Tk()

    # 'title' assigns a text value to the Title Bar area of a window.
    main.title("ICS 32 Messenger Demo")

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
