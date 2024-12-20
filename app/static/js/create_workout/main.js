import { setExerciseAdding, setExerciseDeleting } from './exerciseManager.js';
import { saveWorkout, searchExercise, filterByGroup } from './backendCommunication.js'
import { hide, show, toggleHideAndShow, displayExercises } from './displayElements.js'

document.addEventListener('DOMContentLoaded', function () {
    const addedExercisesList = document.getElementById('added-exercises');
    const allExercisesList = document.getElementById('all-exercises');

    setExerciseAdding(allExercisesList, addedExercisesList)
    setExerciseDeleting(addedExercisesList)

    const saveButton = document.getElementById("save-workout");
    saveButton.addEventListener('click', () => {
        saveWorkout(addedExercisesList)
    })

    const searchExerciseByName = document.getElementById("exersice-name-search");
    searchExerciseByName.addEventListener('input', async (event) => {
        const input = event.target.value;
        const exercises = await searchExercise(input);
        displayExercises(exercises, allExercisesList);
    });

    const MuscleGroupsButton = document.getElementById("dropdown-button")
    const MuscleGroupsList = document.getElementById("muscle-group-list")
    hide(MuscleGroupsList)
    MuscleGroupsButton.addEventListener('click', (event) => {
        toggleHideAndShow(MuscleGroupsList);
    });
    MuscleGroupsList.addEventListener('click', async (event) => {
        const exercises = await filterByGroup(event, MuscleGroupsList);
        displayExercises(exercises, allExercisesList);
    });


});