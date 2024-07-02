from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

# class Experts(models.Model):
#     LOGIN=models.ForeignKey(Login, on_delete=models.CASCADE)
#     image=models.CharField(max_length=500)
#     idproof=models.CharField(max_length=500)
#     name=models.CharField(max_length=100)
#     place=models.CharField(max_length=100)
#     post=models.CharField(max_length=100)
#     district=models.CharField(max_length=100)
#     phone=models.BigIntegerField()
#     email=models.CharField(max_length=100)
#     type=models.CharField(max_length=100)
#     status=models.CharField(max_length=100)


class Experts(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    image = models.CharField(max_length=500)
    idproof = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date = models.DateField()
    gender = models.CharField(max_length=100)  # Add this line


class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=30)
    height=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    image=models.CharField(max_length=400)
    bmi=models.CharField(max_length=400)
    date=models.DateField()
    calorie=models.FloatField()
    type=models.CharField(max_length=40)




class Payment(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()






class Complaints(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    complaints=models.CharField(max_length=400)
    date=models.DateField()
    status=models.CharField(max_length=100)
    reply=models.CharField(max_length=400)

class E_Complaints(models.Model):
    EXPERT=models.ForeignKey(Experts,on_delete=models.CASCADE,default='')
    complaints=models.CharField(max_length=400)
    date=models.DateField()
    status=models.CharField(max_length=100)
    reply=models.CharField(max_length=400)


class Feedback(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    feedback = models.CharField(max_length=100)
    date = models.DateField()

class E_Feedback(models.Model):
    EXPERT = models.ForeignKey(Experts, on_delete=models.CASCADE, default='')
    feedback = models.CharField(max_length=100)
    date = models.DateField()


class Chat(models.Model):
    FROMID = models.ForeignKey(Login, on_delete=models.CASCADE,related_name='fromid')
    TOID = models.ForeignKey(Login, on_delete=models.CASCADE,related_name='toid')
    date =  models.DateField()
    message = models.CharField(max_length=2000)


class Request(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    EXPERT = models.ForeignKey(Experts, on_delete=models.CASCADE, default='')
    status = models.CharField(max_length=100)
    date = models.DateField()


class Tutorial(models.Model):
    EXPERT = models.ForeignKey(Experts, on_delete=models.CASCADE, default='')
    description = models.CharField(max_length=500)
    file = models.CharField(max_length=500)
    pdf = models.CharField(max_length=500)
    title = models.CharField(max_length=500)
    date = models.DateField()


class Task(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    title = models.CharField(max_length=500)
    fromdate = models.DateField()
    todate = models.DateField()
    Duration = models.IntegerField()

class TaskEvaluation(models.Model):
    TASK = models.ForeignKey(Task, on_delete=models.CASCADE, default='')
    date = models.DateField()
    score = models.IntegerField()

class Food(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    type = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    date = models.DateField()
    gram = models.IntegerField()
    callorie=models.IntegerField()

class Event(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    event = models.CharField(max_length=500)
    status = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    rdate = models.DateField()
    rtime = models.TimeField()
class Emotion(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    happy = models.FloatField()
    stress = models.FloatField()
    date=models.DateField()

class Exercises(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    time = models.FloatField()
    type = models.CharField(max_length=50)
    date=models.DateField()
    callorie=models.IntegerField()


class Calnoti(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    date=models.DateField()




class Expertfeedback(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    EXPERT=models.ForeignKey(Experts,on_delete=models.CASCADE,default='')
    feedback=models.CharField(max_length=400)
    date=models.DateField()

