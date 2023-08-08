# Laundry Managment System

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/MeetSherasiya/laundry_managment_system.git
$ cd laundry_managment_system
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd laundry_managment_system
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Home Page
<img src='screenshot/homepage.png' >
<br>
<p>Add Product Page</p>
<img src='screenshot/addproduct.png'>
<br>
<p>All Product Page</p>
<img src='screenshot/allproduct.png'>
<br>
<p>Customer Bills Page</p>
<img src='screenshot/customerbill.png'>
<br>
<p>Bill Page</p>
<img src='screenshot/bill.png'>
