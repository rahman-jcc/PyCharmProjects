# Function to display hostname and
# IP address
def get_Host_name_IP():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        domain_name = socket.getfqdn().split('.', 1)
        print("Hostname :  ", host_name)
        print("IP : ", host_ip)
        print("Default domain : ", domain_name)
    except:
        print("Unable to get Hostname and IP")


get_Host_name_IP() 