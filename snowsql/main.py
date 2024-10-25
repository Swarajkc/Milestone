from decouple import config


connect_dict = {
    'username': config('SNOWFLAKE_USERNAME'),
    'password': config('SNOWFLAKE_PASSWORD'),
    'hostname': config('SNOWFLAKE_HOST')
}

send_email = config("SEND_EMAIL_ON_REGISTER", default=True, cast=bool)
if send_email:
    print(f"Email Sent. {send_email} {type(send_email)}")
else:
    print("Registration Success.")