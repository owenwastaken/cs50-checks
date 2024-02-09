import check50
import re

@check50.check()
def doesnt_crash():
    """decrypt.py doesn't throw an exception"""
    check50.include("decrypt.csv")
    check50.run("python3 decrypt.py").exit(0)


@check50.check()
def decrypt():
    """Decrypts secret note"""
    expected_regex = r"nevergonnagiveyouup!\n?"

    # Copy decrypt.csv into the program's working directory
    check50.include("decrypt.csv")

    # Run program and log output so students can see what their program is doing
    actual = check50.run("python3 decrypt.py").stdout()
    check50.log(f'Note decrypted to "{actual}"')

    # Fail the check if the decrypted note is not the expected result
    if not re.match(expected_regex, actual):
        raise check50.Failure("Did not decrypt note correctly.", help="Make sure you are only printing your decrypted note")

