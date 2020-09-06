#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Auth..</title>
</head>
<body>
    <fieldset>
        <legend>Form Auth.......</legend>
    <form action="demo.py" method="POST">
       <br> <label for="name"> User Name: <br>
            <input required type="text" id="name" name="name" autocomplete="off">
        </label> <br>

        <label for="email"> User Email: <br>
            <input required type="email" id="email" name="email" autocomplete="off">
        </label> <br>

        <label for="password"> Password: <br>
            <input required type="text" id="password" name="password" autocomplete="off">
        </label> <br> <br>

            <input type="submit" value="submit"> <br> <br> 
    </form> 
    </fieldset>
</body>
</html>
""") 
 