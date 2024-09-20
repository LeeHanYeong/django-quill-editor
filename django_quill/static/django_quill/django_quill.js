const djq = {}

class QuillWrapper {
    constructor(targetDivId, targetInputId, quillOptions) {
        if (!Quill.imports["modules/resize"] && quillOptions["modules"].resize) {
            Quill.register("modules/resize", window.QuillResizeModule);
        }
        if (!Quill.imports["modules/imageCompressor"] && quillOptions["modules"].imageCompressor) {
            Quill.register("modules/imageCompressor", imageCompressor);
        }
        this.targetDiv = document.getElementById(targetDivId);
        if (!this.targetDiv) throw 'Target div(' + targetDivId + ') id was invalid';

        this.targetInput = document.getElementById(targetInputId);
        if (!this.targetInput) throw 'Target Input id was invalid';

        this.quill = new Quill('#' + targetDivId, quillOptions);
        this.quill.on('text-change', () => {
            var delta = JSON.stringify(this.quill.getContents());
            var html = this.targetDiv.getElementsByClassName('ql-editor')[0].innerHTML;
            var data = {delta: delta, html: html};
            this.targetInput.value = JSON.stringify(data);
        });
    }
}
