$(document).ready(function() {
    // TODO put in a loop or smth
    $('#btnStart').click(function() {
        hideStart();

        startGame();
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

    // clear the buttons
    clearAnswers();

    console.log(questions[currentQuestion]);
    let question = questions[currentQuestion].fields;

    let answers = [];

    answers[0] = '<input type="button" value="' + question.correctAnswer + '">';
    answers[1] = '<input type="button" value="' + question.incorrectAnswer1 + '">';
    answers[2] = '<input type="button" value="' + question.incorrectAnswer2 + '">';
    answers[3] = '<input type="button" value="' + question.incorrectAnswer3 + '">';

    // shuffles (randomizes) the answers
    answers.sort(function() { return 0.5 - Math.random() });

    // concatenates 
    $('#answerGroup').append(answers.join("\n"));

    $('#answerGroup input').click(function () {
            processAnswer(this.value);
        }
    );
}

/**
    Clears the buttons
**/
function clearAnswers() {
    $('#answerGroup').empty();
}


/**
    Calls the method to display the response
    increments the number of correct answers
    if the answer is correct
    and triggers the new questions
**/
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

/**
 @return true if the current
 round is complete
 **/
function gameFinished() {
    let nextQuestion = questions[currentQuestion].fields;
    return nextQuestion.level === currentLevel + 1;
}

/**
Visualize the answer from
the user in the chat box
@param user's answer
**/
function drawAnswer(text) {
    let answer = '<div class="panel-body2">' +
        ' <p>' + text + '</p> ' +
        '</div>';

    $('.card').append(answer);
}

/**
Visualize the message for the
end of the quiz along with the
user's score
**/
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

