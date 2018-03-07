$(document).ready(function(){

var sendMessage;
sendMessage = function (text) {
            var $messages, message;
            if (text.trim() === '') {
                return;
            }

sendMessage('Hello Philip! :)');
        setTimeout(function () {
            return sendMessage('Hi Sandy! How are you?');
        }, 1000);
        return setTimeout(function () {
            return sendMessage('I\'m fine, thank you!');
        }, 2000);

}