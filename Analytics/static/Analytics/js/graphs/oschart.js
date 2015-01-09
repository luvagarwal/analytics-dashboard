function drawChart1() {

var data = new google.visualization.DataTable();
data.addColumn('string', 'Tping');
data.addColumn('number', 'Slices');
data.addRows({{ o_datatable|safe }});

var options = {'title':'Activities on apparels in your selected price range',
               'width':600,
               'height':500,
                'backgroundColor': '#dddddd'};

var chart = new google.visualization.PieChart(document.getElementById('o_chartpie'));
chart.draw(data, options);
}
