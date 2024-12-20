function addExercise(event, addedExercisesList) {
    const exercise = event.target;  // Отримуємо елемент, на який клікнули
    if (exercise.classList.contains('exercise'))
        addedExercisesList.appendChild(exercise.cloneNode(true));
}

// Функція для додавання обробника події на кожен елемент списку
export function setExerciseAdding(allExercisesList, addedExercisesList) {
    allExercisesList.addEventListener('click', (event) => addExercise(event, addedExercisesList));
}

function deleteExersice(event) {
    const exercise = event.target;  // Отримуємо елемент, на який клікнули
    if (exercise.classList.contains('exercise'))
        exercise.remove();
}

export function setExerciseDeleting(addedExercisesList) {
    addedExercisesList.addEventListener('click', (event) => deleteExersice(event));
}