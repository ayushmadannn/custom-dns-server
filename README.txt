DNS Server Visualizer

In our project we have visualised a DNS server that returns the ip adress for a given website. We have used MySQL, python and django. 

In our DNS server the query goes to the root server through the resolver which returns the tld ip to the resolver.  We then query the tld server based on tld ip and domain to get the ans_ip. We finally query the ans server with ans ip to get ip of the website which is returned.

In the front-end you can either enter input for recursive or iterative DNS server, website: http://localhost:8000/polls/
Based on your choice the site will output the ip from either recursive or iterative server. You can acess this by running python manage.py runserver in mysite directory containing manage.py. CD into the directory containing manage.py before running this command.

After that you go to http://localhost:8000/polls/ and can enter input of your choice. 
Reccommend refreshing after going to http://localhost:8000/polls/ for further queries but works fine otherwise also.

The database in views.py is configured to my sql, change it to yours to work

the program only works on the following domains
domain
google.com
facebook.com
instagram.com
youtube.com
amazon.com
snapchat.com
twitter.com
paypal.com
netflix.com
whatsapp.com
slideshare.net
php.net
battle.net
behance.net
speedtest.net
expolsm.net
sourceforge.net
americanapparel.net
sickdeals.net
docusign.net
wikipedia.org
telegram.org
archive.org
mozilla.org
craigslist.org
coursera.org
wordpress.org
wikimedia.org
geeksforgeeks.org
google.org
google.in
facebook.in
youtube.in
amazon.in
primevideo.in
bits-pilani.ac.in
twitter.in
godaddy.in
namecheap.in
hostinger.in