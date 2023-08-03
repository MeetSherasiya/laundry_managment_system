function register(){
    var username = document.getElementById('username').value
    var email = document.getElementById('email').value
    var password = document.getElementById('password').value
    var password1 = document.getElementById('password1').value
    var csrf = document.getElementById('csrf').value

    var data = {
        'username': username,
        'email': email,
        'password': password,
        'password1': password1
    }

    fetch('/api/register/', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf
        },
        body : JSON.stringify(data)
    }).then(result => result.json()).then(response => {
        console.log(response)
        if(response.status == 201){
            alert("Registration Successfully");
            document.getElementById('username').value = '';
            document.getElementById('email').value = '';
            document.getElementById('password').value = '';
            document.getElementById('password1').value = '';
            window.location.href = '/login';
        }else{
            alert(response.message);
            location.reload();
        }
    })
}


function newreq(){
    var pickup = document.getElementById('pickup').value
    var topwear = document.getElementById('topwear').value
    var bottomwear = document.getElementById('bottomwear').value
    var woolencloth = document.getElementById('woolencloth').value
    var othercloth = document.getElementById('othercloth').value
    var servicetype = document.getElementById('servicetype').value
    var address = document.getElementById('address').value
    var mobilenumber = document.getElementById('mobilenumber').value
    var description = document.getElementById('description').value
    var csrf = document.getElementById('csrf').value

    if (topwear.trim() === '') {
        topwear = 0;
    }

    if (bottomwear.trim() === '') {
        bottomwear = 0;
    }

    if (woolencloth.trim() === '') {
        woolencloth = 0;
    }

    if (othercloth.trim() === '') {
        othercloth = 0;
    }

    var data = {
        'pickup': pickup,
        'topwear': topwear,
        'bottomwear': bottomwear,
        'woolencloth': woolencloth,
        'othercloth': othercloth,
        'servicetype': servicetype,
        'address': address,
        'mobilenumber': mobilenumber,
        'description': description
    }
    fetch('/api/newreq/', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrf
        },
        body : JSON.stringify(data)
    }).then(result => result.json()).then(response => {
        console.log(response)
        if(response.status == 201){
            window.location.href = '/newreq/';
            alert("Request Sent Successfully");
        }else{
            alert(response.message)
        }
    })
}