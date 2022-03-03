function myFunction() {
    //Get the textfield
    var copyText = document.getElementById("textArea");

    //select the textfield
    copyText.select();
    copyText.setSelectionRange(0, 99999);

    //Copy the text inside the text field 
    navigator.clipboard.writeText(copyText.value);

    
   //Alert the copied text
   alert("Copied the text");
  }