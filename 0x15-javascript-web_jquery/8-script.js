$(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      data.results.forEach((mov) => {
        $('UL#list_movies').append(`<li>${mov.title}</li>`);
      });
    },
  });
});
