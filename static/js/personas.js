$(document).ready(function(){
// TODO put in a loop
getQuestions();
    drawQuestion("Koe e nai sladkoto <3 :D ");
    updateAnswers("maimunka", "kuchence", "zaiche", "mishlence");

    $('input').click(function () {
            console.log("button clicked")
                drawRespond(this.value);
                resetAnswers();
                console.log();
            }
    );
    console.log(question);
});

    var correctAnswers;
    var wrongAnswers;
    var question;

// Displays the question in the chatbox
 function drawQuestion(text){
   let question = '<p>' + '<div class="panel-body">' +
           ' <p>' + text +  '</p> ' +
        '</div>' + '</p>';

   $('.card').append(question);

 }

// Displays the answer in the chatbox
 function drawRespond(text){
    let answer = '<div class="panel-body2">' +
                    ' <p>' + text +  '</p> ' +
                 '</div>';

   $('.card').append(answer); }


// Reads the answers corresponding to the question from the database
// and updates each button accordingly
 function updateAnswers(value1, value2, value3, value4){
    //TODO get answers from the database and update the buttons accordingly

    $("#btn1").attr('value', value1);
    $("#btn2").attr('value', value2);
    $("#btn3").attr('value', value3);
    $("#btn4").attr('value', value4);
 }


// Resets the buttons to their default value
 function resetAnswers(){
    $("#btn1").attr('value', 'Option1');
    $("#btn2").attr('value', 'Option2');
    $("#btn3").attr('value', 'Option3');
    $("#btn4").attr('value', 'Option4');
 }


// Do I really need that? Pfff :D
 function getResponse(answer){
    $.ajax({
            type: "GET",
            url: "" + answer, //TODO QUE?
            success: function () {
               //TODO

            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                alert("Status: " + textStatus);
                alert("Error: " + errorThrown);
            }
        });
 }


// Keep track of the correct and incorrect answers of the current quiz/conversation
 function storeScore(answer){ //TODO reconsider.... perhaps check answer's id to see if it is correct

        if (answer){
            correctAnswers++;
        }
        else
            wrongAnswers++;
 }

 function getQuestions (){

 $('#btn1').click(function() {
        alert("woop woop");

    $.ajax({
    url: '/explorescotland/quizzes/',
    success: function(data) {
    question = data;
    }
    });

    });
 };


$(document).ready(function() {

    $('#testAJAXButton').click(function() {
        alert("worked");

        $.ajax({
            url: '/explorescotland/test_ajax/',
            success: function(data) {
                alert(data);
            }
        });

    });

});
