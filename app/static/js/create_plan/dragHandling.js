let draggedItem = null;
let placeholder = null;

export function handleDragStart(e, list) {
    if (e.target.classList.contains('drag-item')) {
        draggedItem = e.target;
        setTimeout(() => {
            e.target.style.opacity = list.classList.contains('drop-list') ? '0' : '0.5';
        }, 0);
    }
}

// Helper function to handle dragend
export function handleDragEnd(e) {
    draggedItem.style.opacity = '1'; // Reset opacity
}

// Helper function for dragover
export function handleDragOver(e, list){
    e.preventDefault();
    if (sourceList() !== list && !list.classList.contains('drag-list')) {
        const children = [...list.children];
        const closest = children.find(child => child.getBoundingClientRect().top > e.clientY);
        if(!placeholder) { //Add only one placeholder
            placeholder = document.createElement('div');
            placeholder.classList.add('custom-placeholder');

            const width = list.children[0].offsetWidth;
            const height = draggedItem.offsetHeight;

            placeholder.style.width = `${width}px`;
            placeholder.style.height = `${height}px`;
        }
        if (closest) {
            list.insertBefore(placeholder, closest); // Insert placeholder before closest item
        }
        else {
            list.appendChild(placeholder); // Append placeholder to the end
        }
    }
}

// Helper function for drop
export function handleDrop(e, list){
  e.preventDefault();
  draggedItem.style.opacity = '1';

  if (sourceList() !== list && !list.classList.contains('drag-list')) {
    const newItem = draggedItem.cloneNode(true); // Clone the dragged item
    list.insertBefore(newItem, placeholder); // Insert the new item at the correct position
  }

  if (sourceList().classList.contains('drop-list')) {
      draggedItem.parentNode.removeChild(draggedItem); // Remove the original item from the source list
  }
  placeholder.remove(); // Remove placeholder
}

export function handleDragLeave(e) {
    placeholder.remove();
    placeholder = null;
    console.log(e.target.offsetWidth);
}

function sourceList() {
    return draggedItem.parentNode;
}
