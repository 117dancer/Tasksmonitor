function formSubmit(){
var data=$("#inNumber").val();
alert(data);
$.ajax({
                    type: 'POST',
                    async: true ,
                    url:"/task",
                    data:JSON.stringify(data),
                    contentType: 'application/json; charset=UTF-8',
                    success:function(data){
                        alert("sucsess to get the reback data!");
                    },
                    error:function(errMessge){
                    alert("get the back data failure!");
                    }
                });

}


