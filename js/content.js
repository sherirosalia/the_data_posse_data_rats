function ratRates(){
    let containerDiv=document.getElementById("ratRates"),
    url="https://public.tableau.com/views/Rats-in-the-Restaurants/BehaviorAnalysis?:language=en&:display_count=y&:origin=viz_share_link";

    let viz = new tableau.Viz(containerDiv, url);
    
}
$(document).ready(function(){
       
        ratRates()
        });


        




// 
// initViz()
// $( window ).load(function() {
//     initViz()
//   });
// $(document).ready(function(){
//     	$('.content').css({
//       	'margin-top':$('.jumbotron').outerHeight()
//       });
//     });

// document.getElementById("demo").innerHTML = "Hello World!";