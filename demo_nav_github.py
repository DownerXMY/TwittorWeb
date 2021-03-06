import os
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv='X-UA-Compatible' content='ie=edge'>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <script src="http://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
    <title>Github</title>
</head>
<body>
    <nav class='navbar navbar-expand-lg justify-content-center navbar-dark bg-dark'><!--To Add Nevigation Bar-->
        <nav class="navbar navbar-dark bg-dark">
            <a class="navbar-brand" href="#">
                <svg class="octicon octicon-mark-github text-white" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
            </a>
        </nav>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class='navbar-nav'>
        <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle text-white" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Why Github?</a>
            <div class='dropdown-menu' aria-labelledby="navbarDropdown">
                <a class='dropdown-item' href="#"><b>Features</b></a>
                <a class='dropdown-item' href="#">Code Review</a>
                <a class='dropdown-item' href="#">Project Management</a>
                <a class='dropdown-item' href="#">Integrations</a>
                <a class='dropdown-item' href="#">Team Management</a>
                <a class='dropdown-item' href="#">Social Coding</a>
                <a class='dropdown-item' href="#">Documentation</a>
                <a class='dropdown-item' href="#">Code Hosting</a>
                <div class='dropdown-divider'></div>
                <a class='dropdown-item' href="#"><b>Case Studies</b></a>
                <a class='dropdown-item' href="#"><b>Security</b></a>
            </div>
        </li>
        <li class='nav-item'>
            <a class="nav-link text-white" href="">Business</a>
        </li>
        <li class='nav-item dropdown'>
            <a class="nav-link dropdown-toggle text-white" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Explore</a>
            <div class='dropdown-menu' aria-labelledby="navbarDropdown">
                <a class='dropdown-item' href="#"><b>Explore Github</b></a>
                <div class='dropdown-divider'></div>
                <a class='dropdown-item' href="#">Learn & Contribute</a>
                <a class='dropdown-item' href="#">Topics</a>
                <a class='dropdown-item' href="#">Collections</a>
                <a class='dropdown-item' href="#">Trending</a>
                <a class='dropdown-item' href="#">Learning Lab</a>
                <a class='dropdown-item' href="#">Open Source Guides</a>
                <div class='dropdown-divider'></div>
                <a class='dropdown-item' href="#">Connect With Others</a>
                <a class='dropdown-item' href="#">Events</a>
                <a class='dropdown-item' href="#">Community Forum</a>
                <a class='dropdown-item' href="#">Github Education</a>
            </div>
        </li>
        <li class='nav-item'>
            <a class="nav-link text-white" href="">Marketplace</a>
        </li>
        <li class='nav-item dropdown'>
            <a class="nav-link dropdown-toggle text-white" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Pricing</a>
            <div class='dropdown-menu' aria-labelledby="navbarDropdown">
                <a class='dropdown-item' href="#"><b>Plans</b></a>
                <a class='dropdown-item' href="#">Compare Plans</a>
                <a class='dropdown-item' href="#">Contact Sales</a>
                <div class='dropdown-divider'></div>
                <a class='dropdown-item' href="#"><b>Nonprofit</b></a>
                <a class='dropdown-item' href="#"><b>Education</b></a>
            </div>
        </li>
        <li class='nav-item'>
            <input class="form-control mr-auto" type="search" placeholder="Search Github" aria-label="Search">
        </li>
        <li class='nav-item'>
            <a class="nav-link text-white" href="">Sign in</a>
        </li>
        <li class='nav-item'>
            <button class="btn btn-outline-warning text-white" type="submit">Sign up</button>
        </li>
    </ul>
    </div>
    </nav>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0')

    

