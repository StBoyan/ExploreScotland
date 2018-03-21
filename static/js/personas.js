$(document).ready(function() {
    $('#btnStart').click(function() {
        hideStart();

        getLevel();
    })
});

/**
    Hide the introductory information and button
**/
function hideStart() {
	$('#btnStart').hide();
    $('.panel-body3').hide();
}



var correctAnswers = 0;
var questions = [];
var currentQuestion = 0;
var currentLevel = 0;

/**
Ajax method to retrieve child's
level from the database
**/

function getLevel() {

    $.ajax({
        url: '/explorescotland/level/',
        dataType: 'json',
        type: 'GET',
        success: function(data) {
        let data2 = data[0]['fields'];
            currentLevel = data2['level'];
            currentQuestion = (currentLevel - 1) * 5;
            startGame();
        }

    });
};

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

/**
    Visualizes the questions by the personas in the
    chat box
**/
function drawQuestion() {
    console.log(questions[currentQuestion]);

    let question = questions[currentQuestion].fields;
    let questionHtml = '<p>' + '<div class="panel-body">' +
        ' <p>' + question.question + '</p> ' +
        '</div>' + '</p>';

    $('.card').append(questionHtml);
}

/**
    Displays the buttons with the possible answers
**/
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

    // concatenates the randomized answers
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
        setTimeout(function(){
        drawQuestion();
        drawAnswerButtons();
        }, 1500);
    }
}

/**
 @return true if the current
 round is complete
 **/
function gameFinished() {
    let nextQuestion = questions[currentQuestion].fields;
    alert("Next Q level = " + nextQuestion.level + "current level =" + currentLevel);
    return nextQuestion.level === currentLevel + 1;
}

/**
Visualize the answer from
the user in the chat box
@param user's answer
**/
function drawAnswer(text) {
    let answer = '<div class="float-left">' + '<div class="panel-body2">' +
        ' <p>' + text + '</p> ' +
        '</div>' + '</div>';

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

