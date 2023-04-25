// Add a function to create a circle for each event location
function createCircles(map) {
    // Use Django template tag to directly pass the events data into the JavaScript code
    const events = window.events;
    console.log(events)
    events.forEach(event => {
        const circle = new google.maps.Circle({
            strokeColor: "#e7b10a",
            strokeOpacity: 0.8,
            strokeWeight: 2,
            fillColor: "#01a250",
            fillOpacity: 0.35,
            map,
            center: {
                lat: parseFloat(event.locationId__latitude),
                lng: parseFloat(event.locationId__longitude),
            },
            radius: parseFloat(event.locationId__radius) * 1000, // Convert to meters if the radius is in kilometers
        });

        // Add an event listener for click events on each circle
        circle.addListener("click", () => {
            const trashName = event.trashId__name;
            const locationName = event.locationId__buildingName;
            const status = event.status;

            const message = `
            <div style="text-align: center">
                <h2 style="font-weight: bold">Event Details</h2>
                <p style="font-weight: bold">Trash: ${trashName}</p>
                <p style="font-weight: bold">Location: ${locationName}</p>
                <p style="font-weight: bold">Status: ${status}</p>
                <button id="ok-button" style="margin-top: 16px">OK</button>
            </div>
            `;

            const overlay = document.createElement("div");
            overlay.style.position = "fixed";
            overlay.style.top = 0;
            overlay.style.left = 0;
            overlay.style.width = "100%";
            overlay.style.height = "100%";
            overlay.style.backgroundColor = "rgba(0, 0, 0, 0.5)";
            overlay.style.display = "flex";
            overlay.style.alignItems = "center";
            overlay.style.justifyContent = "center";

            const dialog = document.createElement("div");
            dialog.style.backgroundColor = "white";
            dialog.style.padding = "16px";
            dialog.innerHTML = message;

            overlay.appendChild(dialog);
            document.body.appendChild(overlay);

            const okButton = document.getElementById("ok-button");
            okButton.addEventListener("click", () => {
            document.body.removeChild(overlay);
            });
        });
    });
}

// Initialize and add the map
function initMap() {

    // The map, centered at user's current location
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        disableDefaultUI: true,
        fullscreenControl: true,
    });

    // Try HTML5 geolocation
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const userLocation = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                };
                // Set the center of the map to the user's current location
                map.setCenter(userLocation);


                // Add a marker at the user's current location
                const marker = new google.maps.Marker({
                    position: userLocation,
                    map: map,
                });
            },
            () => {
                // If the user denies geolocation permission, center the map on a default location
                const exeter = { lat: 50.735529873, lng: -3.5345781864 };
                map.setCenter(exeter);
                const marker = new google.maps.Marker({
                    position: exeter,
                    map: map,
                });
            }
        );
    } else {
        // Browser doesn't support geolocation, center the map on a default location
        const exeter = { lat: 50.735529873, lng: -3.5345781864 };
        map.setCenter(exeter);
        const marker = new google.maps.Marker({
            position: exeter,
            map: map,
        });
    }

    createCircles(map);
}

window.initMap = initMap; // Assign the initMap function to the window object here