<!DOCTYPE html>
<meta charset="utf-8">
<style>

.node circle {
  fill: #fff;
  stroke: steelblue;
  stroke-width: 1.5px;
}

.node {
  font: 10px sans-serif;
}

.link {
  fill: none;
  stroke: #ccc;

}

</style>
<body>
<script src="http://d3js.org/d3.v3.min.js"></script>
<script src="./foo.v1.js"></script>

<script>

var diameter = 960;

var tree = d3.layout.tree()
    .size([360, diameter / 2 - 120])
    .separation(function(a, b) { return (a.parent == b.parent ? 1 : 2) / a.depth; });

var diagonal = d3.svg.diagonal.radial()
    .projection(function(d) { return [d.y, d.x / 180 * Math.PI]; });

var svg = d3.select("body").append("svg")
    .attr("width", diameter)
    .attr("height", diameter - 150)
  .append("g")
    .attr("transform", "translate(" + diameter / 2 + "," + diameter / 2 + ")");

var all_children = new Array;
  function get_all_childs(d, all_childs){
    
    all_children.push(all_childs);

    if(d.children){
            var children = d.children;
            for (var i = 0; i < children.length; i++) {
                var temp_array = get_all_childs(children[i], all_children);
                console.log("got from recursion: : "+temp_array.length+" children");
                all_children.push(temp_array);
            }
    }
    else{
        //return all_children;
        //console.log("end, our array has: "+all_children.length+" elements");
    }
    return all_children;
  }
  

d3.json("youyoujson.json", function(error, root) {
  var nodes = tree.nodes(root),
      links = tree.links(nodes);

  var link = svg.selectAll(".link")
      .data(links)
    .enter().append("path")
      .attr("class", "link")
      .attr("d", diagonal)
      .attr("stroke-width",function(d){ return d.target.bytes/10000+"px";})

  var node = svg.selectAll(".node")
      .data(nodes)
    .enter().append("g")
      .attr("class", "node")
      .attr("transform", function(d) { return "rotate(" + (d.x - 90) + ")translate(" + d.y + ")"; })

  node.append("circle")
      .attr("r", 4.5)
      .on("click",get_all_children);

  node.append("text")
      .attr("dy", ".31em")
      .attr("text-anchor", function(d) { return d.x < 180 ? "start" : "end"; })
      .attr("transform", function(d) { return d.x < 180 ? "translate(8)" : "rotate(180)translate(-8)"; })
      .text(function(d) { return d.name; });

      function get_all_children(d){
         var all_children = get_all_childs(d);
             console.log("end, our array has: "+all_children.length+" elements");
           
        }
});

d3.select(self.frameElement).style("height", diameter - 150 + "px");

drawIP();

</script>