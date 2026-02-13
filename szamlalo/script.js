function paros(){
    var szam = parseInt(document.getElementById('szam').value);
    var dontes = "Páratlan";
    if (szam%2==0){
        dontes = "Páros";
    }
    if (szam == 0){
        dontes = "Ez a nulla szám";
    }
    alert(dontes);
}
function prim(){
    var szam = parseInt(document.getElementById('szam').value);
    var dontes = "PRÍM";
    var osztok;
    switch (szam) {
        case 1:
            dontes = "nem prím";
            break
            case 2:
            dontes = "prím";
            break;    
        default:
            gyok = Math.floor(Math.sqrt(szam));
            for (let index = 2; index <= gyok; index++) {
                if (szam%index==0){
                    osztok = index;
                    dontes = "NEM prím, mert osztója a pl: "+osztok;

                }
            }
            break;
    }
    alert(dontes);
}
function tokeletes(){
    var szam = parseInt(document.getElementById('szam').value);
    osztok = [];
    osztoindex=0;
    dontes = "Nem tokéletes szám";
    for (let index = 1; index <= szam/2; index++) {
        if (szam%index==0){
            osztok[osztoindex]=index;
            osztoindex++;
        }         
    }
    var osszeg=0;
    for (let index = 0; index < osztok.length; index++) {
        osszeg = osszeg+osztok[index];
        
    }
    if (osszeg == szam){
        dontes ="Tokéletes szám";
    }
    alert(dontes);
}


