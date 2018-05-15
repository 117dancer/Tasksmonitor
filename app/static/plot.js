var myChart = echarts.init(document.getElementById('main'));
var option = {
            title: {
                text: "下发任务统计"
            },
            tooltip: {},
            legend: {
                data:['static']
            },
            xAxis: {
                data: []
            },
            yAxis: {},
            series: [{
                name: 'number',
                type: 'bar',
                data: []
            }]
        };
myChart.showLoading();
myChart.setOption(option);

$.ajax({
                    type: 'POST',
                    async: true ,
                    url:"/sendTask",
                    data:null,
                    contentType: 'application/json; charset=UTF-8',
                    success:function(data){
                        alert("sucsess to get the reback data!");
                        myChart.hideLoading();
                        myChart.setOption({
                        xAxis: {
                           data: data.categories
                           },
                           series: [{
            // 根据名字对应到相应的系列
                            name: '销量',
                            data: data.data1
                            }]
                        })},
                    error:function(errMessge){
                    alert("get the back data failure!");
                    }
                });
