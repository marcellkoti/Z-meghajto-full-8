var kiir = "";

tomb = ["kep1.jfif", "kep2.jfif" ,"kep3.jfif"];
leiras = ["kep1 szövege","kep2 szövege","ez pedig a kep3 szövege"];
document.getElementById("kepleiras").innerHTML = leiras[0];
document.getElementById("kep").src = "pic/"+tomb[0];
function gomb(){
    for (let index = 0; index < tomb.length; index++) {
        kiir +=tomb[index]+"<br>"  ;     
    }
document.getElementById("szoveg").innerHTML = kiir;
}
let szamlalo=0;
let szam = 0;

function minusz(){
    szamlalo--;
    szam = szamlalo%tomb.length;
    document.getElementById("kep").src = "pic/"+tomb[szam];
    document.getElementById("kepleiras").innerHTML = leiras[szam];
}

function plusz(){
    szamlalo++;
    szam = szamlalo%tomb.length;
    document.getElementById("kep").src = "pic/"+tomb[szam]
    document.getElementById("kepleiras").innerHTML = leiras[szam];
    
}


