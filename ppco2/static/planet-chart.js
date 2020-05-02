$.ajax({
  url: $("#planet_chart_container").attr("data-url"),
  dataType: "json",
  success: function (data) {
    Highcharts.chart("planet_chart_container", data);
  },
});
