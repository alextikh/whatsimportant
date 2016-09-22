var len =document.getElementsByClassName("emojitext").length;//the number of the messages +1

var element = document.getElementsByClassName("emojitext")[len-1];//the newest message
if((element.innerHTML.indexOf('added') == -1) &&(element.innerHTML.indexOf('removed')== -1)&&(element.innerHTML.indexOf('changed the subject')== -1))

{

if(element.classList.contains("selectable-text"))
{
  var Context = document.getElementsByClassName("emojitext")[len-1].innerHTML;//put in var the context of the message
  var Regexp = /<!-- react-text: \d+ -->(\w+)<!-- \/react-text -->/g;
  var match = Regexp.exec(Context);
  Context= match[1];
}
else{
  var Name = document.getElementsByClassName("emojitext")[len-1];//put in var the name of the message

}


}
var element2 = document.getElementsByClassName("emojitext")[len-2];//the newest message
if((element2.innerHTML.indexOf('added') == -1) &&(element2.innerHTML.indexOf('removed')== -1)&&(element2.innerHTML.indexOf('changed the subject')== -1))

{

if(element2.classList.contains("selectable-text"))
{
  var Context = document.getElementsByClassName("emojitext")[len-2].innerHTML;//put in var the context of the message
  var Regexp = /<!-- react-text: \d+ -->(\w+)<!-- \/react-text -->/g;
  var match = Regexp.exec(Context);
  Context= match[1];
}
else{
  var Name = document.getElementsByClassName(number);//put in var the name of the message

}


}
alert("Context " +Context);
alert("Name " +Name);


//if(element.classList.contains("selectable-text")&&element:not(:contains('added'))&&element:not(:contains('removed')))//check if the element is the context of the message and it is real one
