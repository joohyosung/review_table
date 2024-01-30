window.initMap = function () {
    const map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: 37.55474, lng: 126.9706 },
      zoom: 15,
    });
  };
  const API_KEY = config.apikey