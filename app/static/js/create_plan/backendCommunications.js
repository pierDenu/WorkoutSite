async function getWorkoutById(workout_id) {
    try {
        const response = await fetch(`/workout-data-by-id/${workout_id}`);
        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        const workout = await response.json();
        return workout;
    } catch (error) {
        console.error('Error fetching workout:', error);
        // Можна повернути спеціальне значення або інформацію про помилку
        return { error: error.message };
    }
}
