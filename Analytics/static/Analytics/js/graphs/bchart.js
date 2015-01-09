function drawChart() {

var data = new google.visualization.DataTable();
data.addColumn('string', 'Tping');
data.addColumn('number', 'Slices');
data.addRows({{ b_datatable|safe }});

// Set chart options
var options = {'title':'Activities on apparels in your selected price range',
               'width':600,
               'height':500,
                'backgroundColor': '#dddddd'};

// Instantiate and draw our chart, passing in some options.
var chart = new google.visualization.PieChart(document.getElementById('b_chartpie'));
chart.draw(data, options);
}
<script type="text/javascript">
google.load("visualization", "1", {packages:["geochart"]});
google.setOnLoadCallback(drawRegionsMap);

function drawRegionsMap() {

var data = google.visualization.arrayToDataTable({{ country_datatable|safe }});
var options = {};
var chart = new google.visualization.GeoChart(document.getElementById('country_div'));
chart.draw(data, options);
}
</script>