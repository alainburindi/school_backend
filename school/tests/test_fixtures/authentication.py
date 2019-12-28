create_user = '''mutation{{
            createUser(email: "{email}", username: "{username}",
             password: "{password}"){{
                message
                user{{
                    email
                    username
                }}
            }}
        }} '''

login_user = '''
mutation{{
  login(email: "{email}", username:"{username}", password:"{password}"){{
    message
    token
    }}
  }}
'''

login_empty_email_and_username = '''
mutation{
  login(password:"password234"){
    message
    token
    }
  }
'''
