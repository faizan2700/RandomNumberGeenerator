def load_friends(self):
        all_users = self.requester.get_all_users()

        for user in all_users:
            if user['username'] != self.username:
                friend_frame = ttk.Frame(self.canvas_frame)

                profile_photo = tk.PhotoImage(file="images/avatar.png")
                profile_photo_label = ttk.Label(friend_frame, image=profile_photo)
                profile_photo_label.image = profile_photo

                friend_name = ttk.Label(friend_frame, text=user['real_name'], anchor=tk.W)

                message_this_friend = partial(self.open_chat_window, username=user["username"], real_name=user["real_name"])

                message_button = ttk.Button(friend_frame, text="Chat", command=message_this_friend)

                profile_photo_label.pack(side=tk.LEFT)
                friend_name.pack(side=tk.LEFT)
                message_button.pack(side=tk.RIGHT)

                friend_frame.pack(fill=tk.X, expand=1) 
