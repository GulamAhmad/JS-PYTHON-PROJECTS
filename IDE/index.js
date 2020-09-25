function update() {
  var idoc = document.getElementById("iframe").contentWindow.document; // setting iframe as an output window

  idoc.open();
  idoc.write(editor.getValue()); // getting the value from editor and displaying it on iframe
  idoc.close();
}

//setting up the editor
function setupEditor() {
  window.editor = ace.edit("editor"); //making editor div as an editor
  editor.setTheme("ace/theme/tomorrow_night_blue"); // theme of the editor
  editor.getSession().setMode("ace/mode/html"); //editor mode
  editor.setValue(
    `<!DOCTYPE html>
  <html>
    <head>
      <title> Document </title>
    </head>
    <body>
      <p> Welcome </p>
    </body>
  </html>`,
    1
  ); //1 = moves cursor to end

  editor.getSession().on("change", function () {
    update(); //updatind the output when ever anything changes
  });

  //focusing cursor on editor
  editor.focus();

  // option for editor
  editor.setOptions({
    fontSize: "16pt",
    showLineNumbers: false,
    showGutter: false,
    vScrollBarAlwaysVisible: true,
    enableBasicAutocompletion: false,
    enableLiveAutocompletion: false,
  });

  editor.setShowPrintMargin(false);
  editor.setBehavioursEnabled(false);
}

// getting started
function ready() {
  setupEditor();
  update();
}
