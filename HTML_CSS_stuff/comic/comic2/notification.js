var finished = function(){
    var divs = $('.container > div').length;
  console.log(divs);
    if(divs >= 9){
        var msg = {
            title:"Great!!",
            text:"You have successfully created 9 scenes in comic"
        }
        success(msg);
    } else if(divs > 1){
        var remaining = 9 - divs;
        var msg = {
            title:"Good going..",
            text:"Only "+remaining+" more scenes to go"
        }
        success(msg)
    }
}

$.ajax({
    url:"story.html"
}).done(function(data){
    var status = checkForErrors(data);
  console.log(status);
    if(status == "no error"){
        finished();
    }else{
        throwError(status);
    }
});