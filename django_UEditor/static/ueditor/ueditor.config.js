/**
 * ueditor complete configuration items
 * You can configure the characteristics of the entire editor here
 */
/**************************hint********************** **********
 * All commented configuration items are ueditor default values.
 * To modify the default configuration, please first make sure that the true purpose of the parameter has been fully clarified.
 * There are two main modification schemes, one is to cancel the comment here, and then modify it to the corresponding parameter; the other is to pass in the corresponding parameter when instantiating the editor.
 * When upgrading the editor, you can directly use the old version of the configuration file to replace the new version of the configuration file, don't worry about the script error caused by the lack of parameters required by the new function in the old version of the configuration file.
 **************************hint*********************** *********/

(function() {

    /**
     * The root path of the editor resource file. What it means is: take the editor instantiated page as the current path, and point to the path of the editor resource files (ie, dialog and other folders).
     * In view of the various path problems that many students have when using the editor, it is strongly recommended that you use the "relative path relative to the root directory of the website" for configuration.
     * "Relative path relative to the root of the website" is a path that starts with a slash and is like "/myProject/ueditor/".
     * If there are multiple pages in the site that are not at the same level and the editor needs to be instantiated, and the same ueditor is referenced, the URL here may not apply to the editor of each page.
     * Therefore, ueditor provides a root path that can be individually configured for different page editors. Specifically, write the following code at the top of the page where the editor needs to be instantiated. Of course, the URL here needs to be equal to the corresponding configuration.
     * window.UEDITOR_HOME_URL = "/xxxx/xxxx/";
     */
    var URL = window.UEDITOR_HOME_URL || getUEBasePath();

    /**
     * Configuration item main body. Note that the URL variable should not be omitted for all the configuration related to the path here.
     */
    window.UEDITOR_CONFIG = {

        //Add a path for the editor instance, this cannot be commented
        UEDITOR_HOME_URL: URL

        // Server unified request interface path
        ,
        serverUrl: URL + "php/controller.php"

        //All the function buttons and drop-down boxes on the toolbar can be redefined by choosing what you need in the instance of the new editor
        ,
        toolbars: [
                [
                    'fullscreen', 'source', '|', 'undo', 'redo', '|',
                    'bold', 'italic', 'underline', 'fontborder', 'strikethrough', 'superscript', 'subscript', 'removeformat', 'formatmatch', 'autotypeset', 'blockquote', 'pasteplain', '|', 'forecolor', 'backcolor', 'insertorderedlist', 'insertunorderedlist', 'selectall', 'cleardoc', '|',
                    'rowspacingtop', 'rowspacingbottom', 'lineheight', '|',
                    'customstyle', 'paragraph', 'fontfamily', 'fontsize', '|',
                    'directionalityltr', 'directionalityrtl', 'indent', '|',
                    'justifyleft', 'justifycenter', 'justifyright', 'justifyjustify', '|', 'touppercase', 'tolowercase', '|',
                    'link', 'unlink', 'anchor', '|', 'imagenone', 'imageleft', 'imageright', 'imagecenter', '|',
                    'simpleupload', 'insertimage', 'emotion', 'scrawl', 'insertvideo', 'music', 'attachment', 'map', 'gmap', 'insertframe', 'insertcode', 'webapp', 'pagebreak', 'template', 'background', '|',
                    'horizontal', 'date', 'time', 'spechars', 'snapscreen', 'wordimage', '|',
                    'inserttable', 'deletetable', 'insertparagraphbeforetable', 'insertrow', 'deleterow', 'insertcol', 'deletecol', 'mergecells', 'mergeright', 'mergedown', 'splittocells', 'splittorows', 'splittocols', 'charts', '|',
                    'print', 'preview', 'searchreplace', 'drafts', 'help'
                ]
            ]
            //The tooltip displayed when the mouse is placed on the toolbar, leave it blank to support automatic multi-language configuration, otherwise the configuration value shall prevail
            //,labelMap:{
            //    'anchor':'', 'undo':''
            //}

        //Language configuration item, the default is zh-cn. If necessary, you can also use the following method to automatically switch between multiple languages. Of course, the prerequisite is that the corresponding language file exists in the lang folder:
        //lang value can also be obtained automatically (navigator.language||navigator.browserLanguage ||navigator.userLanguage).toLowerCase()
        ,
        lang: "en",
        langPath: URL + "lang/"

        //Theme configuration item, the default is default. If necessary, you can also use the following method to automatically switch multiple themes. Of course, the prerequisite is that there is a corresponding theme file in the themes folder:
        //The following skins are available: default
        //,theme:'default'
        //,themePath:URL +"themes/"

        //,zIndex: 900 //The base of the editor level, the default is 900

        //For the getAllHtml method, the encoding setting will be added to the corresponding head tag.
        //,charset:"utf-8"

        //If you instantiate the manually modified domain of the editor page, you need to set it to true here
        //,customDomain:false

        //Common configuration items
        //, isShow: true //The editor is displayed by default

        //,textarea:'editorValue' // When the form is submitted, the server obtains the parameters used by the editor to submit the content. In the case of multiple instances, the name attribute of the container can be given, and the value given by the name will be the key value of each instance. Set this value every time it is instantiated

        //,initialContent:'Welcome to ueditor!' //Initialize the content of the editor, you can also give the value through textarea/script, see the official website example

        //,autoClearinitialContent:true //Whether to automatically clear the initial content of the editor, note: if the focus attribute is set to true, this is also true, then the editor will be triggered when the initial content is not seen

        //,focus:false //Whether to let the editor get focus during initialization true or false

        //If you customize, it’s best to give the p tag the following line height, or you will feel a sense of jumping when you don’t type in Chinese
        //,initialStyle:'p(line-height:1em)'//The base of the editor level, which can be used to change the font, etc.

        //,iframeCssUrl: URL +'/themes/iframe.css' //Introduce a css file to the iframe in the editing area

        //indentValue
        //The first line indentation distance, the default is 2em
        //,indentValue:'2em'

        //,initialFrameWidth:1000 //initialize editor width, default 1000
        //,initialFrameHeight:320 //Initialize editor height, default 320

        //,readonly: false //After the editor is initialized, whether the editing area is read-only, the default is false

        //,autoClearEmptyNode: true //Whether to delete empty inlineElement nodes when getContent (including nested cases)

        //Enable auto save
        //,enableAutoSave: true
        //Auto save interval time, unit ms
        //,saveInterval: 500

        //,fullscreen: false //Whether to turn on full screen when initializing, turn off by default

        //,imagePopup:true //The floating layer switch for image operation, which is turned on by default

        //,autoSyncData:true //Automatically synchronize the data submitted by the editor
        //, emotionLocalization: false // Whether to enable expression localization, it is disabled by default. To enable it, please make sure that the emotion folder contains the images expression folder provided by the official website

        //Paste only keep the label, remove all the attributes of the label
        //,retainOnlyLabelPasted: false

        //,pasteplain:false //Whether the default is to paste in plain text. False means not to use plain text to paste, true to use plain text to paste
        //Filtering rules in plain text paste mode
        //'filterTxtRules' : function(){
        //    function transP(node){
        //        node.tagName = 'p';
        //        node.setStyle();
        //    }
        //    return {
        // //Delete directly and its byte content
        //        '-' : 'script style object iframe embed input select',
        //        'p': {$:{}},
        //        'br':{$:{}},
        //        'div':{'$':{}},
        // 'li': {'$': {}},
        //        'caption':transP,
        //        'th':transP,
        // 'tr': transP,
        // 'h1': transP, 'h2': transP, 'h3': transP, 'h4': transP, 'h5': transP, 'h6': transP,
        //        'td':function(node){
        // // td without content is deleted directly
        // var txt = !! node.innerText ();
        //            if(txt){
        //                node.parentNode.insertAfter(UE.uNode.createText(' &nbsp; &nbsp;'),node);
        //            }
        // node.parentNode.removeChild (node, node.innerText ())
        //        }
        //    }
        //}()

        //,allHtmlEnabled:false //Does the data submitted to the background contain the entire html string

        //insertorderedlist
        //The drop-down configuration of the ordered list. When the value is left blank, it supports automatic multi-language recognition. If the value is configured, this value shall prevail
        //,'insertorderedlist':{
        // //Custom style
        // 'num':'1,2,3...',
        //        'num1':'1),2),3)...',
        // 'num2':'(1),(2),(3)...',
        //'cn':'One, two, three...',
        //'cn1':'one), two), three)...',
        //'cn2':'(one),(two),(three)...',
        // //system build-in
        //     'decimal' : '' ,         //'1,2,3...'
        //     'lower-alpha' : '' ,    // 'a,b,c...'
        //     'lower-roman' : '' ,    //'i,ii,iii...'
        //     'upper-alpha' : '' , lang   //'A,B,C'
        //     'upper-roman' : ''      //'I,II,III...'
        //}

        //insertunorderedlist
        //The drop-down configuration of the unordered list. When the value is left blank, it supports automatic multi-language recognition. If the value is configured, this value shall prevail
        //,insertunorderedlist: {//Customized style
        //'dash' :'— dash', //-dash
        //'dot':'. Small circle', //The system comes with
        //'circle':'', //'○ small circle'
        //'disc':'', //'● little dot'
        //'square':'' //'■ small square'
        //}
        //,listDefaultPaddingLeft: '30'//The base multiple of the default left indentation
        //,listiconpath:'http://bs.baidu.com/listicon/'//Custom label path
        //,maxListLevel: 3 //Limit the number of levels that can be tab, set -1 to no limit

        //,autoTransWordToList:false //Forbid the list pasted in word to automatically become list label

        //fontfamily
        //Font setting label is left blank to support automatic multi-language switching. If configured, the configured value shall prevail
        //,'fontfamily':[
        // {label:'',name:'songti',val:'Songti,SimSun'},
        // {label:'',name:'kaiti',val:'Kaiti, Kaiti_GB2312, SimKai'},
        // {label:'', name:'yahei', val:'MasaHei, Microsoft YaHei'},
        // {label:'',name:'heiti',val:'Heiti, SimHei'},
        // {label:'',name:'lishu',val:'Lishu, SimLi'},
        //    { label:'',name:'andaleMono',val:'andale mono'},
        //    { label:'',name:'arial',val:'arial, helvetica,sans-serif'},
        //    { label:'',name:'arialBlack',val:'arial black,avant garde'},
        //    { label:'',name:'comicSansMs',val:'comic sans ms'},
        //    { label:'',name:'impact',val:'impact,chicago'},
        //    { label:'',name:'timesNewRoman',val:'times new roman'}
        //]

        //fontsize
        //Font size
        //,'fontsize':[10, 11, 12, 14, 16, 18, 20, 24, 36]

        //paragraph
        //When the paragraph format value is left blank, automatic multi-language recognition is supported. If configured, the configured value shall prevail
        //,'paragraph':{'p':'', 'h1':'', 'h2':'', 'h3':'', 'h4':'', 'h5':'', 'h6':''}

        //rowspacingtop
        //The value of the paragraph spacing is the same as the displayed name
        //,'rowspacingtop':['5', '10', '15', '20', '25']

        //rowspacingBottom
        //The value of the paragraph spacing is the same as the displayed name
        //,'rowspacingbottom':['5', '10', '15', '20', '25']

        //lineheight
        //Inline spacing value is the same as the displayed name
        //,'lineheight':['1', '1.5','1.75','2', '3', '4', '5']

        //customstyle
        //Custom style, does not support internationalization, configure the value here to display the last value
        //The element of block is set according to the logic of setting paragraph, the element of inline is set according to the logic of BIU
        //Try to use some commonly used tags
        //Parameter Description
        //tag the name of the tag used
        //The name displayed by label is also used to identify different types of identifiers. Note that this value must be different for each one.
        //style added style
        //Each object is a custom style
        //,'customstyle':[
        //    {tag:'h1', name:'tc', label:'', style:'border-bottom:#ccc 2px solid;padding:0 4px 0 0;text-align:center;margin:0 0 20px 0;'},
        //    {tag:'h1', name:'tl',label:'', style:'border-bottom:#ccc 2px solid;padding:0 4px 0 0;margin:0 0 10px 0;'},
        //    {tag:'span',name:'im', label:'', style:'font-style:italic;font-weight:bold'},
        //    {tag:'span',name:'hi', label:'', style:'font-style:italic;font-weight:bold;color:rgb(51, 153, 204)'}
        //]

        //Open the right-click menu function
        //,enableContextMenu: true
        //For the content of the right-click menu, please refer to the default menu example in plugins/contextmenu.js, leave the label blank to support internationalization, otherwise this configuration shall prevail
        //,contextMenu:[
        //    {
        // label:'', //displayed name
        // cmdName:'selectall',//command command executed, when the right-click menu is clicked
        // //exec is optional, with exec, this function will be executed when clicked, the priority is higher than cmdName
        //        exec:function () {
        // //this is an instance of the current editor
        //            //this.ui._dialogs['inserttableDialog'].open();
        //        }
        //    }
        //]

        //Shortcut menu
        //,shortcutMenu:["fontfamily", "fontsize", "bold", "italic", "underline", "forecolor", "backcolor", "insertorderedlist", "insertunorderedlist"]

        //elementPathEnabled
        //Whether to enable the element path, the default is to display
        //,elementPathEnabled : true

        //wordCount
        //,wordCount:true //Whether to enable word count
        //,maximumWords:10000 //Maximum number of characters allowed
        //Word count prompt, {#count} represents the current number of words, {#leave} represents how many characters can be entered, leave it blank to support automatic multi-language switching, otherwise it will be displayed according to this configuration
        //,wordCountMsg:'' //Currently {#count} characters have been entered, you can also enter {#leave} characters
        //If the word limit is exceeded, leave it blank to support automatic multi-language switching, otherwise it will be displayed according to this configuration
        //,wordOverFlowMsg:'' //<span style="color:red;">The number of characters you have entered has exceeded the maximum allowable value, and the server may refuse to save! </span>

        //tab
        //The distance moved when the tab key is clicked, the multiple of tabSize, what character is the unit of tabNode
        //,tabSize:4
        //,tabNode:'&nbsp;'

        //removeFormat
        //Tags and attributes that can be deleted when clearing the format
        //removeForamtTags tag
        //,removeFormatTags:'b,big,code,del,dfn,em,font,i,ins,kbd,q,samp,small,span,strike,strong,sub,sup,tt,u,var'
        //removeFormatAttributes attribute
        //,removeFormatAttributes:'class,style,lang,width,height,align,hspace,valign'

        //undo
        //The maximum number of times to roll back, the default is 20
        //,maxUndoCount:20
        //When the number of characters entered exceeds this value, save the scene once
        //,maxInputCount:1

        // autoHeightEnabled
        // Whether to automatically grow taller, the default is true
        //,autoHeightEnabled:true

        //scaleEnabled
        //Is it possible to stretch the height, the default is true (when it is turned on, the automatic height is invalid)
        //, scaleEnabled: false
        //,minFrameWidth:800 //minimum width when dragging the editor, default 800
        //,minFrameHeight:220 //minimum height when dragging the editor, default 220

        //autoFloatEnabled
        //Whether to keep the position of the toolbar unchanged, the default is true
        //,autoFloatEnabled:true
        //The height of the toolbar from the top of the browser when floating, used for certain pages with fixed headers
        //,topOffset:30
        //The height of the toolbar from the bottom of the editor (if the parameter is greater than or equal to the height of the editor, the setting is invalid)
        //,toolbarTopOffset:400

        //Set whether the remote picture is captured and saved locally
        //, catchRemoteImageEnable: true //Set whether to capture remote images

        //pageBreakTag
        //Paging identifier, the default is _ueditor_page_break_tag_
        //,pageBreakTag:'_ueditor_page_break_tag_'

        // autotypeset
        //Automatic typesetting parameters
        //, autotypeset: {
        // mergeEmptyline: true, //Merge empty lines
        // removeClass: true, //Remove redundant classes
        // removeEmptyline: false, //Remove empty lines
        // textAlign:"left", //The typesetting of paragraphs, can be left, right, center, justify. Remove this attribute to indicate that typesetting is not performed
        // imageBlockLine: "center"
        // pasteFilter: false, //Filter the content pasted in according to the rules
        // clearFontSize: false, //Remove all embedded font sizes and use the editor's default font size
        // clearFontFamily: false, //Remove all embedded fonts and use the editor's default font
        // removeEmptyNode: false, // remove empty nodes
        // //Tags that can be removed
        // removeTagNames: {tag name: 1},
        // indent: false, // indent at the beginning of the line
        // indentValue: '2em', //The size of the indentation at the beginning of the line
        // bdc2sb: false,
        // tobdc: false
        //}

        //tableDragable
        //Whether the table can be dragged
        //,tableDragable: true



        //sourceEditor
        //The way to view the source code, codemirror is code highlighting, textarea is a text box, and the default is codemirror
        //Note that the default codemirror can only be used in ie8+ and non-ie
        //,sourceEditor:"codemirror"
        //If sourceEditor is codemirror, also configure two parameters
        //codeMirrorJsUrl js loaded path, the default is URL + "third-party/codemirror/codemirror.js"
        //,codeMirrorJsUrl:URL + "third-party/codemirror/codemirror.js"
        //codeMirrorCssUrl css loading path, the default is URL + "third-party/codemirror/codemirror.css"
        //,codeMirrorCssUrl:URL + "third-party/codemirror/codemirror.css"
        //Whether to enter the source code mode after the editor is initialized, the default is no.
        //,sourceEditorFirst:false

        //iframeUrlMap
        //The path of the dialog content ~ will be replaced with the URL, once the attribute is opened, it will overwrite all the default paths of the dialog
        //,iframeUrlMap:{
        //    'anchor':'~/dialogs/anchor/anchor.html',
        //}

        //allowLinkProtocol allows link addresses, link addresses with these prefixes will not automatically add http
        //, allowLinkProtocols: ['http:', 'https:', '#', '/', 'ftp:', 'mailto:', 'tel:', 'git:', 'svn:']

        //webAppKey APIkey of Baidu application, each webmaster must first go to Baidu official website to register a key before they can use the app function normally, registration introduction, http://app.baidu.com/static/cms/getapikey.html
        //, webAppKey: ""

        //Default filter rules related configuration items
        //,disabledTableInTable:true //disable table nesting
        //,allowDivTransToP:true //Div tags allowed to enter the editor automatically become p tags
        //,rgb2Hex:true //The color in the default output data is automatically changed from rgb format to hexadecimal format

        // xss filter is turned on, inserthtml and other operations
        ,
        xssFilterRules: true
            //input xss filter
            ,
        inputXssFilter: true
            //output xss filter
            ,
        outputXssFilter: true
            // Source of xss filtering whitelist: https://raw.githubusercontent.com/leizongmin/js-xss/master/lib/default.js
            ,
        whitList: {
            a: ['target', 'href', 'title', 'class', 'style'],
            abbr: ['title', 'class', 'style'],
            address: ['class', 'style'],
            area: ['shape', 'coords', 'href', 'alt'],
            article: [],
            aside: [],
            audio: ['autoplay', 'controls', 'loop', 'preload', 'src', 'class', 'style'],
            b: ['class', 'style'],
            bdi: ['dir '],
            bdo: ['dir'],
            big: [],
            blockquote: ['cite', 'class', 'style'],
            br: [],
            caption: ['class', 'style'],
            center: [],
            cite: [],
            code: ['class', 'style'],
            col: ['align', 'valign', 'span', 'width', 'class', 'style'],
            colgroup: ['align', 'valign', 'span', 'width', 'class', 'style'],
            dd: ['class', 'style'],
            del: ['datetime'],
            details: ['open'],
            div: ['class', 'style'],
            dl: ['class', 'style'],
            dt: ['class', 'style'],
            em: ['class', 'style'],
            font: ['color', 'size', 'face'],
            footer: [],
            h1: ['class', 'style'],
            h2: ['class', 'style'],
            h3: ['class', 'style'],
            h4: ['class', 'style'],
            h5: ['class', 'style'],
            h6: ['class', 'style'],
            header: [],
            hr: [],
            i: ['class', 'style'],
            img: ['src', 'alt', 'title', 'width', 'height', 'id', '_src', 'loadingclass', 'class', 'data-latex'],
            ins: ['datetime'],
            li: ['class', 'style'],
            mark: [],
            no: [],
            ol: ['class', 'style'],
            p: ['class', 'style'],
            pre: ['class', 'style'],
            s: [],
            section: [],
            small: [],
            span: ['class', 'style'],
            sub: ['class', 'style'],
            sup: ['class', 'style'],
            strong: ['class', 'style'],
            table: ['width', 'border', 'align', 'valign', 'class', 'style'],
            tbody: ['align', 'valign', 'class', 'style'],
            td: ['width', 'rowspan', 'colspan', 'align', 'valign', 'class', 'style'],
            tfoot: ['align', 'valign', 'class', 'style'],
            th: ['width', 'rowspan', 'colspan', 'align', 'valign', 'class', 'style'],
            thead: ['align', 'valign', 'class', 'style'],
            tr: ['rowspan', 'align', 'valign', 'class', 'style'],
            tt: [],
            in: [],
            ul: ['class', 'style'],
            video: ['autoplay', 'controls', 'loop', 'preload', 'src', 'height', 'width', 'class', 'style']
        }
    };

    function getUEBasePath(docUrl, confUrl) {

        return getBasePath(docUrl || self.document.URL || self.location.href, confUrl || getConfigFilePath());

    }

    function getConfigFilePath() {

        var configPath = document.getElementsByTagName('script');

        return configPath[configPath.length - 1].src;

    }

    function getBasePath(docUrl, confUrl) {

        var basePath = confUrl;


        if (/^(\/|\\\\)/.test(confUrl)) {

            basePath = /^.+?\w(\/|\\\\)/.exec(docUrl)[0] + confUrl.replace(/^(\/|\\\\)/, '');

        } else if (!/^[a-z]+:/i.test(confUrl)) {

            docUrl = docUrl.split("#")[0].split("?")[0].replace(/[^\\\/]+$/, '');

            basePath = docUrl + "" + confUrl;

        }

        return optimizationPath(basePath);

    }

    function optimizationPath(path) {

        var protocol = /^[a-z]+:\/\//.exec(path)[0],
            tmp = null,
            res = [];

        path = path.replace(protocol, "").split("?")[0].split("#")[0];

        path = path.replace(/\\/g, '/').split(/\//);

        path[path.length - 1] = "";

        while (path.length) {

            if ((tmp = path.shift()) === "..") {
                res.pop();
            } else if (tmp !== ".") {
                res.push(tmp);
            }

        }

        return protocol + res.join("/");

    }

    window.UE = {
        getUEBasePath: getUEBasePath
    };

})();