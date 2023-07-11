from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.


'''
There are Total 4 functions here:
1) Register new account (Signin)
2) Activating one registered account (Login)
3) Deactivating one registered account (Logout)
4) Destroying a registered account (Sinout)


The relation is:
Signin -> Login-> Logout -> Sinout
   |                           ^
   |___________________________|
'''


Logged_In=set() # Creating a set of Logged (means already Signed and ACTIVE ACCOUNT) Users , Its an alternative of Django-Signals 
                # Here we can detect the users numbers by this LOCAL STORAGE

def root(request): # Root Page of all operations
    return render(request,"rootPage.html")


def register(request): # To Register a new Account
    if request.method == "POST":
        
        username = request.POST['username']
        email = request.POST['email']
        password=request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        
        # Operations for Verification all the User parameters
        
        try: # As Django Only whrows exceptions if username matches , so handling it is the first job
            
           if User.objects.filter(email=email).count()==0: #Checking the email
               
               if User.objects.filter(password=password).count==0: # Checking the password
                   
                   if len(password)>=8: # Verfications for every new password
                       
                        user=User.objects.create_user(username,email,password)
                        user.first_name=first_name                
                        user.last_name=last_name
                        user.save()
                        messages.success(request,f" {username} , Your account has been created!!")
                        return redirect("/")
                   else:
                        messages.error(request,"Password is too Short")
                        return render(request,"signIn.html")
               else:
                   messages.error(request,"Password entered by someone before!!")
                   return render(request,"signIn.html")
           else:
               messages.error(request,"Email entered by someone before")
               return render(request,"signIn.html")
           
        except Exception:
            messages.error(request,"Username entered by someone before")
            return render(request,"signIn.html")
    else:
        return render(request, 'signIn.html')


def signOut(request): # To Delete a Registered Account
    if request.method == "POST":
        username=request.POST['username']
        
        try:
            User.objects.get(username=username).delete() # Deleting the User Object
            
            if username in Logged_In: # If the User is logged in then clearing the username (If not means after just signing in the person has deleter tha account)
                Logged_In.remove(username)
                
            messages.success(request,f"Object of username :{username} is deleted!!")
            return render(request,"rootPage.html")
        
        except Exception:
            messages.error(request,f"Object of Username {username} Doesnot exists")
            return render(request,"signOut.html")
        
    return render(request,"signOut.html")


def logIn(request): # To ACTIVATE a registered/authentic account
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if username not in Logged_In: # Checking if the username is in set -> the account is already logged in or not
            
            if user is not None:
                login(request, user)
                Logged_In.add(username) # User REGISTERED account is ACTIVE so , his/her username got added in SET
                messages.success(request,f"{username} you are logged in")
                return render(request,"rootPage.html")
            else:
                messages.error(request,f"Login Unsuccessful : Maybe username or password is WRONG!!")
                return render(request,"logIn.html")
            
        else:
            messages.warning(request,f"{username} you are already LOGGED IN")
            return render(request,"logIn.html")
    return render(request,"logIn.html")


def logOut(request): # To DEACTIVATE a registered / authentic account
    if request.method == "POST":
        username = request.POST["username"]
        
        if username in Logged_In: # Searching if the user is logged-in or not
            user = User.objects.filter(username=username).count() # Searching the user in DB
            
            if user == 1:
                logout(request)
                Logged_In.remove(username) # User became UNACTIVE so his/her username also got destroyed
                messages.success(request,f"{username} your account has been disabled")
                return render(request,"rootPage.html")
            else:
                messages.error(request,f"Logout Unsuccessful : Your account doesnot exists already")
                return render(request,"logOut.html")
            
        else:
            messages.warning(request,f"{username} you are already LOGGED OUT/SIGNED OUT")
            return render(request,"logOut.html")
        
    return render(request,"logOut.html")
