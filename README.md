# Password Locker

Password Locker is an application that helps users generate and store passwords on their multiple accounts. The password locker runs on the terminal and uses short codes to navigate through it.


## Author name

Alex Ogola

## Technology used

Python 3.6

## Project setup installation

1.On GitHub, navigate to the main page of the repository.

2.Under the repository name, click Clone or download.

3.In the Clone with HTTPs section, click  to copy the clone URL for the repository.

4.Open Terminal.

5.Change the current working directory to the location where you want the cloned directory to be made.

6.Type git clone, and then paste the URL you copied in Step 2.

7.Press Enter. Your local clone will be created.

8.Have python3.6 is installed on your machine

## Behaviour driven development
| Behaviour   |      Input     |  Output |
|----------|:-------------:|------:|
| Display codes for navigation| In terminal: $./p_locker.py |   Welcome, choose an option: ca-Create Account, li-Log In, ex-Exit |
| Display prompt for creating an account | Enter: ca |   Enter your first name, last name and password |
| Display prompt for login in | Enter: li |   Enter your account name and password |
| Display codes for navigation | Successful login |   Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit |
| Display prompt for creating a credential | Enter: cc |   Enter the site name, your username and password |
| Display a list of credentials | Enter: dc |   Prints a list of saved credentials |
| Display prompt for which credential to copy | Enter: copy |   Enter the site name of the credential you wish to copy |
| Exit application | Enter: ex |   Exit the current navigation stage |



## Live link



## License
MIT licence

Copyright <YEAR> <COPYRIGHT HOLDER>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
