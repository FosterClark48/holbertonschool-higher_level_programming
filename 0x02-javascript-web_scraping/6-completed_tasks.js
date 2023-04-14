#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

// Import request module
const request = require('request');
// Get API URL from CL and store in url variable
const url = process.argv[2];

// Make request to API URL with a callback function
request(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  // Parse JSON response body
  const tasks = JSON.parse(body);
  // Initialize empty object to store the count of completed tasks per user
  const tasksCompleted = {};

  // Iterate through each task in the tasks array
  tasks.forEach(task => {
    if (task.completed) {
      // If the user ID is not already in tasksCompleted, set the initial count to 1
      if (tasksCompleted[task.userId] === undefined) {
        tasksCompleted[task.userId] = 1;
      } else {
        // If the user ID is already in tasksCompleted, increment the count by 1
        tasksCompleted[task.userId] += 1;
      }
    }
  });
  // Print the tasksCompleted object with the user IDs and their respective completed task count
  console.log(tasksCompleted);
});
