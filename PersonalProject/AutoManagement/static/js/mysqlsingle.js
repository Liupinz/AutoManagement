window.onload = function(){
    var oInput = document.getElementById('id_hostip');
    var oValidation = document.getElementById('validation');
    // oInput.onclick = checkIP;

    function checkIP() {
        var entered_ip = document.getElementById('id_hostip').value;
        if(entered_ip){
            var exp= /^(([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/g;
            var reg = entered_ip.match(exp);
            if(reg==null){
                oValidation.innerHTML = "输入ip有误,请重新输入";
           }
           else{
                oValidation.innerHTML = "";
            }
       }
       else {
            oValidation.innerHTML = "请输入ip地址";
        }
   }
   setInterval(checkIP, 1000);
}