from nltk.corpus import stopwords
import string


stop_words = stopwords.words('english')
for word in stopwords.words('english'):
    stop_words.append(word.upper())


numbers = ['(', ')','–', '—', ';', ':', '[', ']', ',', '»', '«', 'January', 'February', 'March', 'April', 'May', 'June', 'July',
           'August', 'September', 'October', 'November', 'December', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'year', 'month', 'months', 'of', 'p',
           '/p', 'lt', 'li', '/li', 'gt', '/ul', 'amp', 'nbsp', 'ul', '/strong']


def get_vacants_en(l):
    head_hunter = False
    for line in l:
        if "Resume updated" in line:
            head_hunter = True
            break
    if (head_hunter):
        key_words = ["Desired position and salary","Work experience","Education","Key skills","Languages", "Skills", "Further information","Опыт вождения", "About me","Recommendations"]
        cv_summary = {"education": "", "position": "",
                      "skills": "", "experience": "", "language": "", "about": "", "other": ""}
        counter = -1
        while counter < len(l) - 1:
            counter += 1
            if counter == len(l):
                break
            if "Desired position and salary" in l[counter]:
                counter += 1
                while('•' not in l[counter]):
                    cv_summary["position"] += " " + l[counter]
                    counter += 1
                while ("•" in l[counter]):
                    cv_summary["position"] += " " + l[counter]
                    counter += 1

            if counter == len(l):
                break
            if "Work experience" in l[counter]:
                cv_summary["experience"] = ""
                counter += 1
                while counter < len(l):
                    if ("Resume updated" not in l[counter]):
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
            if "Education" in l[counter]:
                cv_summary["education"] = ""
                counter += 1
                while counter < len(l):
                    if ("Resume updated" not in l[counter]):
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
            if "Languages" in l[counter]:
                cv_summary["language"] = ""
                counter += 1
                while counter < len(l):
                    if ("Resume updated" not in l[counter]):
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
            if "Skills" in l[counter]:
                cv_summary["skills"] = ""
                counter += 1
                while counter < len(l):
                    if ("Resume updated" not in l[counter]):
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
            if "Recommendations" in l[counter]:
                cv_summary["reference"] = ""
                counter += 1
                while counter < len(l):
                    if ("Resume updated" not in l[counter]):
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
            if "About me" in l[counter]:
                cv_summary["about"] = ""
                counter += 1
                while counter < len(l):
                    if ("Resume updated" not in l[counter]):
                        cv_summary["about"] += " " + l[counter]
                    counter += 1

        for key in cv_summary:
            cv_summary[key] = cv_summary[key].replace(',', ' ').replace(')', '').replace('(', '').split()

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

            "experience": ["Work Experience", "Activities", "Work History", "Affiliations"],

            "language": ["Languages", "Knowledge of Languages", "Language"],

            "about": ["About me", "Additional information", "Additional information", "Awards","Achievements", "Accomplishment"],
            "reference": ["Recommendations", "References","Reference", "Referees"],
            "other": ["interests", "hobby"]
        }

        cv_summary = {"education": "", "position": "",
                      "skills": "", "experience": "", "language": "", "about": "", "reference": "", "other":""}

        counter_l = -1
        while (counter_l < len(l) - 1):
            counter_l += 1
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
            
            cv_summary[key] = [
                ab for ab in cv_summary[key] if not ab in numbers]

    return cv_summary
