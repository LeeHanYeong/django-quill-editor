class QuillWrapper {
  constructor(targetDivId, targetInputId, quillOptions) {
    this.targetDiv = document.getElementById(targetDivId);
    if (!this.targetDiv) throw 'Target div(' + targetDivId + ') id was invalid';

    this.targetInput = document.getElementById(targetInputId);
    if (!this.targetInput) throw 'Target Input id was invalid';

    if (quillOptions.useInlineStyleAttributes) {
      // https://quilljs.com/guides/how-to-customize-quill/#class-vs-inline
      Quill.register(Quill.import('attributors/style/align'), true);
    }

    if (quillOptions.modules && quillOptions.modules.imageUploader && quillOptions.modules.imageUploader.uploadURL) {
      // https://www.npmjs.com/package/quill-image-uploader
      Quill.register("modules/imageUploader", ImageUploader);

      var headers = {};
      if (quillOptions.modules.imageUploader.addCSRFTokenHeader) {
       headers['X-CSRFToken'] = document.querySelector('[name=csrfmiddlewaretoken]').value
      }

      var imageUploaderModule = {
        upload: file => {
          return new Promise((resolve, reject) => {
            const formData = new FormData();
            formData.append("image", file);

            fetch(
                quillOptions.modules.imageUploader.uploadURL, {
                  method: "POST",
                  body: formData,
                  headers: headers,
                }
              )
              .then(response => response.json())
              .then(result => {
                console.log(result);
                resolve(result.image_url);
              })
              .catch(error => {
                reject("Upload failed");
                alert("Uploading  failed");
                console.error("Error:", error);
              });
          });
        }
      }

    }

    this.quill = new Quill('#' + targetDivId, {
      ...quillOptions,
      modules: {
        ...quillOptions.modules,
        imageUploader: imageUploaderModule
      }
    });
    this.quill.on('text-change', () => {
      var delta = JSON.stringify(this.quill.getContents());
      var html = this.targetDiv.getElementsByClassName('ql-editor')[0].innerHTML;
      var data = {
        delta: delta,
        html: html
      };
      this.targetInput.value = JSON.stringify(data);
    });
  }
}