import { handleDragStart, handleDragOver, handleDrop, handleDragEnd, handleDragLeave } from './dragHandling.js';

document.addEventListener('DOMContentLoaded', function () {
    const availableWorkoutsGrid = document.querySelectorAll('.workouts-grid');
    const daysList = document.querySelectorAll('.day-box');
    const lists = [...availableWorkoutsGrid, ...daysList];

    const attachEventListeners = (list) => {
        list.addEventListener('dragstart', (e) => handleDragStart(e, list));
        list.addEventListener('dragover', (e) => handleDragOver(e, list));
        list.addEventListener('drop', (e) => handleDrop(e, list));
        list.addEventListener('dragend', (e) => handleDragEnd(e));
    };

    const dayGrid = document.querySelector('.top-section');
    dayGrid.addEventListener('dragleave', (e) => handleDragLeave(e));

    lists.forEach(attachEventListeners);
})