document.addEventListener("DOMContentLoaded", function(){
    tdClick();
    document.getElementById("pStart").addEventListener("click", function(){ reset(); turn = 0; document.getElementById("res").innerHTML = "your turn (O)";});
    document.getElementById("rStart").addEventListener("click", function(){ reset(); turn = 1; requestData(); document.getElementById("res").innerHTML = "your turn (O)";});

   if(turn == 1){
    requestData();
   }
    
});

var tris = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
]

var turn = -1;
var players=["O", "X"]
var ch = "";

function changeTurn(){
    if(turn == 0){
        turn = 1;

    }else{
        turn = 0;
    }
}

function isFree(val){
    if(val != 'x' && val != 'o'){
        return true;
    }

    return false;
}

function tdClick(){
    var tds = document.getElementsByTagName("td");
    
    for(i=0; i < tds.length; i++){
        tds[i].addEventListener("click", function(e){
            var id = e.target.id.split("-")[1];
            var found = false;

            if(turn == 0){
                for(j=0; j < tris.length; j++){
                    for(n=0; n < tris[j].length; n++){
                        if(tris[j][n] == id.toString()){
                            tris[j][n] = players[turn].toLowerCase();
                            found = true;
                            e.target.textContent = players[turn];
                            changeTurn();
                            break;
                        }
                    }
                }
            }else{

                for(j=0; j < tris.length; j++){
                    for(n=0; n < tris[j].length; n++){
                        if(tris[j][n] == ch){
                            tris[j][n] = players[turn].toLowerCase();
                            found = true;
                            e.target.textContent = players[turn];
                            changeTurn();
                            break;
                        }
                    }
                }
            }

            if(anyWon(tris) != 'n'){
                
                if(anyWon(tris) == "DRAW"){
                    document.getElementById("res").innerHTML = "DRAW";
                }else if(document.getElementById("res").innerHTML = "winner : x"){
                    finished(tris);
                    document.getElementById("res").innerHTML = "you lost";
                    document.getElementById("res").style.color = "rgb(248, 86, 186)";
                }else{
                    finished(tris);
                    document.getElementById("res").innerHTML = "you won";
                }
                
            }else{
                if(turn == 1){
                    requestData();
                }
            }
           
            
            


        });
    }
}

function reset(){
    var x = 0;
    for(i=0; i < tris.length; i++){
        for(j=0; j < tris.length; j++){
            x++;
            tris[i][j] = x.toString();
        }
    }

    var td = document.getElementsByTagName("td");
    for(i=0; i < td.length; i++){
        td[i].textContent = "";
    }

    document.getElementById("res").style.color = "rgb(51, 238, 238)";
    document.getElementById("res").innerHTML = "choose to continue";
}

function anyWon(tris){
    if(winnerCheck(tris) == 'd'){
        return "DRAW";
    }else if(winnerCheck(tris) == 'x' || winnerCheck(tris) == 'o'){
        return "winner : "+winnerCheck(tris).toUpperCase();
    }else{
        return "n";
    }
}

function finished(tris){
    for(i=0; i < tris.length; i++){
        for(j=0; j < tris[i].length; j++){
            if(isFree(tris)){
                tris[i][j] = "x";
            }
        }
    }
}



function requestData(){
    var data = {
        "tris": tris
    }

    var choice;
  
    // loader starts
    document.getElementById("loader").style.display  = "block";
    document.getElementById("main").style.filter = "blur(10px)";
    $.ajax({
        type: "POST",
        url: "/process",
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: 'json',
        success: function(result) {
            robotTurn(result);
          } 
      });

   
}

function winnerCheck(tris){

    // horrizontal and vertical check
    
    for(i=0; i < tris.length; i++){
        if(tris[i][0] == tris[i][1] && tris[i][0] == tris[i][2]){
            return tris[i][1];
        }

        if(tris[0][i] == tris[1][i] && tris[0][i] == tris[2][i]){
            return tris[1][i];
        }
    }

    if((tris[0][0] == tris[1][1] && tris[1][1] == tris[2][2]) || (tris[0][2] == tris[1][1] && tris[1][1] == tris[2][0])){
        return tris[1][1];
    }

    // draw check
    var draw = true;

    for(i=0; i  < tris.length; i++){
        for(j=0; j < tris[i].length; j++){
            if(isFree(tris[i][j])){
                draw = false;
                break;
            }
        }
    }

    if(draw){
        return "d";
    }else{
        return 'n';
    }

}

function robotTurn(r){

    // loader stops
    document.getElementById("loader").style.display  = "none";
    document.getElementById("main").style.filter = "blur(0px)";
    ch = r;
    var id = "l-"+r;

    document.getElementById(id).click();

}

