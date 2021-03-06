# -*- coding: utf-8 -*-

# Copyright (c) 2012 - 2014 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module containing some JavaScript resources.
"""

from __future__ import unicode_literals

bootstrap_js = """
if(typeof GM_xmlhttpRequest === "undefined") {
    GM_xmlhttpRequest = function(/* object */ details) {
        details.method = details.method.toUpperCase() || "GET";

        if(!details.url) {
            throw("GM_xmlhttpRequest requires an URL.");
        }

        // build XMLHttpRequest object
        var oXhr = new XMLHttpRequest;
        // run it
        if(oXhr) {
            if("onreadystatechange" in details)
                oXhr.onreadystatechange = function() {
                    details.onreadystatechange(oXhr)
                };
            if("onload" in details)
                oXhr.onload = function() { details.onload(oXhr) };
            if("onerror" in details)
                oXhr.onerror = function() { details.onerror(oXhr) };

            oXhr.open(details.method, details.url, true);

            if("headers" in details)
                for(var header in details.headers)
                    oXhr.setRequestHeader(header, details.headers[header]);

            if("data" in details)
                oXhr.send(details.data);
            else
                oXhr.send();
        } else
            throw ("This Browser is not supported, please upgrade.")
    }
}

if(typeof GM_addStyle === "undefined") {
    function GM_addStyle(/* String */ styles) {
        var head = document.getElementsByTagName("head")[0];
        if (head === undefined) {
            document.onreadystatechange = function() {
                if (document.readyState == "interactive") {
                  var oStyle = document.createElement("style");
                  oStyle.setAttribute("type", "text\/css");
                  oStyle.appendChild(document.createTextNode(styles));
                  document.getElementsByTagName("head")[0].appendChild(oStyle);
                }
            }
        }
        else {
            var oStyle = document.createElement("style");
            oStyle.setAttribute("type", "text\/css");
            oStyle.appendChild(document.createTextNode(styles));
            head.appendChild(oStyle);
        }
    }
}

if(typeof GM_log === "undefined") {
    function GM_log(log) {
        if(console)
            console.log(log);
    }
}

if(typeof GM_openInTab === "undefined") {
    function GM_openInTab(url) {
        window.open(url)
    }
}

// Define unsafe window
var unsafeWindow = window;
window.wrappedJSObject = unsafeWindow;

// GM_registerMenuCommand not supported
if(typeof GM_registerMenuCommand === "undefined") {
    function GM_registerMenuCommand(caption, commandFunc, accessKey) { }
}

// GM Resource not supported
if(typeof GM_getResourceText === "undefined") {
    function GM_getResourceText(resourceName) {
        throw ("eric6 Web Browser: GM Resource is not supported!");
    }
}

if(typeof GM_getResourceURL === "undefined") {
    function GM_getResourceURL(resourceName) {
        throw ("eric6 Web Browser: GM Resource is not supported!");
    }
}

// GM Settings not supported
if(typeof GM_getValue === "undefined") {
    function GM_getValue(name, defaultValue) {
        return defaultValue;
    }
}

if(typeof GM_setValue === "undefined") {
    function GM_setValue(name, value) { }
}

if(typeof GM_deleteValue === "undefined") {
    function GM_deleteValue(name) { }
}

if(typeof GM_listValues === "undefined") {
    function GM_listValues() {
        return new Array("");
    }
}
"""
