class friend:
    count = 0

    def __init__(self, name="",lname="", hobbies=[], mob=0, email="", bdate="", address=""):
        friend.count = friend.count + 1
        self.__fid = "F" + str(friend.count)
        self.__name = name
        self.__lname = lname
        self.__hobbies = hobbies
        self.__mob = mob
        self.__email = email
        self.__bdate = bdate
        self.__address = address

    def __str__(self):
        str1 = f"""
        Friend Details
        __________________
        
        Friend id : {self.__fid}
        Name: {self.__name}
        Last Name : {self.__lname}
        hobbies : {self.__hobbies}
        Mob No. : {self.__mob}
        Email : {self.__email}
        Birth date : {self.__bdate}
        Address : {self.__address}"""

        return str1
    

    # getter methods
    def get_fid(self):
        return self.__fid

    def get_name(self):
        return self.__name

    def get_lname(self):
        return self.__lname

    def get_hobbies(self):
        return self.__hobbies

    def get_mob(self):
        return self.__mob
    
    def get_email(self):
        return self.__email
    
    def get_bdate(self):
        return self.__bdate
    
    def get_address(self):
        return self.__address
    

    # setter methods
    def set_name(self, name):
        self.__name = name

    def set_lname(self, lname):
        self.__lname = lname

    def set_hobbies(self, hobbies):
        self.__hobbies = hobbies

    def set_mob(self, mob):
        self.__mob = mob
        
    def set_email(self, email):
        self.__email = email
        
    def set_bdate(self, bdate):
        self.__bdate = bdate
        
    def set_address(self, address):
        self.__address = address
