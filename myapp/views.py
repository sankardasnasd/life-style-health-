import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import Count
from django.db.models.functions import ExtractYear
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .cal import getcalval
# Create your views here.
from lifestyle import settings
from myapp.models import *

def public_home(request):
    a=Experts.objects.filter(status='approved')
    return render(request,'publicindex.html',{'data':a})

def forget_password(request):
    return render(request,'forget password.html')

def forget_password_post(request):
    em = request.POST['email']
    import random
    import string
    # password = random.randint(000000, 999999)
    log = Login.objects.filter(username=em)

    length = 10 # Adjust the password length as needed
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))

    from django.core.mail import send_mail

    if log.exists():
        logg = Login.objects.get(username=em)
        message = 'Welcome To LifeStyle !  .....Your temporary Password  is!... ' + str(password)
        send_mail(
            'temporary...! Password',message,
            settings.EMAIL_HOST_USER,
            [em, ],
            fail_silently=False
        )
        logg.password = password
        logg.save()
        return HttpResponse('<script>alert("..Please check Email...");window.location="/login"</script>')
    else:
        return HttpResponse('<script>alert("invalid");window.location="/forget_password"</script>')

def login(request):
    if 'submit' in request.POST:
        username = request.POST['username']
        password = request.POST['password']

        a=Login.objects.filter(username=username,password=password)
        if a.exists():
            b = Login.objects.get(username=username, password=password)
            request.session['lid']=b.id
            if b.type=='admin':
                return HttpResponse('''<script>alert("Login successfully ");window.location='/admin_home'</script>''')
            elif b.type == 'expert':
                return HttpResponse('''<script>alert("Login successfully ");window.location='/expert_home'</script>''')
            elif b.type == 'user':
                obu=User.objects.get(LOGIN__id=b.id)
                request.session['utype']=obu.type

                request.session['cal']=float(obu.calorie)
                request.session['cu']=float(obu.calorie)
                request.session['cr']=float(obu.calorie)
                return HttpResponse('''<script>alert("Login successfully ");window.location='/user_home'</script>''')
            elif b.type == 'pending':
                return HttpResponse('''<script>alert("please wait for admin approval..!");window.location='/login'</script>''')
            elif b.type == 'reject':
                return HttpResponse('''<script>alert(" Admin Rejected..!");window.location='/login'</script>''')
            else:
                return HttpResponse('''<script>alert("Invalid ");window.location='/login'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid ");window.location='/login'</script>''')
    return  render(request,'loginindex.html')



def logout(request):
    request.session['lid']=''
    return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')


