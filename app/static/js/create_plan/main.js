import { handleDragStart, handleDragOver, handleDrop, handleDragEnd } from './dragHandling.js';

document.addEventListener('DOMContentLoaded', function () {
    const availableWorkoutsGrid = document.querySelectorAll('.workouts-grid');
    const daysList = document.querySelectorAll('.day-box');
    const lists = [...availableWorkoutsGrid, ...daysList];

    const attachEventListeners = (list) => {
        list.addEventListener('dragstart', (e) => handleDragStart(e, list));
        list.addEventListener('dragover', (e) => handleDragOver(e, list));
        list.addEventListener('drop', (e) => handleDrop(e, list));
        list.querySelectorAll('.list-item').forEach(item => {
            item.addEventListener('dragend', (e) => handleDragEnd(e, draggedItem));
        });
        list.addEventListener('dragleave', (e) => {
            // let placeholder = document.querySelector('.placeholder');
            // placeholder.remove();
        }); // Remove placeholder when leaving the list
    };

    lists.forEach(attachEventListeners);
})