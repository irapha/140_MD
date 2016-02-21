function render_graph(data, waketime, bedtime) {
  var margin = {top: 20, right: 20, bottom: 30, left: 40},
      width = 960 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom;

  var x = d3.scale.linear().domain([0, 24*60]).range([margin.left, width]),
      y = d3.scale.linear().domain([d3.max(data, function(d) { return d[1]; }), 0]).range([margin.top, height]);

  var xAxis = d3.svg.axis().scale(x).orient("bottom")
        .ticks(15)
        .tickFormat(function(d) { return (d / 60).toPrecision(2); }),
      yAxis = d3.svg.axis().scale(y).orient("left");

  var svg = d3.select("#graph")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom);

  svg.append("g")
        .attr("class", "axis")
        .attr("transform", "translate(" + margin.left + ", 0)")
        .call(yAxis);

  svg.append("g")
        .attr("class", "axis")
        .attr("transform", "translate(0, " + height + ")")
        .call(xAxis);

  svg.selectAll('.axis')
    .style({'stroke': 'Black', 'stroke-width': '1px', 'color': '#333'});

  svg.selectAll("circle")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", function(d) {
        return x(d[0]);
    })
    .attr("cy", function(d) {
        return y(d[1]);
    })
    .attr("r", 3)
    .style("fill", function(d) {
      var position = d[0];
      if (waketime < position && position < bedtime) {
        return '#ff9900';
      } else if ((bedtime < waketime) && (position > bedtime || position < waketime)) {
        return '#ff9900';
      }
      return '#000099';
    });
}
