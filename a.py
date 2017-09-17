hardConsonants = {"б", "в", "г", "д", "з", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х"}
unpairConsonants = {"ж", "ш", "ч", "щ", "ц"}
vowels = {"а", "о", "и", "е", "ё", "э", "ы", "у", "ю", "я"}
exceptions = {"Аникита", "Никита", "Мина", "Савва", "Сила", "Фока"}
consonants = hardConsonants | unpairConsonants | {"й"}
analysis = False
PATRONIM = False
BELONG = False


def del_last_vowels(a):
    while a[-1] in vowels:
        a = a[:-1]
    return a


def two_cons_not_nt(a):
    a = a.lower()
    if a[0] not in vowels:
        if a[1] not in vowels:
            if a != "нт":
                return True
    return False


def analyse_patronim(fatherName):
    ending = fatherName[-4:]
    if fatherName[-5:] in {"ьевич", "ьевна"}:
        print(fatherName[:-5] + "ий")
    elif ending in {"ович", "овна"}:
        stemName = fatherName[:-4]
        print(stemName)
        print(stemName + "а", stemName + "у", stemName + "ы")
        print(stemName + "о")
    elif ending in {"евич", "евна"}:
        stemName = fatherName[:-4]
        print(stemName)
        print(stemName + "' любая гласная'")
        print(stemName + "ь")
        print(stemName + "е")
        print(stemName + "й")
        print(stemName + "я")
    elif ending == "ична":
        stemName = fatherName[:-4]
        print(stemName + "а")
    else:
        stemName = fatherName[:-2]
        print(stemName + "а")


def synthesize_patronim(name):
    if name[-1] in hardConsonants:
        print(name + "ович,", name + "овна")
    elif name[-1] in unpairConsonants:
        print(name + "евич,", name + "евна")
    elif name[-1] in vowels and name[-2] in unpairConsonants:
        print(name[:-1] + "евич,", name[:-1] + "евна")
    elif name[-1] in {"а", "у", "ы"}:
        if name in exceptions:
            stemName = del_last_vowels(name)
            print(stemName + "ич,", stemName + "ична")
        else:
            stemName = del_last_vowels(name)
            print(stemName + "ович,", stemName + "овна")
    elif name[-2] in vowels and name[-1] in vowels:
        print(name + "евич,", name + "евна")
    elif name[-1] == "о":
        print(name + "вич,", name + "вна")
    elif name[-1] == "ь":
        print(name[:-1] + "евич,", name[:-1] + "евна")
    elif name[-1] == "е":
        print(name[:-1] + "евич,", name[:-1] + "евна")
    elif name[-1] in "и":
        print(name + "евич,", name + "евна")
    elif name[-2:] == "ий":
        if (name[-3] in {"к", "х", "ц"}) or (two_cons_not_nt(name[-4:-2])):
            print(name[:-1] + "евич,", name[:-1] + "евна")
        else:
            print(name[:-2] + "ьевич,", name[:-2] + "ьевна")
    elif name[-2:] in {"ея", "ия"}:
        print(name[:-1] + "евич,", name[:-1] + "евна")
    elif name[-1].isupper() and name[-1].lower() in vowels:
        print(name[:-1] + name[-1].lower() + "евич,", name[:-1] + name[-1].lower() + "евна")
    elif name[-1] == "й" and name[-2].isupper() and name[-2].lower() in vowels:
        print(name[:-2] + name[-2].lower() + "евич,", name[:-2] + name[-2].lower() + "евна")
    else:
        print("Не могу синтезировать отчество для " + name)


def synthesize_belong(name):
    if name[-1] == "ь":
        if name[-2] == "л":
            print(name + "ский")
        else:
            print(name[:-1] + "ский")
    elif name[-1] == "л":
        print(name + "ьский")
    elif name[-1] in {"а", "я", "и", "ы"}:
        print(name[:-1] + "инский")
    else:
        print(name[:-1] + "енский")


def synthesize_demonym(name):
    if name[-3:] in {"ово", "ево", "ино", "ено"}:
        if name[-4:] in {"рово"}:
            return name[:-1] + "чане"
        elif name.lower() == "косово":
            return "косовары"
        return name[:-1] + "цы"
    elif name[-3:] in {"тск"}:
        if name[-4:] in {"атск"}:
            return name[:-2] + "чане"
        return name[:-2] + "яне"
    elif name[-2:] in {"цк", "цы", "ец"}:
        if name[-4:] in {"пецк"}:
            return name[:-3] + "чане"
        if name[-3] == "л":
            return name[:-2] + "ьчане"
        return name[:-2] + "чане"
    elif name[-3:] in {"рск"}:
        if name.lower() in {"ангарск", "орск"}:
            return name[:-2] + "чане"
        elif name.lower() in {"курск"}:
            return "куряне"
        return name[:-2] + "цы"
    elif name[-3:] in {"йск", "тск"}:
        if name.lower() in {"бийск", "братск"}:
            return name[:-2] + "чане"
        return name[:-2] + "цы"
    elif name[-3:] in {"вск", "дск"}:
        if name.lower() in {"ульяновск"}:
            return name[:-2] + "цы"
        if name.lower() == "прокопьевск":
            return "прокопчане"
        elif name.lower() == "нижневартовск":
            return "вартовчане"
        return name[:-2] + "чане"
    elif name[-4:] in {"льск", "анск"}:
        if name.lower() == "архангельск":
            return "архангелогородцы"
        elif name.lower() == "тобольск":
            return "тоболяки"
        return name[:-2] + "чане"
    elif name.lower()[-4:] in {"омск"}:
        return name[:-2] + "ичи"
    elif name[-2:] in {"ск"}:
        if name.lower() == "волжск":
            return "волжане"
        elif name.lower() == "смоленск":
            return "смоляне"
        return name[:-2] + "цы"
    elif name.lower() in {"чили", "бурунди", "джибути", "зимбабве", "малави", "мали", "сан-томе", "сомали", "тувалу", "фиджи"}:
        return name[:-1] + "ийцы"
    elif name.lower() in {"науру", "палау", "перу"}:
        return name + "анцы"
    elif name.lower() in {"пуэрто-рико", "марокко"}:
        return name[:-1] + "анцы"
    elif name.lower() in {"вануату", "кирибати", "лесото", "сьерра-леоне", "филиппины"}:
        return name[:-1] + "цы"
    elif name.lower() == "сейшелы":
        return "сейшельцы"
    elif name.lower() == "кабо-верде":
        return "кабовердианцы"
    elif name.lower() == "таджикистан":
        return "таджики"
    elif name.lower() == "афганистан":
        return "афганцы"
    elif name.lower() == "узбекистан":
        return "узбеки"
    elif name.lower() == "буркина-фасо":
        return "буркинийцы"
    elif name.lower() == "багамские острова":
        return "багамцы"
    elif name.lower() == "гвинея-бисау":
        return "бисау-гвинейцы"
    elif name.lower() == "конго":
        return "конголезцы"
    elif name.lower() == "того":
        return "тоголезцы"
    elif name.lower() == "нидерланды":
        return "голландцы"
    elif name.lower() == "объединённые арабские эмираты":
        return "эмиратовцы"
    elif name.lower() == "маршалловы острова":
        return "маршалловцы"
    elif name.lower() == "соломоновы острова":
        return "соломоновцы"
    elif name.lower() == "соединённые штаты америки":
        return "американцы"
    elif name.lower() == "гаити":
        return "гаитяне"
    elif name.lower() == "мальдивы":
        return "мальдивиане"
    elif name.lower() == "монако":
        return "монегаски"
    elif name.lower() == "переславль-залесский":
        return "переславцы"
    elif name.lower() == "петропавловск-камчатский":
        return "петропавловцы"
    elif name.lower() == "великий устюг":
        return "устюжане"
    elif name.lower() == "гусь-хрустальный":
        return "гусевчане"
    elif name.lower() == "грозный":
        return "грозненцы"
    elif name.lower() == "энгельс":
        return "энгельситы"
    elif name[-1] in {"н", "ш", "й"}:
        return name + "цы"
    elif name[-2:] in {"ль"}:
        if name[-3:] in {"вль"}:
            return name[:-2] + "цы"
        elif name.lower() == "израиль":
            return name + "тяне"
        return name + "цы"
    elif name.lower() in {"пермь", "тверь", "тула"}:
        return name[:-1] + "яки"
    elif name.lower() in {"андорра", "антигуа", "аруба", "никарагуа", "самоа", "тонга"}:
        return name + "нцы"
    elif name.lower() in {"камбоджа", "шри-ланка", "мальта"}:
        return name[:-1] + "ийцы"
    elif name[-1:] in {"ь"}:
        if name.lower() == "назрань":
            return "назрановцы"
        elif name.lower() == "керчь":
            return "керчане"
        elif name.lower() == "сибирь":
            return "сибиряки"
        elif name.lower() == "беларусь":
            return "белорусы"
        return name[:-1] + "цы"
    elif name[-2:] in {"ки"}:
        return name[:-2] + "чане"
    elif name.lower() == "ямайка":
        return "ямайцы"
    elif name.lower() == "молдова":
        return "молдаване"
    elif name.lower() == "польша":
        return "поляки"
    elif name.lower() == "мьянма":
        return "бирманцы"
    elif name.lower() == "литва":
        return "литовцы"
    elif name[-3:] in {"ама", "ада"}:
        return name[:-1] + "цы"
    elif name[-2:] in {"ма"}:
        if name.lower() == "кинешма":
            return "кинешемцы"
        else:
            return name[:-1] + "ичи"
    elif name[-4:] in {"анда"}:
        return name[:-1] + "ийцы"
    elif name[-2:] in {"па", "ич"}:
        if name.lower() == "европа":
            return "европейцы"
        return name[:-1] + "чане"
    elif name[-2:] in {"да", "га"}:
        return name[:-2] + "жане"
    elif name[-3:] in {"ика"}:
        return name + "нцы"
    elif name[-2:] in {"ка"}:
        if name.lower() == "находка":
            return name[:-2] + "кинцы"
        return name[:-2] + "чане"
    elif name[-2:] in {"ла"}:
        if name.lower() == "кола":
            return name[:-1] + "яне"
        if name.lower() in {"ангола", "венесуэла", "гватемала"}:
            return name[:-1] + "ьцы"
        return name[:-1] + "инцы"
    elif name[-2:] in {"на", "ра", "ры"}:
        if name.lower() == "коломна":
            return name[:-2] + "чане"
        return name[:-1] + "цы"
    elif name.lower() == "комсомольск-на-амуре":
        return "комсомольчане"
    elif name.lower() == "ростов-на-дону":
        return "ростовчане"
    elif name.lower() == "яя":
        return "яйчане"
    elif name.lower() == "уфа":
        return "уфимцы"
    elif name.lower() == "великобритания":
        return "британцы"
    elif name.lower() == "германия":
        return "немцы"
    elif name.lower() == "франция":
        return "французы"
    elif name.lower() == "минеральные воды":
        return "минераловодцы"
    elif name.lower() == "набережные челны":
        return "челнинцы"
    elif name.lower() == "великий новгород":
        return "новгородцы"
    elif name.lower() == "нижний новгород":
        return "нижегородцы"
    elif name.lower() == "нижний тагил":
        return "тагильчане"
    elif name.lower() == "кипр":
        return "киприоты"
    elif name.lower() == "мадагаскар":
        return "малагасийцы"
    elif name.lower() == "кндр":
        return "северокорейцы"
    elif name.lower() == "старый оскол":
        return "старооскольцы"
    elif name.lower() == "восточный тимор":
        return "тиморцы"
    elif name.lower() == "сергиев посад":
        return "сергиевопосадцы"
    elif name.lower() == "кот-д'ивуар":
        return "ивуарийцы"
    elif name.lower() == "экваториальная гвинея":
        return "экваторогвинейцы"
    elif name.lower() == "южная осетия":
        return "югоосетины"
    elif name.lower() == "южный судан":
        return "суданцы"
    elif name.lower() == "южно-африканская республика":
        return "южноафриканцы"
    elif name.lower() == "центрально-африканская республика":
        return "центральноафриканцы"
    elif name.lower() == "туркмения":
        return "туркменистанцы"
    elif name.lower() == "армения":
        return "армяне"
    elif name.lower() == "дания":
        return "датчане"
    elif name.lower() == "финляндия":
        return "финны"
    elif name.lower() == "демократическая республика конго":
        return "конголезцы"
    elif name.lower() == "новая зеландия":
        return "новозеландцы"
    elif name.lower() == "папуа-новая гвинея":
        return "гвинейцы"
    elif name.lower() == "саудовская аравия":
        return "аравийцы"
    elif name.lower() == "италия":
        return "итальянцы"
    elif name.lower() == "монголия":
        return "монголы"
    elif name.lower() == "абхазия":
        return "абхазцы"
    elif name.lower() == "грузия":
        return "грузины"
    elif name.lower() == "киргизия":
        return "киргизстанцы"
    elif name.lower() == "норвегия":
        return "норвежцы"
    elif name.lower() == "россия":
        return "россияне"
    elif name.lower() == "сербия":
        return "сербы"
    elif name.lower() in {"кения", "танзания", "босния"}:
        return name[:-1] + "йцы"
    elif name[-2:] in {"ва"}:
        return name[:-1] + "ичи"
    elif name[-4:] in {"ыния"}:
        return name[:-2] + "ы"
    elif name[-3:] in {"ния"}:
        return name[:-2] + "цы"
    elif name.lower() in {"болгария", "венгрия"}:
        return name[:-2] + "ы"
    elif name.lower() in {"швейцария", "черногория"}:
        return name[:-2] + "цы"
    elif name[-6:] in {"ландия"}:
        return name[:-2] + "цы"
    elif name.lower() in {"бразилия", "португалия"}:
        return name[:-2] + "ьцы"
    elif name[-3:] in {"ция"}:
        if name.lower() == "швеция":
            return name[:-3] + "ды"
        return name[:-3] + "ки"
    elif name[-3:] in {"пия", "тия"}:
        return name[:-2] + "ы"
    elif name[-3:] in {"кия", "хия"}:
        return name[:-2] + "и"
    elif name[-2:] in {"ия", "ея"}:
        if name.lower() == "азия":
            return "азиаты"
        return name[:-1] + "йцы"
    elif name[-2:] in {"за"}:
        return name[:-1] + "енцы"
    elif name[-1] in {"э"}:
        return name + "нцы"
    elif name[-1] in vowels:
        return name[:-1] + "инцы"
    elif name[-1] in {"д", "р", "з", "ж", "с"}:
        if name == "энгельс":
            return name + "иты"
        return name + "цы"
    elif name[-1] in {"г"}:
        if name.lower() == "санкт-петербург":
            return "петербуржцы"
        elif name.lower() == "выборг":
            return "выборжане"
        return name[:-1] + "жцы"
    elif name[-2:] in {"ет"}:
        return name[:-2] + "тяне"
    elif name[-1] in {"т"}:
        if name.lower() == "сургут":
            return "сургутяне"
        elif name.lower() == "златоуст":
            return "златоустовцы"
        return name + "цы"
    elif name[-2:] in {"ый"}:
        return name[:-2] + "енцы"
    elif name[-1] in {"л"}:
        if name.lower() == "орёл":
            return "орловчане"
        elif name.lower() == "кызыл":
            return "кызылчане"
        return name + "ьцы"
    elif name[-1] in {"к"}:
        if name.lower() == "стерлитамак":
            return "стерлитамаковцы"
        elif name.lower() == "нальчик":
            return "нальчане"
        return name + "цы"
    elif name[-3:] in {"нам"}:
        return name + "цы"
    elif name[-1] in {"м"}:
        if name.lower() == "гаврилов-ям":
            return "гаврилов-ямцы"
        elif name.lower() == "крым":
            return "крымчане"
        return name + "ляне"
    elif name[-3:] in {"ров", "зов", "бов"}:
        return name + "чане"
    elif name[-1] == "в":
        if name.lower() == "псков":
            return "псковичи"
        return name + "цы"

    return ""

with open('input.txt', encoding="utf-8") as f:
    lines = f.readlines()
f.close()

f = open('output.txt', 'w', encoding="utf-8")
ctr = 0
ci = []
for item in lines:
    mas = item.split()
    syn = synthesize_demonym(mas[0]).lower()
    syn = syn.replace("-", "")
    if syn != mas[1]:
        if syn != "":
            f.write("%s\t" % mas[0])
            f.write("%s\t" % mas[-1])
            f.write("%s\n" % syn)
    else:
        ctr += 1
f.write("%d\t" % ctr)
f.close()
