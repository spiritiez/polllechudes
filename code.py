#выбираем загаданное слово "вслепую"
choice = set("заяц", "солнце", "вафля", "вампир", "чай", "глаза", "цветочки", "кепка", "котик", "кружка", "буква")
#присваиваем переменной word соответствующее значение
word = choice[0]
    
gamepad = "*" * len(word) #выводим звездочки на местах букв в загаданном слове    
myenters = set() #это будет множеством вводов игрока
mywins = set() #это - множество угаданных букв
commands = set() #все команды
commands.add("helpme")
commands.add("myenters")
commands.add("mywins")
commands.add("giveup")

alphabet = "йцукенгшщзхъфывапролджэёячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЁЯЧСМИТЬБЮ"
helpme = "helpme - вывести правила игры" + "/n" + "myenters - вывести все буквы, введенные игроком за текущий раунд" + "/n" + "mywins - вывести угаданные игроком буквы за текущий раунд" + "/n" + "giveup - с помощью этой команды игрок может сдаться и увидеть загаданное слово, но при этом он проиграет"
print("Добро пожаловать в игру! Перед вами зашифрованное слово, вы должны вводить буквы и отгадывать его. Подробнее о правилах игры узнайте с помощью команды helpme")
print(gamepad) #выводим звездочки со строки 11
attempts = len(word) * 2

while attempts > 0: #пока у нас не кончатся попытки, мы можем играть 
    ent = input() #ввод игрока
    if ent in commands: #проверяем, не команда ли это
        if ent == "mywins":
            for elem in mywins:
                print(elem, end=" ")
            print("\n") 
        if ent == "helpme":
            print(helpme)
        if ent == "myenters":
            for elem in myenters:
                print(elem, end=" ")
            print("\n")
        if ent == "giveup":
            print(len(myenters), "попыток")
            print("ВЫ ПРОИГРАЛИ")
            print("загаданное слово:", word)
            break
        
        attempts += 1
    
    elif ent == word: #проверяем, не угадал ли игрок за одну попытку слово
        print(word)
        print(len(myenters), "попыток")
        print("ПОБЕДА")
        break 
    
    elif ent in myenters: #проверяем,была ли введенная буква уже до этого
        print("такую букву вы уже пробовали")
            
    elif ent in word: #если буква есть в слове
        print("верно!!!")
        letter = 0
        while word[letter] != ent:
            letter += 1
        gamepad = gamepad[:letter] + ent + gamepad[letter + 1:]
        myenters.add(ent)
        mywins.add(ent)
        if gamepad == word: #проверяем, не угадал ли игрок за эту попытку слов
            print(word)
            print(len(myenters), "попыток")
            print("ПОБЕДА")
            break
          
    elif ent in alphabet and ent not in word:
        print("неверно")
        myenters.add(ent)
        
    else:
        print("ОШИБКА")
    print(gamepad)
    attempts -= 1 #уменьшаем количество попыток
    print("осталось попыток:", attempts) #выводим количество попыток
    
if gamepad != word and ent != "giveup":
    print("ПРОИГРЫШ")
    print("загаданное слово:", word) 
