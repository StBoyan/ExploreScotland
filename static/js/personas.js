$(document).ready(function(){
// TODO put in a loop
$('#btnStart').click(function(){
    $(this).hide();

//    for ( i = 0; i<=5; i++){
    getQuestions();
    response();
//    }
    drawQuizEnd();

})

//    drawQuestion(getQuestions.question);
//    updateAnswers(getQuestions.correctAnswer, getQuestions.incorrectAnswer1, getQuestions.incorrectAnswer2, getQuestions.incorrectAnswer3);


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

// Keep track of the correct and incorrect answers of the current quiz/conversation
 function storeScore(answer){ //TODO reconsider.... perhaps check answer's id to see if it is correct

        if (answer){
            correctAnswers++;
        }
        else
            wrongAnswers++;
 }

 function getQuestions (){

    $.ajax({
    url: '/explorescotland/quizzes/',
    success: function(data) {
    question = data;
    drawQuestion(question.question);
    updateAnswers(question.correctAnswer, question.incorrectAnswer1, question.incorrectAnswer2, question.incorrectAnswer3);
    }

    });
 };

function response(){
$('input').click(function () {
            console.log("button clicked")
                drawRespond(this.value);
                resetAnswers();
                console.log();
            }
    );
}
 function drawQuizEnd(){
    let finale = '<div class="panel-body">' +
                    ' <p>';
    if (correctAnswers == 5){
        finale+="Congratulations! You answered correctly on all my questions. You progress to the next level!" + '</p> ' + '</div>';
    }
    else {
        finale+= "Thank you! It was lovely talking to you today! Your score from the quiz is " + correctAnswers +'</p>' + '</div>';
    }
   $('.card').append(finale);
 }


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
