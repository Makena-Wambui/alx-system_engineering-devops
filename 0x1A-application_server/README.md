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
</BODY>
</HTML>
