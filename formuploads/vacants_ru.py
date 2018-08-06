from nltk.corpus import stopwords
import string


def stop_words_kk():
    stop_words_kk = []
    with open('./stop.txt', 'rb') as f:
        lines = f.readlines()
        stop_words_kk.append(lines[0])
    return stop_words_kk


stop_words = stopwords.words('russian')
stop_words += stop_words_kk()
for word in stopwords.words('russian'):
    stop_words.append(word.upper())
stop_words += stopwords.words('english')
for word in stopwords.words('english'):
    stop_words.append(word.upper())


numbers = ['(', ')', '—', ';', ':', '[', ']', ',', '»', '«', 'Январь', 'Февраль',
           'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
           'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'года', 'месяцев', 'of', 'p',
           '/p', 'lt', 'li', '/li', 'gt', '/ul', 'amp', 'nbsp', 'ul', '/strong']


def get_vacants_ru(l):
    head_hunter = False
    for line in l:
        if "Резюме обновлено" in line:
            head_hunter = True
            break

    key_words = ["Желаемая должность и зарплата","Опыт работы","Образование","Ключевые навыки","Знание языков","Навыки","Опыт вождения","Дополнительная информация", "Обо мне","Рекомендации" ]

    if (head_hunter):
        cv_summary = {"education": "", "position": "",
                      "skills": "", "experience": "", "language": "", "about": "", "reference": "", "other": ""}
        counter = -1
        while counter < len(l) - 1:
            counter += 1
            if counter == len(l):
                break
            if "Желаемая должность и зарплата" in l[counter]:
                counter += 1
                while('•' not in l[counter]):
                    cv_summary["position"] += " " + l[counter]
                    counter += 1
                while ("•" in l[counter]):
                    cv_summary["position"] += " " + l[counter]
                    counter += 1

            if counter == len(l):
                break
            if "Опыт работы" in l[counter]:
                cv_summary["experience"] = ""
                counter += 1
                while counter < len(l):
                    if ("Резюме обновлено" not in l[counter]):
                        ok = False
                        for k in key_words:
                            if (k in l[counter]):
                                ok = True
                                break
                        if ok:
                            break
                        cv_summary["experience"] += " " + l[counter]
                    counter += 1

            if counter == len(l):
                break
            if "Образование" in l[counter]:
                cv_summary["education"] = ""
                counter += 1
                while counter < len(l):
                    if ("Резюме обновлено" not in l[counter]):
                        ok = False
                        for k in key_words:
                            if (k in l[counter]):
                                ok = True
                                break
                        if ok:
                            break
                        cv_summary["education"] += " " + l[counter]
                    counter += 1

            if counter == len(l):
                break
            if "Знание языков" in l[counter]:
                cv_summary["language"] = ""
                counter += 1
                while counter < len(l):
                    if ("Резюме обновлено" not in l[counter]):
                        ok = False
                        for k in key_words:
                            if (k in l[counter]):
                                ok = True
                                break
                        if ok:
                            break
                        cv_summary["language"] += " " + l[counter]
                    counter += 1

            if counter == len(l):
                break
            if "Навыки" in l[counter]:
                cv_summary["skills"] = ""
                counter += 1
                while counter < len(l) - 1:
                    if ("Резюме обновлено" not in l[counter]):
                        ok = False
                        for k in key_words:
                            if (k in l[counter]):
                                ok = True
                                break
                        if ok:
                            break
                        cv_summary["skills"] += " " + l[counter]
                    counter += 1
                    

            if counter == len(l):
                break
            if "Опыт вождения" in l[counter]:
                cv_summary["other"] = ""
                counter += 1
                while counter < len(l):
                    if ("Резюме обновлено" not in l[counter]):    
                        ok = False
                        for k in key_words:
                            if (k in l[counter]):
                                ok = True
                                break
                        if ok:
                            break
                        cv_summary["other"] += " " + l[counter]
                    counter += 1

            if counter == len(l):
                break
            if "Рекомендации" in l[counter]:
                cv_summary["reference"] = ""
                counter += 1
                while counter < len(l):
                    if ("Резюме обновлено" not in l[counter]):
                        ok = False
                        for k in key_words:
                            if (k in l[counter]):
                                ok = True
                                break
                        if ok:
                            break
                        cv_summary["reference"] += " " + l[counter]
                    counter += 1
                                    
            if counter == len(l):
                break
            if "Обо мне" in l[counter]:
                cv_summary["about"] = ""
                counter += 1
                while counter < len(l):
                    if ("Резюме обновлено" not in l[counter]):
                        cv_summary["about"] += " " + l[counter]
                    counter += 1

        for key in cv_summary:
            cv_summary[key] = cv_summary[key].replace(',', ' ').replace(')', '').replace('(', '').split()

            cv_summary[key] = [a for a in cv_summary[key]
                               if not a in stop_words and not a in string.punctuation]
            cv_summary[key] = [ab for ab in cv_summary[key]
                               if not ab in stop_words_k and not ab in numbers]

        if 'position' in cv_summary:
            key_pos = [x for x in cv_summary["position"] if x != "•"]
            cv_summary['position'] = key_pos

    else:

        key_words = {
            "education": ["Образование", "Квалификация",
                          "Специальность"],

            "position": ["Цель", "В поиске","Желаемая должность и зарплата", "Желаемая должность"],

            "skills": ["Навыки",
                       "Компьютерная грамотность"],

            "experience": ["Опыт работы", "трудовая деятельность","Стаж работы", "Профессиональный опыт"],

            "language": ["Языки", "Знание Языков", "Язык ", "Владение языками"],

            "about": ["Обо мне", "Дополнительная информация", "Дополнительные сведения", "Качества", "Достижения", "Сведения о себе"],
            "reference": ["Рекомендации"],
            "other": ["Хобби", "Водительское удостоверение", "Интересы"],
        }

        cv_summary = {"education": "", "position": "",
                      "skills": "", "experience": "", "language": "", "about": "", "reference": "", "other": ""}

        counter_l = -1
        while (counter_l < len(l) - 1):
            counter_l += 1
            print(l[counter_l])
            for key in key_words:
                for word in key_words[key]:
                    if counter_l < len(l) and word.lower() in l[counter_l].lower():
    
                        check = True
                        cv_summary[key] += " " + l[counter_l].lower().replace(word.lower(), '')

                        counter_l += 1
                        while (check):
                            if (counter_l > len(l) - 1):
                                check = False
                                break
                            for key_1 in key_words:
                                if key_1 != key:
                                    for word_1 in key_words[key_1]:
                                        if word_1.lower() in l[counter_l].lower():
                                            check = False
                                            counter_l -= 1
                                            break
                                    if check == False:
                                        break
                            if not check:
                                break
                            else:
                                cv_summary[key] += " " + l[counter_l]
                                counter_l += 1

        for key in cv_summary:
            cv_summary[key] = cv_summary[key].replace(',', ' ').replace(')', '').replace('(', '').split()
            cv_summary[key] = [a for a in cv_summary[key]
                               if not a in stop_words and not a in string.punctuation]
            cv_summary[key] = [ab for ab in cv_summary[key]
                               if not ab in stop_words_k and not ab in numbers]

        if 'position' in cv_summary:
            key_pos = [x for x in cv_summary["position"] if x != "•"]
            cv_summary['position'] = key_pos

    return cv_summary
