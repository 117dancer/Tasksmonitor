function killTask()
{
                $.ajax({
                    type: 'POST',
                    async: true ,
                    url:"/kill",
                    data:null,
                    contentType: 'application/json; charset=UTF-8',
                    success:function(data){
                        alert("congratulations! you have sucessfully kill all the task!");
                    },
                    error:function(errMessge){
                    alert("error!");
                    }
                });

}
//
//function formSubmit(){
////var data=$("#inNumber").val();
//document.getElementById("#formid").submit();
//return true;
//}
