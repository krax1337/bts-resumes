var i_ed = 0;
var i_ex = 0;
var i_la = 0;

function increment_lan() {
    i_la += 1; /* function for automatic increament of feild's "Name" attribute*/
}

function increment_edu() {
    i_ed += 1; /* function for automatic increament of feild's "Name" attribute*/
}

function increment_exp() {
    i_ex += 1; /* function for automatic increament of feild's "Name" attribute*/
}

function dec_edu() {
    i_ed -= 1; /* function for automatic increament of feild's "Name" attribute*/
}

function dec_exp() {
    i_ex -= 1; /* function for automatic increament of feild's "Name" attribute*/
}

var edu = 0;
var exp = 0;

function new_education() {
    var r = document.createElement('div');
    edu += 1;
    r.setAttribute("id", 'edu' + edu);

    r.setAttribute("class", 'element_ed');
    increment_edu();

    var y = document.createElement("INPUT");
    y.setAttribute("type", "text");
    y.setAttribute("placeholder", "Название учебного заведения");
    y.setAttribute("class", "form-control");
    y.setAttribute("style", " text-align:center");
    y.setAttribute("name", "education_name" + i_ed);
    y.setAttribute("id", i_ed);
    y.required = true;


    var y_2 = document.createElement("INPUT");
    y_2.setAttribute("type", "text");
    y_2.setAttribute("placeholder", "Степень");
    y_2.setAttribute("class", "form-control");
    y_2.setAttribute("style", " text-align:center");
    y_2.setAttribute("name", "education_degree" + i_ed);
    y_2.setAttribute("id", i_ed);

    var y_3 = document.createElement("INPUT");
    y_3.setAttribute("type", "text");
    y_3.setAttribute("placeholder", "Дата начала обучения");
    y_3.setAttribute("class", "form-control");
    y_3.setAttribute("style", " text-align:center");
    y_3.setAttribute("name", "education_start_date" + i_ed);
    y_3.setAttribute("id", i_ed);

    var y_4 = document.createElement("INPUT");
    y_4.setAttribute("type", "text");
    y_4.setAttribute("placeholder", "Дата конца обучения");
    y_4.setAttribute("class", "form-control");
    y_4.setAttribute("style", " text-align:center");
    y_4.setAttribute("name", "education_end_date" + i_ed);
    y_4.setAttribute("id", i_ed);

    var y_5 = document.createElement("TEXTAREA");
    y_5.setAttribute("type", "text");
    y_5.setAttribute("placeholder", "Описание");
    y_5.setAttribute("class", "form-control");
    y_5.setAttribute("style", " text-align:center");
    y_5.setAttribute("name", "education_description" + i_ed);
    y_5.setAttribute("id", i_ed);


    r.appendChild(y);
    r.appendChild(y_2);
    r.appendChild(y_3);
    r.appendChild(y_4);
    r.appendChild(y_5);

    document.getElementById("i_ed").value = i_ed;
    document.getElementById("educations").appendChild(r);
}


