import { handleDragStart, handleDragOver, handleDrop, handleDragEnd, handleDragLeave } from './dragHandling.js';
import {savePlan, searchWorkouts} from "./backendCommunications.js";

document.addEventListener('DOMContentLoaded', function () {
    const dragLists = document.querySelectorAll('.drag-list');
    const dropLists = document.querySelectorAll('.drop-list');
    const lists = [...dragLists, ...dropLists];

    const attachEventListeners = (list) => {
        list.addEventListener('dragstart', (e) => handleDragStart(e, list));
        list.addEventListener('dragover', (e) => handleDragOver(e, list));
        list.addEventListener('drop', (e) => handleDrop(e, list));
        list.addEventListener('dragend', (e) => handleDragEnd(e));
    };

    dropLists.forEach((list) => {
        list.addEventListener('dragleave', (e) => handleDragLeave(e));
    });

    lists.forEach(attachEventListeners);

    const submissionForm = document.getElementById("plan-name-form");
    let input = document.getElementById("plan-name-input");
    submissionForm.addEventListener('submit', (event) => {
        event.preventDefault();
        savePlan(dropLists, input.value)
    });

    document.getElementById("search-workout").addEventListener('input',() => {
        searchWorkouts()});
})
