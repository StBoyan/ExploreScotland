$(document).ready(function() {
    // TODO put in a loop or smth
    $('#btnStart').click(function() {
        hideStart();

        startGame();
        //    questions1();
        //    console.log(questionsLevel1);
        //drawQuestion(question.question);
        //updateAnswers("zaiche", question.incorrectAnswer1, question.incorrectAnswer2, question.incorrectAnswer3);
        //response();
        //drawQuizEnd();

    })
});

function hideStart() {
	$('#btnStart').hide();
    $('.panel-body3').hide();
}



var correctAnswers = 0;
var questions = [];
var currentQuestion = 0;
var currentLevel = 1;

/**
Methods that retrieve and manipulate data from the database
**/

/**
Ajax method to retrieve all quiz
questions from the database
**/

function startGame() {

    $.ajax({
        url: '/explorescotland/quizzes/',
        dataType: 'json',
        type: 'GET',
        success: function(data) {
            questions = data;
			drawQuestion();
			drawAnswerButtons();
        }

    });
};

function drawQuestion() {
    console.log(questions[currentQuestion]);
    let question = questions[currentQuestion].fields;

    let questionHtml = '<p>' + '<div class="panel-body">' +
        ' <p>' + question.question + '</p> ' +
        '</div>' + '</p>';

    $('.card').append(questionHtml);
}

function drawAnswerButtons() {

    // clear
    clearAnswers();

    console.log(questions[currentQuestion]);
    let question = questions[currentQuestion].fields;

    let answers = [];

    answers[0] = '<input type="button" value="' + question.correctAnswer + '">';
    answers[1] = '<input type="button" value="' + question.incorrectAnswer1 + '">';
    answers[2] = '<input type="button" value="' + question.incorrectAnswer2 + '">';
    answers[3] = '<input type="button" value="' + question.incorrectAnswer3 + '">';

    // shuffle
    answers.sort(function() { return 0.5 - Math.random() });

    //draw
    $('#answerGroup').append(answers.join("\n"));

    $('#answerGroup input').click(function () {
            processAnswer(this.value);
        }
    );
}


function clearAnswers() {
    $('#answerGroup').empty();
}



function processAnswer(text) {
    console.log(text);

    drawAnswer(text);

    if (questions[currentQuestion].fields.correctAnswer === text) {
        correctAnswers++;
    }
    currentQuestion++;

    let finished = gameFinished();
    if (finished) {
        clearAnswers()
        drawQuizEnd();
    } else {
        drawQuestion();
        drawAnswerButtons();
    }
}

function gameFinished() {
    let nextQuestion = questions[currentQuestion].fields;
    return nextQuestion.level === currentLevel + 1;
}

function drawAnswer(text) {
    let answer = '<div class="panel-body2">' +
        ' <p>' + text + '</p> ' +
        '</div>';

    $('.card').append(answer);
}

function drawQuizEnd() {
    let finale = '<div class="panel-body">' +
        ' <p>';
    if (correctAnswers == 5) {

        console.log("Call the backend to update the level of the user...");
        finale += "Congratulations! You answered correctly on all my questions. You progress to the next level!" +
            '</p> ' + '</div>';
    } else {
        finale += "Thank you! It was lovely talking to you today! Your score from the quiz is " +
            correctAnswers + '</p>' + '</div>';
    }
    $('.card').append(finale);
}


/**
Ajax method to retrieve the child's
level from the database
**/
function getLevel() {
    $.ajax({
        url: '/explorescotland/level',
        success: function(data) {
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

// Displays the answer in the chatbox


/** Draws a message for the end of the quiz**/


// Keep track of the correct and incorrect answers of the current quiz/conversation
function storeScore(answer) { //TODO reconsider.... perhaps check answer's id to see if it is correct

    if (answer.id == question.correctAnswer) { //TODO edit
        correctAnswers++;
    }
}

/** Keeps track of the child's level **/
function storeLevel() {
    if (correctAnswers == 5) {
        level++;
    }
}


function response() {
    $('input').click(function() {
        console.log("button clicked")
        drawRespond(this.value);
        resetAnswers();
    });
}