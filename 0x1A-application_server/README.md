<!DOCTYPE HTML>
<HTML LANG='EN'>
<BODY>
<H1>APPLICATION SERVER VERSUS WEB SERVER</H1>

<P>
These two servers are usually deployed together for a common purpose, that is fulfilling user requests for
content from a website.
</P>

<P>
What is a web server's fundamental job?
	
	To accept and fulfill requests from clients for static content from a website.
	
	For example: images, files, video, HTML Pages.

	The client is almost always a browser or web application.
	
	The request is in the form of a HTTP message as does the web server's response.

</P>

<P>
What is an Application server's fundamental job?
	
	To provide its clients with access to business logic, which generates dynamic content.
	
	This is code that transforms data to provide the specialized functionality of a business, service or application.
	
	Its clients are often applications themselves; and can include web servers and other application servers.
	
	Communication between an application server and its clients might take the form of HTTP Messages,
	
	But this is not mandatory as it is for web servers and their clients.
	
	Communication can use other protocols, including the variants of CGI.
</P>

<H2>HOW DO WEB SERVERS AND APPLICATION SERVERS WORK TOGETHER?</H2>
<P>
A website that serves both static content and dynamically generated content runs web servers for the static content
and application servers for the dynamically generated content.

A reverse proxy and a load balancer sit in front of one or more web servers and one or more web application servers to route traffic to the appropriate server, based on:
	
	1. The type of content requested.

	2. The configured load balancing algorithm.



</P>

<H2>CONFIGURING NGINX TO PROXY REQUESTS TO GUNICORN</H2>
<P>
The `location /` block in your Nginx configuration specifies how Nginx should handle requests that match a particular path. The `/` means it will match any request that comes to the server. 

For your specific requirement, where you need Nginx to serve your page from the route `/airbnb-onepage/`, you should modify the `location` block to reflect that path. Here’s how you can update your configuration:


server {
    listen 80;
    server_name IP_ADDR;

    location /airbnb-onepage/ {
        include proxy_params;
        proxy_pass http://127.0.0.1:5000;
    }
}



- `location /airbnb-onepage/: This block tells Nginx to only proxy requests that match `/airbnb-onepage/`.
So, any request like `http://your_domain/airbnb-onepage/` will be forwarded to the process listening on port 5000.
-`proxy_pass http://127.0.0.1:5000;`: This line forwards the matching requests to `127.0.0.1` on port `5000`, where your Gunicorn server is running.

After making these changes, save the file and test the Nginx configuration:

sudo nginx -t

If the test is successful, restart Nginx to apply the new configuration:

sudo systemctl restart nginx


This will allow Nginx to serve your page at http://18.235.243.79/airbnb-onepage/`
</P>

<P>
Location blocks live within server blocks or other location blocks

They are used to decide how to process the request URI ie 
the part that comes after the domain name or IP Address/Port.

	syntax: location optional_modifier location_match {......}

	location_match defines what Nginx should check the request Uri against.

	Existence or nonexistence of the optional_modifier affects the way that Nginx attempts
	to match the location block.
	
</P>
</BODY>
</HTML>
