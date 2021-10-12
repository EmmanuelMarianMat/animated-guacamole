alpha_to_morse = {
   "A":"._",
   "B":"_...",
   "C":"_._.",
   "D":"_..",
   "E":".",
   "F":".._.",
   "G":"__.",
   "H":"....",
   "I":"..",
   "J":".___",
   "K":"_._",
   "L":"._..",
   "M":"__",
   "N":"_.",
   "O":"___",
   "P":".__.",
   "Q":"__._",
   "R":"._.",
   "S":"...",
   "T":"_",
   "U":".._",
   "V":"..._",
   "W":".__",
   "X":"_.._",
   "Y":"_.__",
   "Z":"__..",
   "1":".____",
   "2":"..___",
   "3":"...__",
   "4":"...._",
   "5":".....",
   "6":"_....",
   "7":"__...",
   "8":"___..",
   "9":"____.",
   "0":"_____",
   ", ":"__..__",
   ".":"._._._",
   "?":"..__..",
   "/":"_.._.",
   "_":"_...._",
   "(":"_.__.",
   ")":"_.__._",
   "!":"__..__",
   "'":".____."
}

morse_to_alpha = {
   "._":"A",
   "_...":"B",
   "_._.":"C",
   "_..":"D",
   ".":"E",
   ".._.":"F",
   "__.":"G",
   "....":"H",
   "..":"I",
   ".___":"J",
   "_._":"K",
   "._..":"L",
   "__":"M",
   "_.":"N",
   "___":"O",
   ".__.":"P",
   "__._":"Q",
   "._.":"R",
   "...":"S",
   "_":"T",
   ".._":"U",
   "..._":"V",
   ".__":"W",
   "_.._":"X",
   "_.__":"Y",
   "__..":"Z",
   ".____":"1",
   "..___":"2",
   "...__":"3",
   "...._":"4",
   ".....":"5",
   "_....":"6",
   "__...":"7",
   "___..":"8",
   "____.":"9",
   "_____":"0",
   "__..__":", ",
   "._._._":".",
   "..__..":"?",
   "_.._.":"/",
   "_...._":"_",
   "_.__.":"(",
   "_.__._":")",
   "__..__":"!",
   ".____.": "'"
}

def encrypt():
    alpha_string = input("Enter your string which contains only alphanumeric characters or the following characters, .,?/-()!': ").rstrip()
    words = alpha_string.split()
    morse_string = ''
    try:
        for word in words:
            for letter in word:
                if letter.isalpha():
                    morse_string+=(alpha_to_morse[letter.upper()] + ' ')
                else:
                    morse_string+=(alpha_to_morse[letter] + ' ')
            morse_string += '| '
        print('Here is your Morse translation:', morse_string[:-2])
    except KeyError:
        print('This string has one or more invalid characters')
    pass

def decrypt():
    morse_string = input('Type your morse code using . and _, seperating letters by spaces and words by |: ')
    words = morse_string.split('|')
    letters = [word.split() for word in words]
    alpha_string = ''
    try:
        for word in letters:
            for letter in word:
                alpha_string += morse_to_alpha[letter]
            alpha_string += ' '
        print('Here is the English translation:', alpha_string.lower())
    except KeyError:
        print('This morse string is invalid')

def main():
    while True:
        choice = input('Enter "e" for string to morse code translation, "d" for morse code to string translation, "q" to quit the program: ').rstrip()
        if choice in ['e','E']:
            encrypt()
        elif choice in ['d','D']:
            decrypt()
        elif choice in ['q','Q']:
            break
        else:
            print('Please enter a valid character')
        print()

if __name__ == '__main__':
    main()
