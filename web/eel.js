(function() {
    window.eel = new Proxy({}, {
        get: function(target, name) {
            return function(...args) {
                return new Promise(function(resolve, reject) {
                    const callId = Math.random().toString(36).substr(2, 9);
                    window[`__eel_return_${callId}`] = resolve;
                    window.eel._eel._call(name, args, callId);
                });
            };
        }
    });

    window.eel._eel = {
        _call: function(name, args, callId) {
            const message = {
                name: name,
                args: args,
                call: callId
            };
            window.sendEelMessage(JSON.stringify(message));
        }
    };

    window.sendEelMessage = function(message) {
        if (window.external && 'invoke' in window.external) {
            window.external.invoke(message);
        } else if (window.chrome && window.chrome.webview) {
            window.chrome.webview.postMessage(message);
        } else {
            console.error("Eel: Unable to send message from JavaScript to Python.");
        }
    };

    window._eel_expose = function(name, func) {
        window[`__eel_exposed_${name}`] = func;
    };

    window._eel_return = function(callId, value) {
        const resolve = window[`__eel_return_${callId}`];
        if (resolve) {
            resolve(value);
            delete window[`__eel_return_${callId}`];
        }
    };
})();
