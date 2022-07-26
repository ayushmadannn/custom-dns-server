from django.shortcuts import render
from django.http import HttpResponse
import pymysql

#from .forms import NameForm

# Create your views here.
def index(request):
    return HttpResponse("Hello World! You're at the polls index")

def homepage(request):
    return render(request, 'polls/page.html')

def recursive(request):
    domain = request.POST.get("domain")

    con = pymysql.connect(host='localhost', user='root',password='dilip', database='test')

    try:

        with con.cursor() as cur:
            s1 = "update recursive_resolver set recursive_resolver.tld_ip=(select root.tld_ip from root where domain = '"+ domain +"') where recursive_resolver.domain ='"+ domain +"';"
            s2 = "update recursive_resolver set recursive_resolver.ans_ip=(select ans_ip from tld where tld_ip = (select tld_ip from root where domain = '"+ domain +"') and domain = '"+ domain +"' ) where recursive_resolver.domain ='"+ domain +"';"
            s3 = "update recursive_resolver set recursive_resolver.ip=(select ip from ans where ans_ip = (select ans_ip from tld where tld_ip = (select tld_ip from root where domain = '"+ domain +"') and domain = '"+ domain +"'))where recursive_resolver.domain ='"+ domain +"';"
            s4 = "select ip from recursive_resolver where domain='"+ domain +"';"


            cur.execute(s1)
            cur.execute(s2)
            cur.execute(s3)
            cur.execute(s4)
            rows = cur.fetchall()

            for row in rows:
                print(f'{row[0]}')
                x = {row[0]}

    finally:

        con.close()
    string1 = "ip address: "+ str(x)
    return HttpResponse("recursive "+string1)

def iterative(request):
    domain = request.POST.get("domain")

    con = pymysql.connect(host='localhost', user='root',password='dilip', database='test1')

    try:

        with con.cursor() as cur:
            s1 = "update computer set computer.tld_ip=(select root.tld_ip from root where domain = '"+ domain +"') where computer.domain ='"+ domain +"';"
            s2 = "update computer set computer.ans_ip=(select ans_ip from tld where tld_ip = (select tld_ip from root where domain = '"+ domain +"') and domain = '"+ domain +"' ) where computer.domain ='"+ domain +"';"
            s3 = "update computer set computer.ip=(select ip from ans where ans_ip = (select ans_ip from tld where tld_ip = (select tld_ip from root where domain = '"+ domain +"') and domain = '"+ domain +"'))where computer.domain ='"+ domain +"';"
            s4 = "select ip from computer where domain='"+ domain +"';"


            cur.execute(s1)
            cur.execute(s2)
            cur.execute(s3)
            cur.execute(s4)
            rows = cur.fetchall()

            for row in rows:
                print(f'{row[0]}')
                x = {row[0]}

    finally:

        con.close()
    string1 = "ip address: "+ str(x)
    return HttpResponse("iterative "+string1)
