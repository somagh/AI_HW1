# IN THE NAME OF ALLAH


def search(parsed, address, text):

    s = ""
    arr = parsed.select(address)

    texts = ""
    for i in range(len(text)):
        if text[i] != '\n' and text[i] != ' ' and text[i] != '\t':
            texts += text[i]
    text = texts

    for i in range(len(arr)):
        if arr[i].name == 'img':
            src = arr[i].get('src')
            if src.find(text) >= 0:
                return True

        arri_images = arr[i].find_all('img')
        for j in range (len(arri_images)):
            src = arri_images[j].get('src')
            # print(arri_images[j], "\n\n", address, "\n\n ",  src, "\ninja src\n\n")
            if src.find(text) >= 0:
                return True

    for i in range(len(arr)):
        s += arr[i].get_text()

    ss = ""
    for i in range(len(s)):
        if s[i] != '\n' and s[i] != ' ' and s[i] != '\t' and ord(s[i]) != 13:
            ss += s[i]

    s = ss

    #print(address, "inja address \n\n\n", ss, "\n\n", text, "\n\n", s.find(text), "\n\n")

    return s.find(text) >= 0
