# Drill 2: Using Lists

from pyscript import display, document 

def check_list (e): 
    document.getElementById('result').innerHTML = ' '

    given_name = document.getElementById('first_name').value.title().strip()
    surname = document.getElementById('last_name').value.title().strip()
    math_guild_members_name = given_name + " " + surname 

    names = ["Rene Baterbonia", "John Batumbahay", "Alejandro Araw", "Sito Policarpio", "Zion Ribaya"]

    student_checker = math_guild_members_name in names 

    display_message = (f'Sorry, {math_guild_members_name} is not in the Math Guild. Try again next year.', f'Congratulations, {math_guild_members_name} is in the club list! We look forward to having a great time with you in Math Guild.')
    display(display_message[student_checker], target='result')