class User:
    """
    class that generates username and password of users 
    """
    user_list = [] 

    def __init__(self,username,password):

        """
        use __init__ method and define properties 
        """
        self.username = username
        self.password = password

    def save_user(self):

        """
        save_user method to saves users object into user list
        """
        User.user_list.append(self)


    @classmethod
    def display_user(cls):
        """
        display user method to display list of user
        """
        return cls.user_list

    def delete_user(self):
        """
        delete user method to delete user object on the list
        """
      
        User.user_list.remove(self)

    