def admin_home(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')

    a=User.objects.filter(type='Normal')
    user=a.count()
    request.session['user']=user
    a1=User.objects.filter(type='Premium')
    puser=a1.count()
    request.session['user']=user
    request.session['puser']=puser

    e=Experts.objects.all()
    expert=e.count()
    request.session['expert']=expert

    c = Complaints.objects.filter(status='pending')
    c2 = c.count()
    request.session['c2']=c2

    f = Feedback.objects.all()
    ff = f.count()

    request.session['f2']=ff
    request.session['f2']=ff

    users_per_year = User.objects.annotate(year=ExtractYear('date')).values('year').annotate(
        count=Count('id')).order_by('year')

    labels = [entry['year'] for entry in users_per_year]
    data = [entry['count'] for entry in users_per_year]
    request.session['lab'] = labels
    request.session['data'] = data
    context = {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    }


    t_per_year = Payment.objects.annotate(year=ExtractYear('date')).values('year').annotate(
        count=Count('id')).order_by('year')
    print("t_per_year")
    print(t_per_year)
    tlabels = [entry['year'] for entry in t_per_year]
    tdata = [entry['count'] for entry in t_per_year]

    request.session['tlab'] = tlabels
    request.session['tdata'] = tdata



    expert_per_year = Experts.objects.annotate(year=ExtractYear('date')).values('year').annotate(
        count=Count('id')).order_by('year')

    elabels = [entry['year'] for entry in expert_per_year]
    edata = [entry['count'] for entry in expert_per_year]
    request.session['elab'] = elabels
    request.session['edata'] = edata
    context2 = {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    }

    complaints_per_year = Complaints.objects.annotate(year=ExtractYear('date')).values('year').annotate(
        count=Count('id')).order_by('year')

    clabels = [entry['year'] for entry in complaints_per_year]
    cdata = [entry['count'] for entry in complaints_per_year]
    request.session['clab'] = clabels
    request.session['cdata'] = cdata
    context2 = {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    }





    return render(request,'admin/adminindex1.html',{'expert':expert,'user':user,'c2':c2,'f2':ff,'c':c,'f':f},)


def admin_verify_expert(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    a=Experts.objects.all()
    return render(request,'admin/verify_expert.html',{'a':a})

def admin_verify_expert_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    f=request.POST['f']
    a=Experts.objects.filter(name__icontains=f)
    if not a:  # If queryset is empty
        return HttpResponse('''<script>alert("Expert  not found");window.location='/admin_verify_expert'</script>''')

    return render(request,'admin/verify_expert.html',{'a':a})



def admin_view_expert_feedback(request,id):
    b=Expertfeedback.objects.filter(EXPERT_id=id)
    return render(request,'admin/admin_view_expert_feedback.html',{'data':b})


def admin_verify_expert_post_date(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    f=request.POST['f']
    t=request.POST['t']
    a=Experts.objects.filter(date__gte=f,date__lte=t)
    if not a:  # If queryset is empty
        return HttpResponse('''<script>alert("Expert  not found");window.location='/admin_verify_expert'</script>''')

    return render(request,'admin/verify_expert.html',{'a':a})


# def admin_approve_expert(request,id):
#     a=Login.objects.filter(id=id).update(type='expert')
#     b=Experts.objects.filter(LOGIN_id=id).update(status='approved')
#     return HttpResponse('''<script>alert("Approved ");window.location='/admin_verify_expert'</script>''')


from django.core.mail import send_mail
from django.http import HttpResponse
from .models import Login, Experts


def admin_approve_expert(request, id):
    a = Login.objects.filter(id=id).update(type='expert')

    b = Experts.objects.filter(LOGIN_id=id).update(status='approved')

    expert = Login.objects.get(id=id)
    expert_email = expert.username

    subject = 'Expert Approval Notification'
    message = 'Dear {},\n\nYour account has been approved as an expert.\n\nRegards,\nAdmin Team'.format(expert.username)
    from_email = 'nazrinzara3810@gmail.com'
    recipient_list = [expert_email]

    send_mail(subject, message, from_email, recipient_list)

    return HttpResponse('''<script>alert("Approved ");window.location='/admin_verify_expert'</script>''')


def admin_reject_expert(request,id):
    a=Login.objects.filter(id=id).update(type='reject')
    b=Experts.objects.filter(LOGIN_id=id).update(status='reject')
    return HttpResponse('''<script>alert("Rejected ");window.location='/admin_verify_expert'</script>''')



def admin_view_user(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    a=User.objects.all()
    return render(request,'admin/admin_view_user.html',{'a':a})

# def admin_view_user_post(request):
#     if request.session['lid']=='':
#         return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
#     f=request.POST['f']
#     a=User.objects.filter(name__icontains=f)
#
#     return render(request,'admin/admin_view_user.html',{'a':a})

from django.http import HttpResponse


def admin_view_user_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')

    f = request.POST.get('f', '')  # Use get() method to avoid KeyError if 'f' is not in POST data
    a = User.objects.filter(name__icontains=f)

    if not a:  # If queryset is empty
        return HttpResponse('''<script>alert("User not found");window.location='/admin_view_user'</script>''')

    return render(request, 'admin/admin_view_user.html', {'a': a})


def admin_view_user_post_date(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')

    f = request.POST.get('f', '')  # Use get() method to avoid KeyError if 'f' is not in POST data
    t = request.POST.get('t', '')  # Use get() method to avoid KeyError if 'f' is not in POST data
    a = User.objects.filter(date__gte=f,date__lte=t)

    if not a:  # If queryset is empty
        return HttpResponse('''<script>alert("User not found");window.location='/admin_view_user'</script>''')

    return render(request, 'admin/admin_view_user.html', {'a': a})


def admin_view_feedback(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    a=Feedback.objects.all()
    return render(request,'admin/admin_view_feedback.html',{'a':a})

def admin_view_feedback_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    f = request.POST['f']
    t = request.POST['t']
    a = Feedback.objects.filter(date__range=[f, t])
    if not a:  # If queryset is empty
        return HttpResponse('''<script>alert("No Feedback  found in this date");window.location='/admin_view_feedback'</script>''')

    return render(request,'admin/admin_view_feedback.html',{'a':a})


def admin_block_unblock(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    a=Experts.objects.filter(status='approved')
    return render(request,'admin/admin_block_or_un_block.html',{'a':a})

def admin_block_unblock_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    f = request.POST['f']

    a=Experts.objects.filter(status='approved',name__icontains=f)
    return render(request,'admin/admin_block_or_un_block.html',{'a':a})

def admin_block_expert(request,id):
    b=Experts.objects.filter(id=id).update(status='Block')
    return HttpResponse('''<script>alert("Blocked ");window.location='/admin_block_unblock'</script>''')


def admin_unblock_expert(request,id):
    b=Experts.objects.filter(id=id).update(status='UnBlock')
    return HttpResponse('''<script>alert("UnBlocked ");window.location='/admin_block_unblock'</script>''')




def admin_view_complaints(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    a=Complaints.objects.all()
    b=E_Complaints.objects.all()
    return render(request,'admin/admin_view_complaints.html',{'a':a,'b':b})



def admin_view_complaints_post(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')

    f=request.POST['f']
    t=request.POST['t']
    a=Complaints.objects.filter(date__range=[f,t])
    if not a:  # If queryset is empty
        return HttpResponse('''<script>alert("No Complaints  found in this date");window.location='/admin_view_complaints'</script>''')

    return render(request,'admin/admin_view_complaints.html',{'a':a})






def admin_reply(request,id):
    a=Complaints.objects.get(id=id)

    return render(request,'admin/reply.html',{'data':a})

def admin_reply_post(request):
    id=request.POST['id']
    reply=request.POST['c']
    c=Complaints.objects.get(id=id)
    c.reply=reply
    c.status="replied"
    c.save()
    return HttpResponse('''<script>alert("Replied ");window.location='/admin_view_complaints'</script>''')


def admin_reply_expert(request,id):
    a=E_Complaints.objects.get(id=id)

    return render(request,'admin/admin_reply_expert_complaints.html',{'data':a})

def admin_reply_expert_post(request):
    id=request.POST['id']
    reply=request.POST['c']
    c=E_Complaints.objects.get(id=id)
    c.reply=reply
    c.status="replied"
    c.save()
    return HttpResponse('''<script>alert("Replied ");window.location='/admin_view_complaints'</script>''')


# expert

def expert_reg(request):
    if 'submit' in request.POST:
        name=request.POST['name']
        place=request.POST['place']
        post=request.POST['post']
        district=request.POST['district']
        phone=request.POST['phone']
        email=request.POST['email']
        type=request.POST['type']
        password=request.POST['password']

        image=request.FILES['image']
        fs=FileSystemStorage()

        fn=fs.save(image.name,image)
        path=fs.url(fn)

        proof=request.FILES['proof']
        fs1=FileSystemStorage()

        fn1=fs1.save(proof.name,proof)
        path1=fs1.url(fn1)

        b=Login()
        b.username=email
        b.password=password
        b.type='pending'
        b.save()

        a=Experts()
        a.LOGIN=b
        a.name=name
        a.type=type
        a.place=place
        a.post=post
        a.district=district
        a.phone=phone
        a.date=datetime.datetime.today()
        a.email=email
        a.idproof=path1
        a.image=path
        a.status='pending'
        a.save()
        return HttpResponse('''<script>alert("Registered ");window.location='/login'</script>''')


    return render(request,'expertindex.html')



def expert_home(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    ob=Experts.objects.get(LOGIN__id=request.session['lid'])
    request.session['fn']=ob.image
    obb=Request.objects.filter(EXPERT__LOGIN__id=request.session['lid'])
    u=[]
    for i in obb:
        if i.USER.LOGIN.id not in u:
            u.append(i.USER.LOGIN.id)
    request.session['user']=len(u)
    ob1=Chat.objects.filter(TOID__id=request.session['lid'],date__month=datetime.datetime.now().strftime('%m'),date__year=datetime.datetime.now().strftime("%Y"))
    s=[]
    for i in ob1:
        if i.FROMID.id not in s:
            s.append(i.FROMID.id)
    request.session['tm']=len(s)
    obb = Request.objects.filter(EXPERT__LOGIN__id=request.session['lid'],status='requested')
    request.session['pen']=len(obb)
    y=[1,2,3,4,5,6,7,8,9,10,11,12]
    c=[]
    for i in y:
        ob1 = Chat.objects.filter(TOID__id=request.session['lid'], date__month=i,
                                  date__year=datetime.datetime.now().strftime("%Y"))
        s = []
        for i in ob1:
            if i.FROMID.id not in s:
                s.append(i.FROMID.id)
        c.append(len(s))
    request.session['data']=c
    return render(request,'expert/expert1.html')



def expert_profile(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    a=Experts.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'expert/expert_profile.html',{'data':a})




def expert_add_tutorial(request):
    a=Tutorial.objects.filter(EXPERT__LOGIN_id=request.session['lid'])
    if 'submit' in request.POST:
        video = request.FILES['video']
        pdf = request.FILES['pdf']
        desc = request.POST['desc']
        title = request.POST['title']

        fs=FileSystemStorage()
        dates=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+'.mp4'
        fs.save(dates,video)
        path=fs.url(dates)

        fs1 = FileSystemStorage()
        dates1 = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.pdf'
        fs1.save(dates1, pdf)
        path1 = fs1.url(dates1)

        a=Tutorial()
        a.EXPERT=Experts.objects.get(LOGIN_id=request.session['lid'])
        a.date=datetime.datetime.now().today()
        a.file=path
        a.pdf=path1
        a.title=title
        a.description=desc
        a.save()
        return HttpResponse('''<script>alert("Success ");window.location='/expert_add_tutorial'</script>''')




    return render(request,'expert/add_tutorial.html',{'i':a})


# def expert_add_tutorial2(request):
#     desc = request.POST['desc']
#     title = request.POST['title']
#
#     a = Tutorial()
#
#     if request.FILES:
#
#         pdf = request.FILES['pdf']
#         fs1 = FileSystemStorage()
#         dates1 = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.pdf'
#         fs1.save(dates1, pdf)
#         path1 = fs1.url(dates1)
#         a.pdf = path1
#
#     if request.FILES:
#         video = request.FILES['video']
#
#         fs = FileSystemStorage()
#         dates = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.mp4'
#         fs.save(dates, video)
#         path = fs.url(dates)
#         a.file = path
#
#     a.EXPERT = Experts.objects.get(LOGIN_id=request.session['lid'])
#     a.date = datetime.datetime.now().today()
#     a.title = title
#     a.description = desc
#     a.save()
#     return HttpResponse('''<script>alert("Success ");window.location='/expert_add_tutorial'</script>''')













def delete_tutorial(request,id):
    var=Tutorial.objects.get(id=id)
    var.delete()
    return HttpResponse('''<script>alert("Deleted ");window.location='/expert_add_tutorial'</script>''')


def edit_expert_profile(request,id):
    a=Experts.objects.get(id=id)
    return render(request,'expert/edit_expert.html',{'i':a})

def expert_edit_profile_post(request):
    id = request.POST['id']
    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    district = request.POST['district']
    phone = request.POST['phone']
    email = request.POST['email']



    a = Experts.objects.get(id=id)
    if 'image' in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage()

        fn = fs.save(image.name, image)
        path = fs.url(fn)
        a.image = path

    a.name=name
    a.place=place
    a.post=post
    a.district=district
    a.phone=phone
    a.email=email
    a.save()
    return HttpResponse('''<script>alert("Success ");window.location='/expert_profile'</script>''')


def expert_change_password(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    if 'submit' in request.POST:
        old=request.POST['old']
        new=request.POST['new']
        confirm=request.POST['confirm']

        a=Login.objects.filter(password=old,id=request.session['lid'])
        if a.exists():
            if new == confirm:
                Login.objects.filter(id=request.session['lid']).update(password=confirm)
                return HttpResponse(
                    '''<script>alert('Successfully changed');window.location='/login'</script>''')
            else:
                return HttpResponse(
                    '''<script>alert('Password Mismatch');window.location='/expert_change_password'</script>''')

        else:
            return HttpResponse(
                '''<script>alert('Password Mismatch');window.location='/expert_change_password'</script>''')
    return render(request,'expert/expert_change_password.html')




def expert_view_user(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    a=User.objects.all()
    return render(request,'expert/expert_view_user.html',{'data':a})

def expert_view_user_post(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    f=request.POST['f']
    a=User.objects.filter(name__contains=f)
    if not a:  # If queryset is empty
        return HttpResponse('''<script>alert("No User  found ");window.location='/expert_view_user'</script>''')


    return render(request,'expert/expert_view_user.html',{'data':a})



# user


def user_reg(request):
    if 'submit' in request.POST:
        name=request.POST['name']
        place=request.POST['place']
        post=request.POST['post']
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])

        gen=request.POST['gen']

        district=request.POST['district']
        phone=request.POST['phone']
        email=request.POST['email']
        password=request.POST['password']
        dob=request.POST['dob']

        image=request.FILES['image']
        fs=FileSystemStorage()

        fn=fs.save(image.name,image)
        path=fs.url(fn)

        bm_height=height/100
        bmii=round(weight/(bm_height **2),2)
        y=int(datetime.datetime.now().strftime("%Y")) -int(dob.split('-')[0])
        bmr=0
        if gen == "Male":
            bmr=(10*weight)+(6.25*height)+(5*y)+5
        else:
            bmr = (10 * weight) + (6.25 * height) + (5 * y) - 16
        cc=bmr* 1.2

        b=Login()
        b.username=email
        b.password=password
        b.type='user'
        b.save()



        a=User()
        a.LOGIN=b
        a.name=name
        a.place=place
        a.dob=dob
        a.weight=weight
        a.height=height
        a.post=post
        a.district=district
        a.phone=phone
        a.email=email
        a.image=path
        a.gender=gen
        a.bmi=bmii
        a.calorie=cc
        a.date=datetime.datetime.now().today().date()
        a.type='Normal'
        a.save()
        # Normal and Premium
        return HttpResponse('''<script>alert("Registered ");window.location='/login'</script>''')


    return render(request,'user/user_reg.html')


def user_home(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    a=User.objects.get(LOGIN_id=request.session['lid'])

    # Aggregate total calories burned for each date
    calorie_data = Food.objects.values('date').annotate(total_calories_burned=Sum('callorie')).order_by('date')

    # Extract dates and total calories burned
    dates = [str(entry['date']) for entry in calorie_data]
    calories_burned = [entry['total_calories_burned'] for entry in calorie_data]

    user = User.objects.get(LOGIN_id=request.session['lid'])  # Get the logged-in user
    today = timezone.now().date()

    # Filter Food records for the current user and today's date
    calorie_data = Food.objects.filter(USER=user, date=today).aggregate(total_calories_burned=Sum('callorie'))
    total_calories_burned = calorie_data['total_calories_burned'] or 0  # Ensure it's zero if no data

    # Calculate the calorie goal based on BMI
    bmi = float(user.bmi)
    calorie_goal = calculate_calorie_goal(bmi)
    request.session['total_calories_burned']=total_calories_burned
    request.session['calorie_goal']=calorie_goal

    context = {
        'total_calories_burned': total_calories_burned,
        'calorie_goal': calorie_goal,
    }




    return render(request,'user/userindex.html',{'data':a,'dates': dates, 'calories_burned': calories_burned})



def user_profile(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    a=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'user/user_profile.html',{'data':a})


def edit_user_profile(request,id):
    a=User.objects.get(id=id)
    return render(request,'user/edit_user.html',{'i':a})


def edit_user_profile_post(request):
    id = request.POST['id']
    name = request.POST['name']
    place = request.POST['place']
    post = request.POST['post']
    district = request.POST['district']
    phone = request.POST['phone']
    email = request.POST['email']



    a = User.objects.get(id=id)
    if 'image' in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage()

        fn = fs.save(image.name, image)
        path = fs.url(fn)
        a.image = path

    a.name=name
    a.place=place
    a.post=post
    a.district=district
    a.phone=phone
    a.email=email
    a.save()
    return HttpResponse('''<script>alert("Success ");window.location='/user_profile'</script>''')



def user_change_password(request):
    if request.session['lid'] == '':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    if 'submit' in request.POST:
        old=request.POST['old']
        new=request.POST['new']
        confirm=request.POST['confirm']

        a=Login.objects.filter(password=old,id=request.session['lid'])
        if a.exists():
            if new == confirm:
                Login.objects.filter(id=request.session['lid']).update(password=confirm)
                return HttpResponse(
                    '''<script>alert('Successfully changed');window.location='/login'</script>''')
            else:
                return HttpResponse(
                    '''<script>alert('Password Mismatch');window.location='/user_change_password'</script>''')

        else:
            return HttpResponse(
                '''<script>alert('Password Mismatch');window.location='/user_change_password'</script>''')
    return render(request,'user/user_change_password.html')


def user_sent_complaints(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    d=Complaints.objects.filter(USER__LOGIN_id=request.session['lid'])
    if 'submit' in request.POST:
        c=request.POST['c']

        v=Complaints()
        v.complaints=c
        v.date=datetime.datetime.now().date()
        v.USER=User.objects.get(LOGIN_id=request.session['lid'])
        v.status='pending'
        v.reply='pending'
        v.save()
        return HttpResponse(
            '''<script>alert('Complaint Sent');window.location='/user_sent_complaints'</script>''')
    return render(request,'user/sent complaints.html',{'data':d})

def expert_sent_complaints(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    d=Complaints.objects.filter(USER__LOGIN_id=request.session['lid'])
    if 'submit' in request.POST:
        c=request.POST['c']

        v=E_Complaints()
        v.complaints=c
        v.date=datetime.datetime.now().date()
        v.EXPERT=Experts.objects.get(LOGIN_id=request.session['lid'])
        v.status='pending'
        v.reply='pending'
        v.save()
        return HttpResponse(
            '''<script>alert('Complaint Sent');window.location='/expert_sent_complaints'</script>''')
    return render(request,'expert/sent complaints.html',{'data':d})

def user_sent_feedback(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    # d=Complaints.objects.filter(USER__LOGIN_id=request.session['lid'])
    if 'submit' in request.POST:
        c=request.POST['c']

        v=Feedback()
        v.feedback=c
        v.date=datetime.datetime.now().date()
        v.USER=User.objects.get(LOGIN_id=request.session['lid'])

        v.save()
        return HttpResponse(
            '''<script>alert(' Sent');window.location='/user_sent_feedback'</script>''')
    return render(request,'user/sent feedback.html')




def expert_sent_feedback(request):
    if request.session['lid']=='':
        return HttpResponse('''<script>alert("Logouted ");window.location='/login'</script>''')
    # d=Complaints.objects.filter(USER__LOGIN_id=request.session['lid'])
    if 'submit' in request.POST:
        c=request.POST['c']

        v=E_Feedback()
        v.feedback=c
        v.date=datetime.datetime.now().date()
        v.EXPERT=Experts.objects.get(LOGIN_id=request.session['lid'])
        v.save()
        return HttpResponse(
            '''<script>alert(' Sent');window.location='/expert_sent_feedback'</script>''')
    return render(request,'expert/sent feedback.html')










# user module chat with expert

def chatwithexpert(request):
    ob = Experts.objects.filter(status='approved')
    return render(request,"user/fur_chat.html",{'val':ob})




def chatview(request):
    obb=Request.objects.filter(USER__LOGIN__id=request.session['lid'],status='accept')
    r=[]
    for i in obb:
        r.append(i.EXPERT.id)
    ob = Experts.objects.filter(status='approved',id__in=r)
    d=[]
    for i in ob:
        r={"name":i.name,'image':i.image,'email':i.email,'loginid':i.LOGIN.id}
        print(r)
        d.append(r)
        print(r)
    return JsonResponse(d, safe=False)


def chatviewexpert(request,id):
   return render(request,"user/fur_chat.html",{"eid":id})




def coun_insert_chat(request,msg,id):
    print("===",msg,id)
    ob=Chat()
    ob.FROMID=Login.objects.get(id=request.session['lid'])
    ob.TOID=Login.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.datetime.now().strftime("%Y-%m-%d")
    ob.save()

    return JsonResponse({"task":"ok"})
    # refresh messages chatlist



def coun_msg(request,id):

    ob1=Chat.objects.filter(FROMID_id=id,TOID__id=request.session['lid'])
    ob2=Chat.objects.filter(FROMID_id=request.session['lid'],TOID_id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FROMID.id,"msg":i.message,"date":i.date,"chat_id":i.id})

    obu=Experts.objects.get(LOGIN_id=id)


    return JsonResponse({"data":res,"name":obu.name,"photo":obu.image,"user_lid":obu.LOGIN.id})




# expert chat with users


def chatwithuser(request):
    ob = User.objects.all()
    return render(request,"expert/fur_chat.html",{'val':ob})

# def expertchatview(request):
#     ob = User.objects.all()
#     d=[]
#     for i in ob:
#         r={"name":i.name,'image':i.image,'email':i.email,'loginid':i.LOGIN.id}
#         print(r)
#         d.append(r)
#         print(r)
#     return JsonResponse(d, safe=False)


from django.http import JsonResponse
from .models import User, Request


def expertchatview(request):
    accepted_requests = Request.objects.filter(status='accept')

    users_with_accepted_requests = User.objects.filter(request__in=accepted_requests).distinct()

    # Prepare the data to be returned
    data = []
    for user in users_with_accepted_requests:
        r = {
            "name": user.name,
            "image": user.image,
            "email": user.email,
            "loginid": user.LOGIN.id
        }
        data.append(r)

    return JsonResponse(data, safe=False)


def expertcoun_insert_chat(request,msg,id):
    print("===",msg,id)
    ob=Chat()
    ob.FROMID=Login.objects.get(id=request.session['lid'])
    ob.TOID=Login.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.datetime.now().strftime("%Y-%m-%d")
    ob.save()

    return JsonResponse({"task":"ok"})
    # refresh messages chatlist


def expertcoun_msg(request,id):

    ob1=Chat.objects.filter(FROMID_id=id,TOID__id=request.session['lid'])
    ob2=Chat.objects.filter(FROMID_id=request.session['lid'],TOID_id=id)
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.FROMID.id,"msg":i.message,"date":i.date,"chat_id":i.id})

    obu=User.objects.get(LOGIN_id=id)


    return JsonResponse({"data":res,"name":obu.name,"photo":obu.image,"user_lid":obu.LOGIN.id})






# new chat single
def chatviewuser(request,id):
   return render(request,"user/fur_chat.html",{"eid":id})









def user_view_tutorial(request,id):
    a=Tutorial.objects.filter(EXPERT_id=id)
    return render(request,'user/user view_tutorial.html',{'a':a})

def user_view_expert(request):
    a=Experts.objects.filter(status='approved')
    return render(request,'user/user_view_expert.html',{'a':a})


def user_sent_expert_feedback(request,id):
    var=Experts.objects.get(id=id)
    return render(request,'user/user_sent_expert_feedback.html',{'a':var})


def user_sent_expert_feedback_post(request):
    id=request.POST['id']
    feed=request.POST['c']

    a=Expertfeedback()
    a.EXPERT=Experts.objects.get(id=id)
    a.feedback=feed
    a.date=datetime.datetime.now().today()
    a.USER=User.objects.get(LOGIN_id=request.session['lid'])
    a.save()
    return HttpResponse(
        '''<script>alert('Success');window.location='/user_home'</script>''')


def user_request(request,id):
    a=Request()
    a.EXPERT=Experts.objects.get(id=id)
    a.USER=User.objects.get(LOGIN_id=request.session['lid'])
    a.status='requested'
    a.date=datetime.datetime.now().today()
    a.save()
    return HttpResponse(
        '''<script>alert(' Request Sent');window.location='/user_view_expert'</script>''')

def user_view_request(request):
    a=Request.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,'user/user_view_request.html',{'a':a})



def expert_view_request(request):
    a=Request.objects.filter(EXPERT__LOGIN_id=request.session['lid'],status='requested')
    return render(request,'expert/expert_view_request.html',{'a':a})



def checkalert(request):
    d=datetime.datetime.now().strftime("%Y-%m-%d")
    a=Event.objects.filter(USER__LOGIN__id=request.session['lid'],date=d,status='viewed')
    print(a)
    if len(a)>0:
        time=datetime.datetime.now().strftime("%H:%M")+":00"

        for i in a:
            print("1", str(i.time).split('.')[0],time)
            if str(i.time).split('.')[0]==time:
                print({"task":"valid","event":i.event+" on "+str(i.date),"t":"e"})
                i.status="completed"
                i.save()
                return JsonResponse({"task":"valid","event":i.event,"t":"e"})
    a = Event.objects.filter(USER__LOGIN__id=request.session['lid'], rdate=d, status='pending')
    print(a)
    if len(a) > 0:
        time = datetime.datetime.now().strftime("%H:%M") + ":00"
        for i in a:
            print("2",str(i.rtime).split('.')[0],time)
            if str(i.rtime).split('.')[0] == time:
                i.status = "viewed"
                i.save()
                print({"task": "valid", "event": i.event+" on "+str(i.date), "t": "r"})
                return JsonResponse({"task": "valid", "event": i.event, "t": "r"})
    print("na")


    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    ob=Exercises.objects.filter(USER__LOGIN__id=request.session['lid'],date=yesterday)
    cal=0
    for i in ob:
        cal=cal+i.callorie
    print(cal,request.session['cal'],yesterday)
    if cal>int(request.session['cal']):
        ob=Calnoti.objects.filter(USER__LOGIN__id=request.session['lid'],date=datetime.datetime.today())

        if len(ob)==0:
            ob=Calnoti()
            ob.USER = User.objects.get(LOGIN__id=request.session['lid'])

            ob.date=datetime.datetime.today()
            ob.save()
            return JsonResponse({"task": "alert", "event":"Warning More calories burned", "t": ""})

    return JsonResponse({"task": "invalid"})


def expert_accept_request(request,id):
    a=Request.objects.filter(id=id).update(status='accept')
    return HttpResponse(
        '''<script>alert(' Request Accept');window.location='/expert_view_request'</script>''')


import json
from django.shortcuts import render


def users_chart(request):
    users_per_year = User.objects.annotate(year=ExtractYear('date')).values('year').annotate(
        count=Count('id')).order_by('year')

    labels = [entry['year'] for entry in users_per_year]
    data = [entry['count'] for entry in users_per_year]
    request.session['lab']=labels
    request.session['data']=data
    context = {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    }

    return render(request, 'admin/year_user.html', context)


import time


def days_between_dates(dt1, dt2):
    date_format = "%Y-%m-%d"
    a = time.mktime(time.strptime(dt1, date_format))
    b = time.mktime(time.strptime(dt2, date_format))
    delta = b - a
    return int(delta / 86400)


def user_add_task(request):
    a=Task.objects.filter(USER__LOGIN_id=request.session['lid'])
    aa=[]
    for i in a:
        ob=TaskEvaluation.objects.filter(TASK__id=i.id)
        d=0
        for j in ob:
            d=d+int(j.score)
        p=int((d/int(i.Duration))*100)
        i.p=p
        aa.append(i)
    if 'submit' in request.POST:
        title = request.POST['title']
        f = request.POST['f']
        t = request.POST['to']

        if t <= f:
            return HttpResponse(
                '''<script>alert("Error: 'To' date must be after 'From' date.");window.location='/user_add_task'</script>''')
        ddif=days_between_dates(f,t)
        a=Task()
        a.USER=User.objects.get(LOGIN_id=request.session['lid'])
        a.fromdate=f
        a.todate=t
        a.title=title
        a.Duration=ddif

        a.save()
        return HttpResponse('''<script>alert("Success ");window.location='/user_add_task'</script>''')




    return render(request,'user/add task.html',{'i':aa,"d":datetime.datetime.now().strftime("%Y-%m-%d")})


def user_event(request):
    a=Event.objects.filter(USER__LOGIN_id=request.session['lid'])
    aa=a

    if 'submit' in request.POST:
        event = request.POST['e']
        ed = request.POST['ed']
        et = request.POST['et']
        rd = request.POST['rd']
        rt = request.POST['rt']
        ob=Event()
        ob.USER=User.objects.get(LOGIN__id=request.session['lid'])
        ob.event = event
        ob.status = 'pending'
        ob.date = ed
        ob.time = et
        ob.rdate = rd
        ob.rtime =rt
        ob.save()


        return HttpResponse('''<script>alert("Success ");window.location='/user_event'</script>''')




    return render(request,'user/add_event.html',{'i':aa,"d":datetime.datetime.now().strftime("%Y-%m-%d")})


def delete_event(request,id):
    var=Event.objects.get(id=id)
    var.delete()
    return HttpResponse('''<script>alert("Delete ");window.location='/user_event'</script>''')


def delete_task(request,id):
    var=Task.objects.get(id=id)
    var.delete()
    return HttpResponse('''<script>alert("Delete ");window.location='/user_add_task'</script>''')


def status_task(request,id):
    request.session['tid']=id
    i=Task.objects.get(id=id)
    ob = TaskEvaluation.objects.filter(TASK__id=i.id)
    d = 0
    for j in ob:
        d = d + int(j.score)
    p = int(i.Duration)-d
    if p<=0:
        return HttpResponse('''<script>alert("Task Completed ");window.location='/user_add_task'</script>''')

    return render(request,"user/add task1.html",{"m":p})


def insert_te(request):
    id=request.session['tid']
    f=request.POST['f']

    ob = TaskEvaluation()
    ob.TASK = Task.objects.get(id=id)
    ob.date = datetime.datetime.today()
    ob.score=f
    ob.save()

    return HttpResponse('''<script>alert("Task Status Updated ");window.location='/user_add_task'</script>''')
import  razorpay
def gopremium(request):
    return HttpResponse('''<script>alert("Go Premium for this ");window.location='/premium'</script>''')


def premium(request):
    request.session['pay_amount'] = 100
    client = razorpay.Client(auth=("rzp_test_edrzdb8Gbx5U5M", "XgwjnFvJQNG6cS7Q13aHKDJj"))
    print(client)
    payment = client.order.create({'amount': str(100) + "00", 'currency': "INR", 'payment_capture': '1'})
    res = User.objects.get(LOGIN__id=request.session['lid'])

    return render(request, 'UserPayProceed.html',
                  {'p': payment, 'val': res, "lid": request.session['lid'], "id": request.session['lid']})







def on_payment_success(request):
    id=request.GET['lid']
    obu = User.objects.get(LOGIN__id=id)
    obu.type='Premium'
    obu.save()

    ob=Payment()
    ob.USER=obu
    ob.date=datetime.datetime.today()
    ob.save()

    request.session['utype'] = obu.type
    request.session['lid'] = id
    request.session['cu'] = float(obu.calorie)
    request.session['cr'] = float(obu.calorie)
    return HttpResponse('''<script>alert("Success ");window.location='/user_home'</script>''')


def delete_food(request,id):
    var=Food.objects.get(id=id)
    var.delete()
    return HttpResponse('''<script>alert("Delete ");window.location='/user_add_food'</script>''')


from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Food, User
import datetime

calories_per_gram = {
    # Fruits
    'Apple': 0.52,
    'Banana': 0.89,
    'Broccoli': 0.34,
    'Orange': 0.50,
    'Apricot': 0.44,
    'Grape': 0.54,
    'Kiwi': 0.52,
    'Mango': 0.62,
    'Peach': 0.32,
    'Lime': 0.22,
    'Dates': 0.52,
    'Guava': 0.62,
    'Papaya': 0.82,
    'Lemon': 0.32,
    'Pineapple': 0.50,
    'Strawberry': 0.32,
    'Watermelon': 0.30,
    'Blueberry': 0.57,
    'Cherry': 0.63,
    'Pomegranate': 0.83,


    # Vegetables
    'Carrot': 0.41,
    'Tomato': 0.18,
    'Potato': 0.77,
    'Onion': 0.40,
    'Spinach': 0.23,
    'Cauliflower': 0.25,
    'Cucumber': 0.16,
    'Bell Pepper': 0.20,
    'Eggplant': 0.24,
    'Zucchini': 0.17,

    # Grains and Legumes
    'Rice': 1.12,
    'Chapati': 0.82,
    'Dal': 1.10,
    'Quinoa': 1.20,
    'Lentils': 1.16,
    'Chickpeas': 1.64,
    'Oats': 3.89,
    'Barley': 3.52,
    'Buckwheat': 3.43,

    # Dairy
    'Milk': 0.42,
    'Yogurt': 0.61,
    'Cheese': 4.02,
    'Butter': 7.17,
    'Paneer': 2.10,
    'Ice Cream': 2.06,

    # Meats and Fish
    'Chicken': 2.39,
    'Beef': 2.50,
    'Pork': 2.42,
    'Lamb': 2.94,
    'Salmon': 2.08,
    'Tuna': 1.32,
    'Shrimp': 1.00,
    'Egg': 1.43,

    # Indian Dishes
    'Ghee Roast': 1.10,
    'Ghee Rice': 1.4,
    'Biriyani': 1.50,
    'Chicken Biriyani': 1.80,
    'Egg Biryani': 1.80,
    'Beef Biryani': 1.90,
    'Pork Biryani': 2.20,
    'Kuzhi Mandhi': 2.40,
    'Alfaham Mandhi': 2.40,
    'Chicken Tandoori': 2.10,
    'Alfaham': 1.40,
    'Samosa': 2.50,
    'Chicken Samosa': 2.80,
    'Beef Samosa': 2.90,
    'Egg Samosa': 2.20,
    'Egg Puffs': 1.20,
    'Chicken Puffs': 1.50,
    'Puffs': 1.00,
    'Pathiri': 1.00,
    'Pani Puri': 3.00,
    'Aloo Paratha': 1.50,
    'Roti': 0.80,
    'Dosa': 1.60,
    'Idli': 1.10,
    'Upma': 1.20,
    'Pongal': 1.40,
    'Vada': 2.20,
    'Bhature': 2.50,
    'Chole': 1.30,
    'Pulao': 1.20,
    'Kheer': 1.80,
    'Gulab Jamun': 3.00,
    'Rasgulla': 2.50,
    'Jalebi': 3.50,
    'Laddu': 4.00,
    'Sambar': 0.70,
    'Vegetable Curry': 1.00,
    'Fish Curry': 1.50,
    'Chicken Curry': 2.00,
    'Mutton Curry': 2.50,
    'Egg Curry': 1.50,
    'Paneer Butter Masala': 2.20,
    'Palak Paneer': 1.80,
    'Aloo Gobi': 1.20,
    'Baingan Bharta': 1.00,
    'Butter Chicken': 2.50,
    'Tandoori Chicken': 2.00,
    'Naan': 2.00,
    'Paratha': 2.00,
    'Porotta': 2.00,
    'Pav Bhaji': 2.20,
    'Bhel Puri': 2.50,
    'Sev Puri': 3.00,
    'Dhokla': 1.10,
    'Kachori': 3.50,
    'Poha': 1.20,
    'Masala Dosa': 1.80,
    'Mysore Pak': 4.00,
    'Halwa': 3.50,
    'Barfi': 3.00,
    'Peda': 3.50,
    'Tea': 1.0,
    'Coffee': 1.0,
    'Boost': 1.20,
    'Horlicks': 1.20,
    'Bournvita ': 1.20,
    'Pepsi ': 1.80,
    'Cola': 1.80,
    'Fruity': 1.80,
    'Chappathi': 1.50,
    'Rotti': 1.50,

    # Chinese Dishes
    'Fried Rice': 1.63,
    'Chicken Fried Rice': 1.83,
    'Egg Fried Rice': 1.63,
    'Beef Fried Rice': 1.99,
    'Spring Roll': 1.50,
    'Dim Sum': 2.00,
    'Sweet and Sour Chicken': 1.92,
    'Kung Pao Chicken': 2.00,
    'Mapo Tofu': 1.00,
    'Peking Duck': 3.00,
    'Wonton Soup': 0.50,
    'Chicken Fry': 2.50,
    'Puttu': 2.00,

    # Japanese Dishes
    'Sushi': 1.30,
    'Tempura': 2.00,
    'Ramen': 1.80,
    'Miso Soup': 0.40,
    'Teriyaki Chicken': 1.90,
    'Sashimi': 1.20,
    'Udon': 1.30,

    # Italian Dishes
    'Pizza': 2.66,
    'Pasta': 1.58,
    'Lasagna': 1.85,
    'Risotto': 1.45,
    'Tiramisu': 2.40,
    'Gelato': 1.60,
    'Panini': 2.00,

    # Mexican Dishes
    'Taco': 2.00,
    'Burrito': 2.50,
    'Quesadilla': 2.20,
    'Enchilada': 2.30,
    'Guacamole': 1.67,
    'Churros': 2.60,
    'Tamales': 2.50,

    # Middle Eastern Dishes
    'Hummus': 1.66,
    'Falafel': 2.50,
    'Shawarma': 2.20,
    'Tabbouleh': 1.20,
    'Baba Ganoush': 1.00,
    'Kebab': 2.30,
    'Baklava': 4.00,

    # Other International Dishes
    'Paella': 1.50,
    'Croissant': 4.50,
    'Crepe': 1.60,
    'Bratwurst': 3.20,
    'Sauerbraten': 1.80,
    'Borscht': 0.30,
    'Pierogi': 1.70,
    'Poutine': 2.50,
    'Feijoada': 2.10,
    'Empanada': 2.70,

    'Almonds': 5.76,
    'Walnuts': 6.54,
    'Cashews': 5.53,
    'Peanuts': 5.67,
    'Pistachios': 5.62,
    'Hazelnuts': 6.26,
    'Macadamia Nuts': 7.18,
    'Pumpkin Seeds': 5.49,
    'Sunflower Seeds': 5.84,
    'Chia Seeds': 4.86,
    'Flax Seeds': 5.34,
    'Sesame Seeds': 5.73,
}

# def user_add_food(request):
#     d=datetime.datetime.today()
#     a = Food.objects.filter(USER__LOGIN_id=request.session['lid'],date=d)
#     if 'submit' in request.POST:
#         type = request.POST['type']
#         f = request.POST['f']
#         t = request.POST['to']
#         name = request.POST['name']
#         g = int(request.POST['g'])
#
#         if t <= f:
#             return HttpResponse(
#                 '''<script>alert("Error: 'To' Time must be after 'From' Time.");window.location='/user_add_food'</script>'''
#             )
#
#         if name not in calories_per_gram:
#             return HttpResponse(
#                 '''<script>alert("Error: Unknown food type.");window.location='/user_add_food'</script>'''
#             )
#
#         calories = calories_per_gram[name] * g
#
#         food = Food()
#         food.USER = User.objects.get(LOGIN_id=request.session['lid'])
#         food.fromtime = f
#         food.totime = t
#         food.gram = g
#         food.date = datetime.datetime.today()
#         food.name = name
#         food.type = type
#         food.callorie = calories
#
#         food.save()
#         return HttpResponse('''<script>alert("Success");window.location='/user_add_food'</script>''')
#
#     return render(request, 'user/food.html', {'i': a})







import datetime
from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Food, User

# Add your calories_per_gram dictionary here

def user_add_food(request):
    d = datetime.datetime.today()
    a = Food.objects.filter(USER__LOGIN_id=request.session['lid'], date=d)

    total_calories = sum([food.callorie for food in a])
    request.session['cr']=abs(request.session['cu']-total_calories)
    if total_calories<request.session['cu']:
        request.session['f1']="Consumed"
        request.session['f2']="Remaining"
        request.session['val1']=total_calories
        request.session['val2']=request.session['cr']
    else:
        request.session['f1'] = "Allowed"
        request.session['f2'] = "Over Used"
        request.session['val1'] = request.session['cu']
        request.session['val2'] = abs(request.session['cr'])

    if 'submit' in request.POST:
        type = request.POST['type']
        # f = request.POST['f']
        # t = request.POST['to']
        name = request.POST['name']
        g = int(request.POST['g'])


        if name not in calories_per_gram:
            try:
                calories=(float(getcalval("100 gm "+name))/100) * g
            except:
                return HttpResponse(
                    '''<script>alert("Error: Unknown food type.");window.location='/user_add_food'</script>'''
                )
        else:
            calories = calories_per_gram[name] * g

        food = Food()
        food.USER = User.objects.get(LOGIN_id=request.session['lid'])
        # food.fromtime = f
        # food.totime = t
        food.gram = g
        food.date = datetime.datetime.today()
        food.name = name
        food.type = type
        food.callorie = calories

        food.save()

        # Update the total calories after adding the new food
        total_calories += calories

        return HttpResponse('''<script>alert("Success");window.location='/user_add_food'</script>''')

    return render(request, 'user/food.html', {'i': a, 'total_calories': total_calories})




# def user_calorie_burn_chart(request):
#     # Aggregate total calories burned for each date
#     calorie_data = Food.objects.values('date').annotate(total_calories_burned=Sum('calorie')).order_by('date')
#
#     # Extract dates and total calories burned
#     dates = [entry['date'] for entry in calorie_data]
#     calories_burned = [entry['total_calories_burned'] for entry in calorie_data]
#
#     return render(request, 'user/callorie.html', {'dates': dates, 'calories_burned': calories_burned})





def user_calorie_burn_chart(request):

    calorie_data = Food.objects.filter(USER__LOGIN__id=request.session['lid']).order_by('date')
    dd=[]
    for i in calorie_data:
        if str(i.date) not in dd:
            dd.append(str(i.date))
    # Extract dates and total calories burned
    calories_burned=[]
    calories_consumed=[]
    emotionl=[]
    for i in dd:
        c=Food.objects.filter(USER__LOGIN__id=request.session['lid'],date=i)
        cf=0
        for j in c:
            cf=cf+float(j.callorie)
        calories_consumed.append(cf)
        c = Exercises.objects.filter(USER__LOGIN__id=request.session['lid'], date=i)
        cf = 0
        for j in c:
            cf = cf + float(j.callorie)
        calories_burned.append(cf)
        c = Emotion.objects.filter(USER__LOGIN__id=request.session['lid'], date=i)
        cf = 0
        for j in c:
            cf = cf + float(j.happy)
        if len(c)>0:
            cf=cf/len(c)
        emotionl.append(cf)

    return render(request, 'user/callorie.html', {'dates': dd, 'calories_burned': calories_burned,"cc":calories_consumed,"emo":emotionl})
#
# def user_calorie_burn_chart(request):
#     # Aggregate total calories burned for each date
#     calorie_data = Food.objects.values('date').annotate(total_calories_burned=Sum('callorie')).order_by('date')
#
#     # Extract dates and total calories burned
#     dates = [str(entry['date']) for entry in calorie_data]
#     calories_burned = [entry['total_calories_burned'] for entry in calorie_data]
#
#     return render(request, 'user/callorie.html', {'dates': dates, 'calories_burned': calories_burned})


# myapp/views.py
from django.shortcuts import render
from .models import Food
from django.utils import timezone

def daily_calorie_intake(request):
    today = timezone.now().date()
    total_calories = Food.objects.filter(USER=User.objects.get(LOGIN_id=request.session['lid']), date=today).aggregate(total=models.Sum('calorie'))['total'] or 0
    context = {
        'total_calories': total_calories,
        'goal_calories': 2000  # You can adjust this to the user's specific goal
    }
    return render(request, 'user/daily callorie.html', context)





from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum
from .models import Food

# def today_calories_view(request):
#     today = timezone.now().date()
#     calorie_data = Food.objects.filter(date=today).aggregate(total_calories_burned=Sum('callorie'))
#     total_calories_burned = calorie_data['total_calories_burned'] or 0  # Ensure it's zero if no data
#
#     context = {
#         'total_calories_burned': total_calories_burned,
#         'calorie_goal': 2000,  # Example calorie goal
#     }
#     return render(request, 'user/today_callorie.html', context)

from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum
from .models import Food, User

# def today_calories_view(request):
#     user = User.objects.get(LOGIN_id=request.session['lid'])  # Assuming the user is logged in and request.user gives the current user
#     today = timezone.now().date()
#
#     # Filter Food records for the current user and today's date
#     calorie_data = Food.objects.filter(USER=user, date=today).aggregate(total_calories_burned=Sum('callorie'))
#     total_calories_burned = calorie_data['total_calories_burned'] or 0  # Ensure it's zero if no data
#
#     # Calculate the calorie goal based on BMI (example calculation)
#     user_profile = User.objects.get(LOGIN_id=request.session['lid'])
#     bmi = float(user_profile.bmi)
#     # Example: set a simple static goal, in reality this could be more complex
#     calorie_goal = 2000  # Placeholder for a more realistic calculation based on BMI
#
#     context = {
#         'total_calories_burned': total_calories_burned,
#         'calorie_goal': calorie_goal,
#     }
#     return render(request, 'user/today_callorie.html', context)



from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum
from .models import Food, User

def calculate_calorie_goal(bmi):
    """
    Calculate daily calorie goal based on BMI.
    This is a simple placeholder function.
    A more accurate method would involve BMR calculations and activity multipliers.
    """
    if bmi < 18.5:
        return 2500  # Underweight
    elif 18.5 <= bmi < 24.9:
        return 2000  # Normal weight
    elif 25 <= bmi < 29.9:
        return 1800  # Overweight
    else:
        return 1600  # Obese

def today_calories_view(request):
    user = User.objects.get(LOGIN_id=request.session['lid'])  # Get the logged-in user
    today = timezone.now().date()

    # Filter Food records for the current user and today's date
    calorie_data = Food.objects.filter(USER=user, date=today).aggregate(total_calories_burned=Sum('callorie'))
    total_calories_burned = calorie_data['total_calories_burned'] or 0  # Ensure it's zero if no data

    # Calculate the calorie goal based on BMI
    bmi = float(user.bmi)
    calorie_goal = calculate_calorie_goal(bmi)

    context = {
        'total_calories_burned': total_calories_burned,
        'calorie_goal': calorie_goal,
    }
    return render(request, 'user/today_callorie.html', context)

def exercises(request):

    l=['Walking(2.5)','Walking(3.5)','Jogging','Running','Cycling','Swimming','Yoga',
       'Weightlifting','Skipping','Rowing']
    l1=[3.5,4.3,7,9.8,6,6,2.5,3,12,7]
    ob=Exercises.objects.filter(USER__LOGIN__id=request.session['lid'])
    return render(request, 'user/exercises.html',{"i":ob,"e":l})
def exercises1(request):

    l=['Walking(2.5)','Walking(3.5)','Jogging','Running','Cycling','Swimming','Yoga',
       'Weightlifting','Skipping','Rowing']
    l1=[3.5,4.3,7,9.8,6,6,2.5,3,12,7]
    t=request.POST['t']
    d=request.POST['d']
    i=l.index(t)
    uob=User.objects.get(LOGIN__id=request.session['lid'])
    c=l1[i]*float(d)*float(uob.weight)
    ob=Exercises()
    ob.USER = uob
    ob.time = d
    ob.type = t
    ob.date=datetime.datetime.today()
    ob.callorie=c
    ob.save()
    return redirect("/exercises#abc")
def emotion(request):
    ob=[]#Emotion.objects.filter(USER__LOGIN__id=request.session['lid'])
    return render(request, 'user/Emotion.html',{"i":ob})
def emotion1(request):
    q1=int(request.POST['q1'])
    q2=int(request.POST['q2'])
    q3=int(request.POST['q3'])
    q4=int(request.POST['q4'])
    q5=int(request.POST['q5'])
    h=round(((q1+q2+q3+q4+q5)/20)*100,2)
    s=100-h
    ob=Emotion()
    ob.USER = User.objects.get(LOGIN__id=request.session['lid'])
    ob.happy = h
    ob.stress = s
    ob.date=datetime.datetime.today()
    ob.save()
    return render(request, 'user/Emotion1.html', {"i": ob})




def admin_view_expert_report(request):

    var=Experts.objects.all()
    return render(request,'admin/reports.html',{'data':var})

def admin_view_expert_report_post(request):
    f=request.POST['f']
    t=request.POST['t']
    var=Experts.objects.filter(date__range=[f,t])
    return render(request,'admin/reports.html',{'data':var})


def admin_view_user_report(request):

    var=User.objects.all()
    return render(request,'admin/admin_view_users_report.html',{'data':var})


def admin_view_user_report_post(request):
    f=request.POST['f']
    t=request.POST['t']
    var=User.objects.filter(date__range=[f,t])
    return render(request,'admin/admin_view_users_report.html',{'data':var})


def admin_view_complaint_report(request):

    var=Complaints.objects.all()
    return render(request,'admin/admin_view_complaint_report.html',{'data':var})

def admin_view_complaint_report_post(request):
    f=request.POST['f']
    t=request.POST['t']
    var=User.objects.filter(date__range=[f,t])
    return render(request,'admin/admin_view_complaint_report.html',{'data':var})


def admin_view_feedback_report(request):

    var=Feedback.objects.all()
    return render(request,'admin/admin_view_feedback_report.html',{'data':var})

def admin_view_feedback_report_post(request):
    f=request.POST['f']
    t=request.POST['t']
    var=Feedback.objects.filter(date__range=[f,t])
    return render(request,'admin/admin_view_feedback_report.html',{'data':var})

