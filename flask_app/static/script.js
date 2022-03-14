const states = {
    QUESTION_1 : "Which direction do you like your toilet paper to face?",
    QUESTION_2 : "The supervisor you hate the most is waving at you like you're bff's. How do you act?",
    QUESTION_3 : "Who has the sexier superheroes: Marvel or DC?",
    QUESTION_4 : "You're Batman! Joker is across town wrecking havoc. What do you do?",
    QUESTION_5 : "You're Thor! Loki is across town wrecking havoc. What do you do?",
    QUESTION_6 : "In a videogame, you are most likely to be a:",
    QUESTION_7 : "You're running late to a date you met on Tinder. What saddens you more?",
    QUESTION_8 : "The crypto coin all your friends forced you to invest in just skyrocketed. You're rich! What's the first thing you do?;",
    QUESTION_9 : "You're favorite character on the Netflix show you're watching is about to die. How do you feel?",
    QUESTION_10 : "At the last second, you get a blue shell and beat your friend at Mario Party. How do you act?",
    RESULT_1 : "You are hostile and dominant (and cant beat me in Mario Party)",
    RESULT_2 : "You are dominant (and cant beat me in Mario Party)",
    RESULT_3 : "You are warm and dominant (and cant beat me in Mario Party)",
    RESULT_4 : "You are hostile and submissive (and cant beat me in Mario Party)",
    RESULT_5 : "You are submissive (and cant beat me in Mario Party)",
    RESULT_6 : "You are warm and submissive (and cant beat me in Mario Party)",
}

const triggers = {
    ANSWER_1 : "Over",
    ANSWER_2 : "Under",
    ANSWER_3 : "Become superficially friendly and fake affection",
    ANSWER_4 : "Pretend you didn't see them and keep walking",
    ANSWER_5 : "Warrior",
    ANSWER_6 : "Mage",
    ANSWER_7 : "Marvel",
    ANSWER_8 : "DC",
    ANSWER_9 : "Disappointing myself",
    ANSWER_10 : "Disappointing them",
    ANSWER_11 : "SHOPPING!!!",
    ANSWER_12 : 'Time to start saving and investing!',
    ANSWER_13 : 'Plan the best way to get a surprise attack',
    ANSWER_14 : "Screw planning! LET'S GO KICK SOME A-",
    ANSWER_15 : 'Plan the best way to get a surprise attack',
    ANSWER_16 : "Screw planning! LET'S GO KICK SOME A-",
    ANSWER_17 : "It's not that deep",
    ANSWER_18 : 'Become anxious and depressed',
    ANSWER_19 : 'Gloat all up in their face',
    ANSWER_20 : 'Accept my win graciously',
}
// use dom to create objects
let container = document.getElementById('box_container');
container.className = 'questions';
// when someone clicks on submit a click event happens:
let submit = document.getElementById('submit'); 
submit.addEventListener('click', next);
// new radio button options based on radio value 
let total = 0;
let i = 2;
function next(e) {
    e.preventDefault();
    // collect value from radio
    const choice = document.querySelectorAll('input[name="choice"]');
    for (const answer of choice) {
        if(answer.checked) {
            total += parseInt(answer.value);
            console.log(total);
            while(i<6){
                // a new box appears
                let box = document.createElement('div');
                
                // change box appearance based on number
                box.className = "daily q"+i+"";
                container.appendChild(box);
                
                //---------------------------QUESTIONS---------------------------------
                let newQuestion = document.createElement("p");
                newQuestion.className = "daily-question"
                box.appendChild(newQuestion);
                
                let answerOneDiv = document.createElement('div');
                box.appendChild(answerOneDiv);
                
                let answerOne = document.createElement("input");
                answerOne.setAttribute("type","radio");
                answerOne.setAttribute("name", "choice")
                answerOne.setAttribute("value", 1)
                answerOneDiv.appendChild(answerOne);
                
                let answerOneLabel = document.createElement("label");
                answerOneDiv.appendChild(answerOneLabel);
                answerOneLabel.textContent = " ";
                
                let answerTwoDiv = document.createElement('div');
                box.appendChild(answerTwoDiv);
                
                let answerTwo = document.createElement("input");
                answerTwo.setAttribute("type","radio");
                answerTwo.setAttribute("name", "choice")
                answerTwo.setAttribute("value", 2)
                answerTwoDiv.appendChild(answerTwo);
                
                let answerTwoLabel = document.createElement("label");
                answerTwoDiv.appendChild(answerTwoLabel);
                answerTwoLabel.textContent = " ";

                //---------------------------BOX 2---------------------------------
                if (box.className == "daily q2"){        
                    newQuestion.textContent = states['QUESTION_2'];
                    answerOneLabel.textContent = triggers['ANSWER_3'];
                    answerTwoLabel.textContent = triggers['ANSWER_4'];
                }
                
                //---------------------------BOX 3---------------------------------             
                if (box.className == "daily q3"){
                    if (total == 2) {
                        newQuestion.textContent = states['QUESTION_6'];
                        answerOneLabel.textContent = triggers['ANSWER_5'];
                        answerTwoLabel.textContent = triggers['ANSWER_6'];                     
                    }
                    if (total == 3) {
                        newQuestion.textContent = states['QUESTION_3'];
                        answerOneLabel.textContent = triggers['ANSWER_7'];
                        answerTwoLabel.textContent = triggers['ANSWER_8'];                        
                    }
                    if (total == 4) {
                        newQuestion.textContent = states['QUESTION_7'];
                        answerOneLabel.textContent = triggers['ANSWER_9'];
                        answerTwoLabel.textContent = triggers['ANSWER_10'];                     
                    }
                }

                //---------------------------BOX 4---------------------------------  
                    if (box.className == "daily q4"){
                        if (total == 3) {
                            newQuestion.textContent = states['QUESTION_8'];
                            answerOneLabel.textContent = triggers['ANSWER_11'];
                            answerTwoLabel.textContent = triggers['ANSWER_12'];                        
                        }
                        if (total == 4) {
                            newQuestion.textContent = states['QUESTION_5'];
                            answerOneLabel.textContent = triggers['ANSWER_13'];
                            answerTwoLabel.textContent = triggers['ANSWER_14'];                        
                        }
                        if (total == 5) {
                            newQuestion.textContent = states['QUESTION_4'];
                            answerOneLabel.textContent = triggers['ANSWER_15'];
                            answerTwoLabel.textContent = triggers['ANSWER_16'];                        
                        }
                        if (total == 6) {
                            newQuestion.textContent = states['QUESTION_9'];
                            answerOneLabel.textContent = triggers['ANSWER_17'];
                            answerTwoLabel.textContent = triggers['ANSWER_18'];                        
                        }
                    }
                //---------------------------BOX 5---------------------------------  
                if (box.className == "daily q5"){
                    newQuestion.textContent = states['QUESTION_10'];
                    answerOneLabel.textContent = triggers['ANSWER_19'];
                    answerTwoLabel.textContent = triggers['ANSWER_20'];                        
                }
                // SUBMIT BUTTON
                box.appendChild(submit);
                i++;
                return;
            }
        }
    }
}