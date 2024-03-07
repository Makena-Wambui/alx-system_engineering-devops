pache is one of the most popular web servers in the world
It serves 50% of all active websites.
You have to master the art of parsing log files.
Log file- a file that records events from certain software and OSs
Contains a record of events for certain software and OSs:
a historical record of all events, processes, and messages along with additional descriptive data,
like timestamps, to contextualize this information.
They show all events associated with the system or application that created them.

Parsing log files:
------------------
Process of converting log data into a common format so they are machine readable.
Log parsing translates structured or unstructured log files so our log management system can read, index and store their data.
Involves splitting large volumes of logs so they are easy to interpret, analyze and store.

Visitor IP is the Ip address of a visitor to a website.
What is an IP address?
------------------------
It is a unique string of letters and/or numbers that identifies a device like a computer or a smart phone on a network.
When you access a website, their IP address can be logged. and used to identify their general geographical location.
This is useful as it helps to know where your website's traffic is coming from, among other things
Now write a bash script that will display visitor IPs and their HTTPS STATUS CODES from the apache log file.

After parsing the log file, we can sort the data toget a better idea of what is happening.
if a particular ip address accessed a website five times, and each time received a https status code of 200,
there would be 5 occurences of that specific event.
Sort command sorts output
uniq -c counts the number of occurences of each unique line
sort -nr sort the output in reverse numerical order so lines with the most occurences are at the top.

