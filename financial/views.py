from django.shortcuts import render
from financial.models import Transaction
from django.db import connection

def trans(request, user_id):
    t= Transaction.objects.filter(user__id__exact= user_id )
    cursor = connection.cursor()
    cursor.execute('SELECT t.amount FROM financial_Transaction t INNER JOIN financial_User u ON t.user_id=u.id WHERE u.id= %s', [user_id])
    am = cursor.fetchall()
    cursor.execute('SELECT t.date FROM financial_Transaction t INNER JOIN financial_User u ON t.user_id=u.id WHERE u.id= %s', [user_id])
    da= cursor.fetchall()
    return render(request, "trans.html", {'trans' : t, 'amounts' : am, 'dates' : da})