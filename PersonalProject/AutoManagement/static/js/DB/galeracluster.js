window.onload = function(){
    var oInput = document.getElementById('id_hostip');
    var oValidation1 = document.getElementById('validation1');
    var oValidation2 = document.getElementById('validation2');
    var oValidation3 = document.getElementById('validation3');
    var oValidation = [oValidation1, oValidation2, oValidation3];


    function checkIP() {
        var entered_ip1 = document.getElementById('id_hostip1').value;
        var entered_ip2 = document.getElementById('id_hostip2').value;
        var entered_ip3 = document.getElementById('id_hostip3').value;
        var entered_ip = [entered_ip1, entered_ip2, entered_ip3];
        var iLen2 = entered_ip.length;

        for(var i=0;i<iLen2;i++){
            if(entered_ip[i]){
                var exp= /^(([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-8][0-9]|9[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/g;
                var reg = entered_ip[i].match(exp);
                if(reg==null){
                    oValidation[i].innerHTML = "输入ip有误,请重新输入";
           }
                else{
                oValidation[i].innerHTML = "";
            }
       }
       else {
            oValidation[i].innerHTML = "请输入ip地址";
       }
        }
   }
   setInterval(checkIP, 1000);
};