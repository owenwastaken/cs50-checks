import check50
import re


@check50.check()
def decrypt():
    """Decrypts secret note"""
    expected_regex = r"nevergonnagiveyouup!\n?"

    check50.log(f'Attempting to run the program without passing secret code as input')

    try:
        # Run program and log output so students can see what their program is doing
        actual = check50.run("python3 decrypt.py").stdout()
        check50.log(f'Note decrypted to "{actual}"')
    except check50.Failure:
        check50.log("Attempting to run the program with passing secret code as input")
        actual = check50.run("python3 decrypt.py").stdin("🔉🎁🚊🎁📂👿🚿🔉🔉👇👿💣🚊🎁🎫🚿🚆🚆🐤!").stdout()


    # Fail the check if the decrypted note is not the expected result
    if not re.match(expected_regex, actual):
        raise check50.Failure("Did not decrypt note correctly.", help="Make sure you are only printing your decrypted note")

