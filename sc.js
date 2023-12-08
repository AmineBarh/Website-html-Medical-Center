// Function to toggle the visibility of the task list
        function SeeAllTasks() {
            var taskList = document.getElementById('taskList');
            // Toggle display property for the task list
            taskList.style.display = (taskList.style.display === 'none' ||  taskList.style.display === '') ? 'block' : 'none';
        }

        // Function to add a new task
        function addTask() {
            var taskInput = document.getElementById('AddTask');
            var tasksList = document.getElementById('allTasks');

            // Create a new list item
            var newTask = document.createElement('li');
            newTask.textContent = taskInput.value;

            // Append the new task to the task list
            tasksList.appendChild(newTask);

            // Clear the input field after adding the task
            taskInput.value = '';

            // Show the task list when a task is added
            document.getElementById('taskList').style.display = 'block';
        }
        var timer; // Variable to hold the timer interval
    var seconds = 0;
    var minutes = 0;
    var hours = 0;

    function startTimer() {
        timer = setInterval(updateTimer, 1000); // Update the timer every second
    }

    function stopTimer() {
        clearInterval(timer); // Stop the timer
    }

    function resetTimer() {
        stopTimer();
        seconds = 0;
        minutes = 0;
        hours = 0;
        updateTimerDisplay();
    }

    function updateTimer() {
        seconds++;
        if (seconds === 60) {
            seconds = 0;
            minutes++;
            if (minutes === 60) {
                minutes = 0;
                hours++;
            }
        }
        updateTimerDisplay();
    }

    function updateTimerDisplay() {
        var formattedTime =
            padNumber(hours) + ':' + padNumber(minutes) + ':' + padNumber(seconds);
        document.getElementById('timerDisplay').textContent = formattedTime;
    }

    function padNumber(number) {
        return number < 10 ? '0' + number : number;
    }