import check50

@check50.check()
def doesnt_crash():
    """decrypt.py doesn't throw an exception"""
    check50.run("python3 decrypt.py").exit(0)


@check50.check()
def decrypt():
    """Decrypts secret note"""
    expected = "nevergonnagiveyouup!"

    # Run program and log output so students can see what their program is doing
    actual = check50.run("python3 decrypt.py").stdout()
    cs50.log(f"Note decrypted to "{actual}")

    # Fail the check if the decrypted note is not the expected result
    if actual != expected:
        raise check50.Failure("Did not decrypt note correctly.", help="Make sure you are only printing your decrypted note")