function new_experinece() {
    var r = document.createElement('div');
    exp += 1;
    r.setAttribute("id", 'exp' + exp);

    r.setAttribute("class", 'element_ed');
    increment_exp();

    var y = document.createElement("INPUT");
    y.setAttribute("type", "text");
    y.setAttribute("placeholder", "Название компании");
    y.setAttribute("class", "form-control");
    y.setAttribute("style", " text-align:center");
    y.setAttribute("name", "experience_name" + i_ex);
    y.setAttribute("id", i_ex);
    y.required = true;


    var y_2 = document.createElement("INPUT");
    y_2.setAttribute("type", "text");
    y_2.setAttribute("placeholder", "Должность");
    y_2.setAttribute("class", "form-control");
    y_2.setAttribute("style", " text-align:center");
    y_2.setAttribute("name", "experience_designation" + i_ex);
    y_2.setAttribute("id", i_ex);

    var y_3 = document.createElement("INPUT");
    y_3.setAttribute("type", "text");
    y_3.setAttribute("placeholder", "Начало работы");
    y_3.setAttribute("class", "form-control");
    y_3.setAttribute("style", " text-align:center");
    y_3.setAttribute("name", "experience_start_date" + i_ex);
    y_3.setAttribute("id", i_ex);

    var y_4 = document.createElement("INPUT");
    y_4.setAttribute("type", "text");
    y_4.setAttribute("placeholder", "Конец работы");
    y_4.setAttribute("class", "form-control");
    y_4.setAttribute("style", " text-align:center");
    y_4.setAttribute("name", "experience_end_date" + i_ex);
    y_4.setAttribute("id", i_ex);

    var y_5 = document.createElement("TEXTAREA");
    y_5.setAttribute("type", "text");
    y_5.setAttribute("placeholder", "Описание");
    y_5.setAttribute("class", "form-control");
    y_5.setAttribute("style", " text-align:center");
    y_5.setAttribute("name", "experience_description" + i_ex);
    y_5.setAttribute("id", i_ex);


    r.appendChild(y);
    r.appendChild(y_2);
    r.appendChild(y_3);
    r.appendChild(y_4);
    r.appendChild(y_5);

    document.getElementById("i_ex").value = i_ex;
    document.getElementById("experiences").appendChild(r);
}


function new_experinece() {
    var r = document.createElement('div');
    exp += 1;
    r.setAttribute("id", 'exp' + exp);

    r.setAttribute("class", 'element_ed');
    increment_exp();

    var y = document.createElement("INPUT");
    y.setAttribute("type", "text");
    y.setAttribute("placeholder", "Название компании");
    y.setAttribute("class", "form-control");
    y.setAttribute("style", " text-align:center");
    y.setAttribute("name", "experience_name" + i_ex);
    y.setAttribute("id", i_ex);
    y.required = true;


    var y_2 = document.createElement("INPUT");
    y_2.setAttribute("type", "text");
    y_2.setAttribute("placeholder", "Должность");
    y_2.setAttribute("class", "form-control");
    y_2.setAttribute("style", " text-align:center");
    y_2.setAttribute("name", "experience_designation" + i_ex);
    y_2.setAttribute("id", i_ex);

    var y_3 = document.createElement("INPUT");
    y_3.setAttribute("type", "text");
    y_3.setAttribute("placeholder", "Начало работы");
    y_3.setAttribute("class", "form-control");
    y_3.setAttribute("style", " text-align:center");
    y_3.setAttribute("name", "experience_start_date" + i_ex);
    y_3.setAttribute("id", i_ex);

    var y_4 = document.createElement("INPUT");
    y_4.setAttribute("type", "text");
    y_4.setAttribute("placeholder", "Конец работы");
    y_4.setAttribute("class", "form-control");
    y_4.setAttribute("style", " text-align:center");
    y_4.setAttribute("name", "experience_end_date" + i_ex);
    y_4.setAttribute("id", i_ex);

    var y_5 = document.createElement("TEXTAREA");
    y_5.setAttribute("type", "text");
    y_5.setAttribute("placeholder", "Описание");
    y_5.setAttribute("class", "form-control");
    y_5.setAttribute("style", " text-align:center");
    y_5.setAttribute("name", "experience_description" + i_ex);
    y_5.setAttribute("id", i_ex);


    r.appendChild(y);
    r.appendChild(y_2);
    r.appendChild(y_3);
    r.appendChild(y_4);
    r.appendChild(y_5);

    document.getElementById("i_ex").value = i_ex;
    document.getElementById("experiences").appendChild(r);
}

function removeElement_edu() {
    document.getElementById("i_ed").value = i_ed - 1;
    i_ed -= 1;
    elem = document.getElementById("edu" + edu);
    elem.remove();
    edu -= 1;
}

function removeElement_exp() {
    document.getElementById("i_ex").value = i_ex - 1;
    i_ex -= 1;
    elem = document.getElementById("exp" + exp);
    elem.remove();
    exp -= 1;
}