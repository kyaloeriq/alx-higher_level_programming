#!/usr/bin/node
const request = require('request');

function countCompletedTasks (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Failed to fetch data from the API:', error);
      return;
    }

    if (response.statusCode !== 200) {
      console.error('Failed to fetch data from the API:', body);
      return;
    }

    const todos = JSON.parse(body);
    // Object to store user ids and their completed task counts
    const userCompletedTasks = {};

    // Looping through todos to count completed tasks for each user
    todos.forEach(todo => {
      if (todo.completed) {
        const userId = todo.userId;
        userCompletedTasks[userId] = (userCompletedTasks[userId] || 0) + 1;
      }
    });

    // Printing users with completed tasks and their counts
    console.log(JSON.stringify(userCompletedTasks, null, 2));
  });
}

const apiUrl = process.argv[2];
countCompletedTasks(apiUrl);
