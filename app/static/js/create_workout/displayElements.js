export function displayExercises(exercises, exerciseList) {
    exerciseList.innerHTML = '';
    console.log(exercises);
    exercises.forEach(exercise => {
        const listItem = document.createElement('li');
        listItem.setAttribute('data-id', exercise.id);
        listItem.classList.add('exercise');
        listItem.innerHTML = `
        ${exercise.name}
        <input type="number" class="reps" placeholder="Reps">
        <input type="number" class="rest-time" placeholder="Rest Time (sec)">
        ${exercise.needs_additional_weight ? '<input type="number"' +
                ' class="add-weight" placeholder="Additional weight (kg)">' : ''}`;
        exerciseList.appendChild(listItem);
    });
}

export function hide(element) {
    element.style.display = 'none';
}

export function show(element) {
    element.style.display = 'block';
}

export function toggleHideAndShow(element) {
    if (element.style.display === 'none' || element.style.display === '') {
        show(element);// Show the list
    }
    else {
        hide(element);   // Hide the list
    }
}