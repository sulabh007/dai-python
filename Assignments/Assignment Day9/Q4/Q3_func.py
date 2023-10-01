from Q3_class import *

friend_details = {}
ob= friend("Kishor","Rane",["Running"],9876543210,"Kishor@email.com",'12-4-1998','Race street')
friend_details[ob.get_fid()] = ob
ob1= friend("Ramesh","Bhosle",["Running","Reading"],98456543210,"Ramesh@email.com",'12-5-1996','Bhosle colony')
friend_details[ob1.get_fid()] = ob1




def displayall():
    for friend in friend_details:
        print(friend_details[friend])


def addnewfriend(name,lname, hobbies, mob, email, bdate, address):
    ob = friend(name,lname, hobbies, mob, email, bdate, address)
    friend_details[ob.get_fid()] = ob

    
def searchbyid(fid) :
    value=friend_details.get(fid)
    if value:
        print(friend_details[fid])
    else:
        print("fid not found")

    
def searchbyname(name):
    for fname in friend_details.values():
        print(fname.get_name())
        if name==fname.get_name():
            return fname
    return -1

def searchbyhobby(hobby):
    flag=0
    for hob in friend_details.values():
        for i in range(len(hob.get_hobbies())):
            if hobby==(hob.get_hobbies())[i]:
                print(hob)
                flag=1
                
    if flag==1:
        return 1
                
    return -1
        
    

        
        
        
    
