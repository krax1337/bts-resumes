from nltk.corpus import stopwords
import string


stop_words = stopwords.words('english')
for word in stopwords.words('english'):
    stop_words.append(word.upper())


numbers = ['(', ')', '—', ';', ':', '[', ']', ',', '»', '«', 'January', 'February', 'March', 'April', 'May', 'June', 'July',
           'August', 'September', 'October', 'November', 'December', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'year', 'month', 'months', 'of', 'p',
           '/p', 'lt', 'li', '/li', 'gt', '/ul', 'amp', 'nbsp', 'ul', '/strong']


def get_vacants_en(l):
    head_hunter = False
    for line in l:
        if "Resume updated" in line:
            head_hunter = True
            break
    if (head_hunter):
        cv_summary = {}
        counter = -1
        print(l)
        for line in l:
            counter += 1

            if "Desired position and salary" in line:
                cv_summary["position"] = l[counter + 1]
                cv_summary["position"] += " " + l[counter + 2]
                counter_l = counter + 3

                while ("•" in l[counter_l]):
                    cv_summary["position"] += " " + l[counter_l]
                    counter_l += 1

            if "Work experience" in line:
                cv_summary["experience"] = ""
                counter_l = counter + 1

                while True:
                    if ("Resume updated" not in l[counter_l]):
                        if ("Education" in l[counter_l]):
                            break
                        cv_summary["experience"] += " " + l[counter_l]

                    counter_l += 1

            if "Education" in line:
                cv_summary["education"] = ""
                counter_l = counter + 1

                while True:
                    if ("Resume updated" not in l[counter_l]):
                        if ("Key skills" in l[counter_l]):
                            break
                        cv_summary["education"] += " " + l[counter_l]

                    counter_l += 1

            if "Languages" in line:
                cv_summary["language"] = ""
                counter_l = counter + 1

                while True:
                    if ("Resume updated" not in l[counter_l]):
                        if ("Skills" in l[counter_l]):
                            break
                        cv_summary["language"] += " " + l[counter_l]

                    counter_l += 1

            if "Skills" in line:
                cv_summary["skills"] = ""
                counter_l = counter + 1

                while True:
                    cv_summary["skills"] += " " + l[counter_l]
                    counter_l += 1
                    if ("Опыт вождения" or "Further information" in l[counter_l]):
                        break

            if "About me" in line:
                cv_summary["about"] = ""
                counter_l = counter + 1

                while True:
                    if (counter_l >= len(l)-1):
                        break
                    if ("Resume updated" not in l[counter_l]):
                        cv_summary["about"] += " " + l[counter_l]

                    counter_l += 1

        for key in cv_summary:
            cv_summary[key] = cv_summary[key].replace(
                '.', ' ').replace(',', ' ').split()

            cv_summary[key] = [a for a in cv_summary[key]
                               if not a in stop_words and not a in string.punctuation]
            cv_summary[key] = [
                ab for ab in cv_summary[key] if not ab in numbers]

        if 'position' in cv_summary:
            key_pos = [x for x in cv_summary["position"] if x != "•"]
            cv_summary['position'] = key_pos

    else:

        key_words = {
            "education": ["Education", "Qualification",
                          "Specialty"],

            "position": ["Goal"],

            "skills": ["Skills", "Additional information",
                       "Computer literacy", "Qualities"],

            "experience": ["Work Experience"],

            "language": ["Languages", "Knowledge of Languages", "Language"],

            "about": ["About me", "Additional information", "Additional information"],
        }

        cv_summary = {"education": "", "position": "",
                      "skills": "", "experience": "", "language": "", "about": ""}

        counter_l = -1
        while (counter_l < len(l) - 1):
            counter_l += 1
            for key in key_words:
                for word in key_words[key]:
                    if word in l[counter_l] or word.lower() in l[counter_l].lower() or word.upper() in l[counter_l].upper():
                        check = True
                        counter_2 = counter_l + 1
                        while (check):
                            if (counter_2 >= len(l) - 1):
                                check = False
                                counter_2 = 0
                                break
                            else:
                                cv_summary[key] += " " + l[counter_2]
                                counter_2 += 1

                            for key_1 in key_words:
                                if key_1 != key:
                                    for word_1 in key_words[key_1]:
                                        if word_1.lower() in l[counter_2].lower():
                                            check = False
                                            counter_l = counter_2 - 1
                                            counter_2 = 0
                                            break
                                    if check == False:
                                        break

        for key in cv_summary:
            cv_summary[key] = cv_summary[key].replace(
                '.', ' ').replace(',', ' ').split()

            cv_summary[key] = [a for a in cv_summary[key]
                               if not a in stop_words and not a in string.punctuation]
            cv_summary[key] = [
                ab for ab in cv_summary[key] if not ab in numbers]

    return cv_summary
