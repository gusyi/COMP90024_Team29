var map;
var infoWindow;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: {
            lat: -37.327732,
            lng: 144.317647,
        },
        zoom: 9,
        mapTypeId: "roadmap",
        streetViewControl: false,
        mapTypeControl: false,
        styles: google_map_style,
        //styles: css
    });

    // set up the style rules and events for google.maps.Data
    map.data.setStyle(styleFeature);

    // load polygon GeoJson
    map.data.addGeoJson(city_coordinates);
    map.data.addGeoJson(victoria);

    map.data.addListener("mouseover", mouseInToRegion);
    //map.data.addListener("mouseover", showInfoWindow);
    map.data.addListener("mouseout", mouseOutOfRegion);

    // initialize the info window
    infoWindow = new google.maps.InfoWindow();
    //map.data.addListener("click", showInfoWindow);
}

function getCircle(magnitude) {
    var low = [204, 49, 87]; // color of smallest datum
    var high = [209, 98, 46]; // color of largest datum

    // delta represents where the value sits between the min and max
    var delta = 0.9;

    var color = [];
    for (var i = 0; i < 3; i++) {
        // calculate an integer color based on the delta
        color[i] = (high[i] - low[i]) * delta + low[i];
    }
    return {
        path: google.maps.SymbolPath.CIRCLE,
        fillColor: "hsl(" + color[0] + "," + color[1] + "%," + color[2] + "%)",
        fillOpacity: 0.2,
        scale: Math.pow(2, magnitude) / 2,
        strokeColor: "grey",
        strokeWeight: 0.1,
        strokeOpacity: 1.0,
    };
}

// Load the info window with necessary infomation
function showInfoWindow(e) {
    var contentString = "Good day";

    //e.feature.setProperty('lib_id', 'hover');

    // Replace the info window's content and position.
    infoWindow.setContent(contentString);
    infoWindow.setPosition(e.latLng);
    infoWindow.open(map);
}

// Applies a gradient style based on the 'percent_variable' column.
// This is the callback passed to data.setStyle() and is called for each row in
// the data set.  Check out the docs for Data.StylingFunction.
// type of 'feature': google.maps.Data.Feature
function styleFeature(feature) {
    var low = [204, 49, 87]; // color of smallest datum
    var high = [209, 98, 46]; // color of largest datum

    // delta represents where the value sits between the min and max
    var delta = 0.9;

    var color = [];
    for (var i = 0; i < 3; i++) {
        // calculate an integer color based on the delta
        color[i] = (high[i] - low[i]) * delta + low[i];
    }

    // determine whether to show this shape or not
    /* var showRow = true;
    if (feature.getProperty('percent_variable') == null ||
        isNaN(feature.getProperty('percent_variable'))) {
        showRow = false;
    } */

    var outlineWeight = 0.5,
        zIndex = 1;
    if (feature.getProperty("state") === "hover") {
        outlineWeight = zIndex = 2;
    }
    var magnitude = 7;
    return {
        strokeWeight: outlineWeight,
        //strokeColor: "#fff",
        strokeColor: "grey",
        strokeOpacity: 0.5,
        zIndex: zIndex,
        fillColor: "white",
        fillOpacity: 0.1,
        icon: getCircle(magnitude),
        //visible: showRow
    };
}

// Responds to the mouse-in event on a map shape (library).
// type of 'e': google.maps.MouseEvent
function mouseInToRegion(e) {
    // set the hover library so the setStyle function can change the border
    e.feature.setProperty("state", "hover");
}
// Responds to the mouse-out event on a map shape (library).
// type of 'e': google.maps.MouseEvent
function mouseOutOfRegion(e) {
    // reset the hover library, returning the border to normal
    e.feature.setProperty("state", "normal");
    // close info window display
    infoWindow.close();
}
