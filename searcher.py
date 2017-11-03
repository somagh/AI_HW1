# IN THE NAME OF ALLAH


def search(parsed, address, text):

    s = ""
    arr = parsed.select(address)

    for i in range(len(arr)):
        s += arr[i].get_text()

    ss = ""
    for i in range(len(s)):
        if s[i] != '\n' and s[i] != ' ' and s[i] != '\t' and ord(s[i]) != 13:
            ss += s[i]

    s = ss

    texts = ""
    for i in range(len(text)):
        if text[i] != '\n' and text[i] != ' ' and text[i] != '\t':
            texts += text[i]

    text = texts

    # print(arr, s.find(text) >= 0, text, "inja search", s, len(s), address," inja address ", " \n\n\n\n\n\n\n\n\n\n\ninja arvandi \n\n\n")

    return s.find(text) >= 0