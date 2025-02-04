class mobiles():
    brandname="samsung"
    brandcolor="white"
    storage="128gb"
    def calling(self,brand):
        print("your calling....",brand)
    def camera(self):
        print("capturing phto")
    def browsing(self):
        print("your are browsing ")
        self.camera()
      
samsung=mobiles()
samsung.calling("samsung") 
samsung.camera()
samsung.browsing()

class car():
    def __init__(self,brandname,color,model):
        self.brandname=brandname
        self.color=color
        self.model=model
    def driving(self,):
        print(f"your are driviing from {self.brandname} car")
    def on_off(self):
        print("start/off")     
tata=car("tata","black","tata123")
tata.driving()
tata. on_off()     
# ========================inheritance============================================
class mobiles():
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def  make_call(self,number):
        print(f"callinf {number} from {self.brand}{self.model}")
    def send_message(self,number,message):
        print(f"sending {message} from {number}{self.brand}{self.model}") 



class smartphone(mobiles):
    def browsing(self):
        print(f"browsing internet on{self.brand} ,{self.model}")
    def apps(self,appname):
        print(f"using {appname} app on{self.brand}, {self.model}")
sphone=smartphone("apple","iphone16")
sphone.make_call("9491835674")     
sphone.send_message("113","hello")
sphone.apps("whatsup")
sphone.browsing()   
#--------------------multilevel inheritance-----------------------
class grandfather():
    def output(self):
        print(f"this is grand father class")
class father(grandfather):
    def outputf(self):
        print(f"this is fatheerclass")
class child(father):
    def outputchild(father):
        print("this is a child class ")
      
object=child()
object.output()     
# ---------------------------------multiple inheritance-------------------------
class parent01():
    def father(self):
        print("this is father class")    
class parent02():
    def mother(self):
        print("this is mother class")   
class child(parent01,parent02):
    def child(self):
        print("this is child class") 
object=child()
object.mother()
object.father()
#-------------------------------hiearichal inheritance ---------------------
class a():
    def father(self):
        print("this is father class") 
class b(a):
    def child(self):
        print("this is father class")
class c(a):
    def child(self):
        print("this is child class") 
object=b()
object.child()
object.father()
object=c()
object.child()
object.father()      
# ====================polymorphisam======================================
class example:
   def add(self, a, b):
      x = a+b
      return x
   def add(self, a, b, c=0):
      x = a+b+c
      return x

obj = example()

print (obj.add(10,20,30))
print (obj.add(10,20))
#--------------------------method overiding-----------------------------
class father():
    def details(self,a):
        print("this is base clsss",a)
class child(father):
    def details(self,a):
        print("this is derived class")  
        super().details("100cr")
object=child()
object.details("100cr")                  








             
        
