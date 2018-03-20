$(document).ready(function(){
// TODO put in a loop or smth
$('#btnStart').click(function(){
    $(this).hide();
    $('.panel-body3').hide();

    getQuestions();
//    questions1();
//    console.log(questionsLevel1);

    drawQuestion(question.question);
    updateAnswers(question.correctAnswer, question.incorrectAnswer1, question.incorrectAnswer2, question.incorrectAnswer3);
    response();
    drawQuizEnd();

})
});

    var correctAnswers = 0;
    var question = {};
    var level;
    var questionsLevel1;
    var questionsLevel2;
    var questionsLevel3;
    var questionsLevel4;
    var questionsLevel5;
    var questionsLevel6;

    /**
    Methods that retrieve and manipulate data from the database
    **/

    /**
    Ajax method to retrieve all quiz
    questions from the database
    **/

    function getQuestions (){

    $.ajax({
    url: '/explorescotland/quizzes/',
    dataType: 'json',
    type: 'GET',
    success: function(data) {
    question = data;

    console.log(question);
    }

    });
    };

    /**
    Ajax method to retrieve the child's
    level from the database
    **/
    function getLevel (){
    $.ajax({
    url: '/explorescotland/level',
    success: function(data){
    level = data;
    }
    });
    };

/**
 Filters and stores in an array
 all questions for level 1
 **/

//    function questions1(level){
//        return level == 1;
//    }
//
//    questionsLevel1 = question.filter(questions1);
 /**
 Filters and stores in an array
 all questions for level 2
 **/
 //    function questions2(level){
//        return level == 2;
//    }
//
//    questionsLevel2 = question.filter(questions2);

 /**
 Filters and stores in an array
 all questions for level 3
 **/

//    function questions3(level){
//        return level == 3;
//    }
//
//    questionsLevel3 = question.filter(questions3);


 /**
 Filters and stores in an array
 all questions for level 4
 **/

 //    function questions4(level){
//        return level == 4;
//    }
//
//    questionsLevel4 = question.filter(questions4);

 /**
 Filters and stores in an array
 all questions for level 5
 **/

 //    function questions5(level){
//        return level == 5;
//    }
//
//    questionsLevel5 = question.filter(questions5);

 /**
 Filters and stores in an array
 all questions for level 6
 **/

 //    function questions6(level){
//        return level == 6;
//    }
//
//    questionsLevel6 = question.filter(questions6);


 /** Methods responsible for the
 visual representation to the user**/

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

/** Draws a message for the end of the quiz**/
 function drawQuizEnd(){
    let finale = '<div class="panel-body">' +
                    ' <p>';
    if (correctAnswers == 5){
        finale+="Congratulations! You answered correctly on all my questions. You progress to the next level!"
        + '</p> ' + '</div>';
    }
    else {
        finale+= "Thank you! It was lovely talking to you today! Your score from the quiz is "
        + correctAnswers +'</p>' + '</div>';
    }
   $('.card').append(finale);
 }

// Updates each button with the corresponding answers
 function updateAnswers(value1, value2, value3, value4){

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

        if (answer.id == question.correctAnswer){ //TODO edit
            correctAnswers++;
        }
 }

/** Keeps track of the child's level **/
function storeLevel (){
    if (correctAnswers == 5){
        level++;
    }
}


function response(){
$('input').click(function () {
            console.log("button clicked")
                drawRespond(this.value);
                resetAnswers();
            }
    );
}
