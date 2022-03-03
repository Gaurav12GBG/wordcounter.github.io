let upload = document.getElementById('upload');
let textArea = document.getElementById('textArea');

upload.addEventListener('change', () => {
    let files = upload.files;

    if(files.length == 0) return;

    const file = files[0];

    let reader = new FileReader();

    reader.onload = (e) => {
        const file = e.target.result;
        const lines = file.split(/\r\n|\n/);
        textArea.value = lines.join('\n');
    };

    reader.onerror = (e) => alert(e.target.error.name);

    reader.readAsText(file); 
    
})