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
