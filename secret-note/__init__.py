import check50

@check50.check()
def doesnt_crash():
    """decrypt.py doesn't throw an exception"""
    check50.run("python3 decrypt.py").exit(0)


@check50.check()
def decrypt():
    """Decrypts secret note"""
    expected = "nevergonnagiveyouup!"
    actual = check50.run("python3 decrypt.py").stdout()
    if actual != expected:
        raise check50.Mismatch("Shhhh! This is a secret!", actual, help="Make sure your program is printing just the output")


