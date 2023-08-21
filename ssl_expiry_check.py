from OpenSSL import SSL
import socket
import datetime

# List of domains to check
domains = ["google.com"]

for domain in domains:
    try:
        # Create an SSL context
        context = SSL.Context(SSL.TLSv1_2_METHOD)
        
        # Create a socket and connect to the domain
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((domain, 443))
        
        # Wrap the socket in the SSL context
        ssl_sock = SSL.Connection(context, sock)
        ssl_sock.set_tlsext_host_name(domain.encode())
        ssl_sock.set_connect_state()
        ssl_sock.do_handshake()
        
        # Get the SSL certificate
        cert = ssl_sock.get_peer_certificate()
        
        # Get the certificate expiry date
        expiry_date = datetime.datetime.strptime(cert.get_notAfter().decode("utf-8"), "%Y%m%d%H%M%SZ")
        
        # Calculate the remaining days to expiry
        remaining_days = (expiry_date - datetime.datetime.now()).days
        
        # Print the SSL expiry information
        print(f"Domain: {domain}")
        print(f"Remaining Days to Expiry: {remaining_days}")
        
        # Close the SSL connection
        ssl_sock.shutdown()
        ssl_sock.close()
    
    except Exception as e:
        # Handle any exceptions that occur during the SSL check
        print(f"Error checking SSL for {domain}: {str(e)}")

