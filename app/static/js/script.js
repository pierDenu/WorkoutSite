// Declare functions outside of DOMContentLoaded

// Function to handle adding exercises
async function getDataById(exerciseId) {
    try {
        // Використовуємо шаблонні рядки для формування URL з параметром query
        const response = await fetch(`/exercise-data-by-id/${exerciseId}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });

        // Перевірка статусу відповіді
        if (!response.ok) {
            // Якщо статус не 200, викидаємо помилку з повідомленням
            throw new Error(`Error: ${response.status} - ${response.statusText}`);
        }

        // Отримання даних як JSON
        const data = await response.json();

        // Повертаємо отримані дані
        return data;
    } catch (error) {
        // Логування помилки
        console.error('Error fetching exercise data:', error);
        // Можна повернути null або додатково обробити помилку, залежно від вимог
        return null;
    }
}

// Function to get workout data
function getWorkoutData(addedExercisesList) {
    const exercises = [];
    const addedExercises = addedExercisesList.querySelectorAll('li');
    const errors = [];

    addedExercises.forEach((exerciseItem, index) => {
        const exerciseId = exerciseItem.getAttribute('data-id');
        const reps = exerciseItem.querySelector('.reps').value;
        const restTime = exerciseItem.querySelector('.rest-time').value;
        const additionalWeightInput = exerciseItem.querySelector('.add-weight');
        const additionalWeight = additionalWeightInput ? additionalWeightInput.value : 0;  // Якщо є поле, беремо значення

        if (!reps || !restTime) {
            const exerciseName = exerciseItem.textContent.split('\n')[0].trim();
            errors.push(`Exercise #${index + 1} (${exerciseName}): Please fill in both Reps and Rest Time.`);
        }

        exercises.push({
            exercise_id: exerciseId,
            reps: reps ? parseInt(reps) : null,
            rest_time: restTime ? parseInt(restTime) : null,
            additional_weight: additionalWeight ? parseInt(additionalWeight) : 0,  // Якщо є додаткова вага, беремо значення, інакше 0
            order: index + 1
        });
    });

    if (errors.length > 0) {
        throw new Error(errors.join('\n'));
    }

    return exercises;
}

// Function to handle saving workout
function saveWorkout(addedExercisesList) {
    const workoutName = document.getElementById("workout-name").value;
    if (!workoutName) {
        alert('Please enter a workout name.');
        return;
    }

    try {
        const exercises = getWorkoutData(addedExercisesList);

        const workoutData = {
            name: workoutName,
            duration: 60,
            exercises: exercises
        };

        // Send workout data to the server
        fetch('/save-workout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ workout: workoutData })
        })
        .then(response => response.json())
        .then(data => {
            if (data.message) {
                alert(data.message);
            } else {
                alert('Something went wrong');
            }
        })
        .catch(error => console.error('Error:', error));
    } catch (error) {
        alert(error.message);
    }
}

// Функція для додавання елемента у список
function addExercise(event, addedExercisesList) {
    const exercise = event.target;  // Отримуємо елемент, на який клікнули
    if (exercise.id === 'exercise')
        addedExercisesList.appendChild(exercise.cloneNode(true));
}

// Функція для додавання обробника події на кожен елемент списку
function setExerciseAdding(allExercisesList, addedExercisesList) {
    allExercisesList.addEventListener('click', (event) => addExercise(event, addedExercisesList));
}

function deleteExersice(event) {
    const exercise = event.target;  // Отримуємо елемент, на який клікнули
    if (exercise.id === 'exercise')
        exercise.remove();
}

function setExerciseDeleting(addedExercisesList) {
    addedExercisesList.addEventListener('click', (event) => deleteExersice(event));
}

// DOMContentLoaded event listener
document.addEventListener('DOMContentLoaded', function () {
    const addedExercisesList = document.getElementById('added-exercises');
    const allExercisesList = document.getElementById('all-exercises');

    setExerciseAdding(allExercisesList, addedExercisesList)
    setExerciseDeleting(addedExercisesList)

    const saveButton = document.getElementById("save-workout");
    saveButton.addEventListener('click', () => {
        saveWorkout(addedExercisesList)
    })
});
