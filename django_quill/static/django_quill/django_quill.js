class QuillWrapper {
    constructor(targetDivId, targetInputId, quillOptions) {
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

(function($) {

    $(function(){
        // Setting current enabled __prefix__ object as the one that will be cloned;
        $('.django-quill-widget-container').each((idx, quill_container) => {
            let quill_widget = $(quill_container).find('.django-quill-widget');
            quill_widget = quill_widget[0];

            //Injecting this logic inside the component so I will be able to know that future cloned items will inherit this data.
            if (quill_widget.id.includes('__prefix__') === true) {
                $(quill_widget).data('is_quill_cloned', '1');
            }
        });
    });

    // Using custom events from django
    // https://docs.djangoproject.com/en/3.2/ref/contrib/admin/javascript/#inline-form-events
    $(document).on('formset:added', function(event, $row, formsetName) {
        //console.log('New item added', event, formsetName, $row);

        $('.django-quill-widget-container').each((idx, quill_container) => {

            let quill_widget = $(quill_container).find('.django-quill-widget');
            quill_widget = quill_widget[0];

            let quill_input = $(quill_container).find('.django-quill-widget-input');
            quill_input = quill_input[0];

            if (quill_widget.id.includes('__prefix__') === false) {
                if ($(quill_widget).data('is_quill_enabled') !== '1') {
                    if($(quill_widget).data('is_quill_cloned') == '1') {
                        // Removing old toolbar since it cames from the Clone;
                        $(quill_container).find('.ql-toolbar').remove();

                        console.log(quill_widget.id, quill_input.id);
                        new QuillWrapper(quill_widget.id, quill_input.id,{"theme": "snow", "modules": {"syntax": true, "toolbar": [[{"font": []}, {"header": []}, {"align": []}, "bold", "italic", "underline", "strike", "blockquote", {"color": []}, {"background": []}], ["code-block", "link", "image"], ["clean"]]}} );

                        $(quill_widget).data('is_quill_enabled', '1');
                    }
                }
            }

        });

        //if (formsetName == 'author_set') {
        // Do something
        //}
    });

    $(document).on('formset:removed', function(event, $row, formsetName) {
        // Row removed
    });

})(django.jQuery);