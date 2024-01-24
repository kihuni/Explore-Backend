import cgi

# Create an instance of the FieldStorage class to handle the CGI form data
form = cgi.FieldStorage()


# Get the value of a form field
name = form.getvalue('name')


# Print the HTTP headers
print("Content-type: text/html\n")

# Generate the HTML response
print("<html>")
print("<head>")
print("<title>CGI Example</title>")
print("</head>")
print("<body>")
print("<h1>Hello, {}!</h1>".format(name))
print("</body>")
print("</html>")
