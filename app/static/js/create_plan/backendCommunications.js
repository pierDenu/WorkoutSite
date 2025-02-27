export async function searchWorkouts() {
    const name = document.getElementById("search-workout").value;
    const response = await
        fetch(`/plans/search-workouts-by-name?name=${encodeURIComponent(name)}`);
    const html = await response.text();
    document.getElementById("workout-list").innerHTML = html;
}

export async function savePlan(dropLists, planName){
    let data = {plan_name: planName};
    const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
    days.forEach((day) => {
        data[day]  = {}
        const list = document.getElementById(day);
        const elements = list.querySelectorAll('li');
        let order = 1;
        elements.forEach((element) => {
            const workoutId = element.getAttribute("data-workout-id");
            data[day][order] = workoutId;
            order++;
        });
    });
    const result = await postJSONData("/plans/save", data);
    console.log("Success:", result);
}

async function postJSONData(url, data) {
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        return await response.json();  // Return parsed JSON result
    } catch (error) {
        console.error("Error:", error);
        throw error;  // Re-throw so caller can handle it if needed
    }
}
