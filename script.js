document.getElementById('locationForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const latitude = document.getElementById('latitude').value;
    const longitude = document.getElementById('longitude').value;
    const date = document.getElementById('date').value;

    fetch(`/examine/${latitude}/${longitude}/${date}`)
        .then(response => response.json())
        .then(data => {
            // Option 1: Redirect to another page with query parameters
            //window.location.href = `/results?analysis=${encodeURIComponent(data.analysis)}`;

            // Option 2: Display the result on the same page (comment out the above line if using this option)
             document.body.innerHTML += `<h1>Chlorophyll</h1>: <p>${data.Chlorophyll}</p><br><h1>DaytimeSST</h1>: <p>${data.DaytimeSST}</p><br><h1>NighttimeSST</h1>: <p>${data.NighttimeSST}</p><br><h1>DaytimeSST</h1>: <p>${data.NighttimeSST}</p><br><h1>Analysis</h1>: <p>${data.Analysis}</p>`;
        })
        .catch(error => console.error('Error:', error));
});