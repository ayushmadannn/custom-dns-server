# custom-dns-server
##Custom visualizaton of a simple DNS Server

DNS Server Visualization


System Requirement Specification:

A DNS server (short for domain-name-system server), in very simple terms, would be a server
that maps IP addresses (which are a series of numbers separated by full stops that identify a
device/server on a network) to domain names. For example, www.google.com would be
mapped to an IP address like 8.8.8.8, which makes it a lot easier for users to just remember
google.com instead of remembering the entire list of numbers.

There are 2 main types of queries we’ll be working on :-
(a)Recursive queries
(b)Iterative queries

A recursive DNS query would comprise of a client who would request for a domain to be
resolved, a recursive dns resolver which would act as an interface between the client and other
servers, a root server which would redirect the request to the correct top level domain server
depending on the domain, a TLD (top level domain) server which would redirect the request to
the correct authoritative server, and finally an Authoritative server (also called nameserver)
which would fetch back the correct IP address of the domain requested to the recursive server
which in turn would fetch it back to the client, after storing the record in its own local cache.
An iterative DNS query would comprise of a client who would request for a domain to be
resolved, a DNS resolver similar to the one in the recursive dns above, but the difference being
it would fetch back only the referrals to other root servers instead of querying other servers
itself. Here, the client would have to query root, TLD and authoritative servers himself.
The servers would also be storing different types of data records. The root and TLD servers
would be storing CNAME records - which maps one type of domain to another domain and
Authoritative servers and recursive servers(local cache) would contain A records - which map
domains to IP addresses.
So, our visualization of a DNS server would comprise of these data requirements.


System Requirements:
The following are the system requirements for our DNS server visualization :-
1. MySQL
2. Python
3. Django
4. Windows Machine
5. Import pymysql library


Entity Relationship:
We have the entities as shown in the following diagrams as shown below, which are of recursive
and iterative dns queries respectively.
The relationship between each entity is more or less the same, where the requested server
fetches back an ip address
