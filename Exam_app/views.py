from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):


    return render( request, 'index.html')

def register(request):
    errors = User.objects.register(request.POST)
    if len (errors) > 0:
        for key, error in errors.items():
            messages.error(request, error)
        return redirect("/")
    else:
        PW_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            email=request.POST['email'].lower(), 
            password= PW_hash, 
            F_name=request.POST['first_name'],
            L_name=request.POST['last_name']
        )
        request.session['user_id'] = user.id
        messages.success(request, 'YAYYYY YOURE IN!')
        return redirect('/success')

def success(request):
    if 'user_id' not in request.session:
        messages.error(request, "Permission Denied")
        return redirect("/")
    
    context = {
        'user' : User.objects.get(id = request.session['user_id']),
        "Trips" : Trip.objects.all()
    }
    return render (request, "success.html", context)


def login(request):
    errors = User.objects.login(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('/')

    else:
        user = User.objects.filter(email=request.POST['email'].lower())
        if len(user) < 1 :
            messages.error(request, 'No-ones using this lame email.')
            return redirect("/")

        if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
            print(f"LOG - Session val 'user_id' = {user[0].id}")
            request.session['user_id'] = user[0].id
            return redirect('/success')
        else:
            messages.error(request, 'Wrong password!')
            return redirect('/')

def logout(request):
    request.session.clear()
    messages.success(request, "Log out successful!")
    print(f"LOG - Log out successful, redirecting to home")  
    return redirect("/")

def newTrip(request):
    return render (request, 'new.html')

def create_trip(request):
    errors = Trip.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for Key, value in errors.items():
            messages.error(request, value)
        return redirect('/newTrip')

    else: 
        user = User.objects.get(id = request.session['user_id'])
        Trip.objects.create(
            destination= request.POST['destination'],
            start= request.POST['start'],
            end= request.POST['end'],
            plan= request.POST['plan']
        )
        return redirect('/success')

def editTrip(request, id):

    context={
        'user' : User.objects.get(id=request.session['user_id']),
        'trip' : Trip.objects.get(id=id),
        'start' : Trip.objects.get(id=id).start.strftime('%Y-%m-%d'),
        'end' : Trip.objects.get(id=id).end.strftime('%Y-%m-%d')
    }
    return render (request , 'Edits.html', context)



def update_trip(request, id):

    errors= Trip.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for k, value in errors.items():
            messages.error(request, value)
        return redirect('/editTrip/'+ str(id))

    if request.POST:
        trip = Trip.objects.get(id=id)
        trip.destination = request.POST['destination']
        trip.start = request.POST['start']
        trip.end = request.POST['end']
        trip.plan = request.POST['plan']
        trip.save()
        return redirect('/success')

def view(request, id):
    context={

     'trip' : Trip.objects.get(id=id)

    }
    return render (request, 'decrip.html', context)


def delete_trip(request, id):
    trip = Trip.objects.get(id=id)
    trip.delete()
    return redirect('/success')