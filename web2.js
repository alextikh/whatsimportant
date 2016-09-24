var len =document.getElementsByClassName("selectable-text").length;//the number of the messages +1

var text = document.getElementsByClassName("selectable-text")[len-1];//the newest message

if(text.innerHTML.length>0){
  var Context = text.innerHTML;//put in var the context of the message
  var Regexp = /<!-- react-text: \d+ -->(\w+)<!-- \/react-text -->/g;
  var match = Regexp.exec(Context);
  Context= match[1];
}

var len =document.getElementsByClassName("message-pre-text").length;//the number of the messages +1

var name = document.getElementsByClassName("message-pre-text")[len-1];//the newest message
var the_name = document.getElementsByClassName("message-pre-text")[len-1].innerHTML;
if(the_name.length>0)
{
  var Name = the_name;//put in var the context of the message
  //var Regexp = /<!-- react-text: \d+ -->(\w+)<!-- \/react-text -->/g;
  //var match = Regexp.exec(Context);
  //Context= match[1];
}


console.log(Name);

alert("Context " +Context);
alert("Name " +Name);


//if(element.classList.contains("selectable-text")&&element:not(:contains('added'))&&element:not(:contains('removed')))//check if the element is the context of the message and it is real one
