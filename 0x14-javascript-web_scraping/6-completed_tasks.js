#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasks = todos.filter((todo) => todo.completed);

  const taskCountPerUser = {};

  completedTasks.forEach((todo) => {
    const userId = todo.userId;
    if (taskCountPerUser[userId]) {
      taskCountPerUser[userId]++;
      return;
    }
    taskCountPerUser[userId] = 1;
  });

  console.log(taskCountPerUser);
});
