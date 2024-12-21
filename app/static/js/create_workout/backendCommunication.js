import {hide} from "./displayElements.js";

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
export function saveWorkout(addedExercisesList) {
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
        fetch('/workouts/save', {
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


export async function searchExercise(input) {
    const response = await fetch(`/search-exercise-name/${input}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });
    const data = await response.json();
    const exercises = data['exercises']
    return exercises;
}



export async function filterByGroup(event, list) {
    const muscleGroup = event.target;
    if (muscleGroup.classList.contains('muscle-group')) {
        try {
            const groupName = muscleGroup.innerHTML; // or use a `data-name` attribute
            const response = await fetch(`/search-exercise-muscle-group/${groupName}`);

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            const exercises = data['exercises']

            // Hide the list (if needed) and return the filtered data
            hide(list);
            return exercises;
        } catch (error) {
            console.error('Error:', error);
        }
    }
}
