var map;
var infoWindow;
var percent_array = ["0", "0", "0", "0", "0"];
var percentMin = Number.MAX_VALUE,
    percentMax = -Number.MAX_VALUE;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: {
            lat: -37.327732,
            lng: 144.317647,
        },
        zoom: 9,
        mapTypeId: "roadmap",
        disableDefaultUI: true,
        styles: google_map_style,
        gestureHandling: "greedy",
    });
    // set up the style rules and events for google.maps.Data
    map.data.setStyle(styleFeature);

    // load polygon GeoJson
    map.data.addGeoJson(city_coordinates, { idPropertyName: "city_id" });
    /* map.data.addGeoJson(victoria, {
        idPropertyName: "vic_lga__3",
    }); */

    map.data.addListener("mouseover", mouseInToRegion);
    //map.data.addListener("mouseover", showInfoWindow);
    map.data.addListener("mouseout", mouseOutOfRegion);

    // initialize the info window
    infoWindow = new google.maps.InfoWindow();
    map.data.addListener("click", showInfoWindow);

    // wire up the button
    var selectBox = document.getElementById("census-variable");
    google.maps.event.addDomListener(selectBox, "change", function () {
        clearCensusData();
        loadCensusData(selectBox.options[selectBox.selectedIndex].value);
    });

    // load data for the
    loadPercentData();
}

/** Removes census data from each shape on the map and resets the UI. */
function clearCensusData() {
    percentMin = Number.MAX_VALUE;
    percentMax = -Number.MAX_VALUE;
    map.data.forEach(function (row) {
        row.setProperty("percent_variable", undefined);
    });
    document.getElementById("data-box").style.display = "none";
    document.getElementById("data-caret").style.display = "none";
}

async function loadPercentData() {
    /* for (var k = 0; k < 92; k++) {
        var percentVariable = getRndInteger(0, 100);

        var region_id = "MELBOURNE";
        // keep track of min and max values
        if (percentVariable < percentMin) {
            percentMin = percentVariable;
        }
        if (percentVariable > percentMax) {
            percentMax = percentVariable;
        }
        // update the existing row with the new data
        map.data
            .getFeatureById(region_id)
            .setProperty("percent_variable", percentVariable);
    } */
    await updatePercent();
    for (var i = 0; i < 5; i++) {
        var percentVariable = percent_array[i];
        var city_id = i;

        // keep track of min and max values
        if (percentVariable < percentMin) {
            percentMin = percentVariable;
        }
        if (percentVariable > percentMax) {
            percentMax = percentVariable;
        }

        // update the existing row with the new data
        map.data
            .getFeatureById(city_id)
            .setProperty("percent_variable", ""+percentVariable);

    }

    // update and display the legend
    document.getElementById("census-min").textContent = percentMin.toLocaleString();
    document.getElementById("census-max").textContent = percentMax.toLocaleString();
}

async function updatePercent() {

    for (i = 0; i < 5; i++) {

        percent_array[i] = getRndInteger(0, 100);
    }
}

function getCircle(magnitude) {
    var low = [204, 49, 87]; // color of smallest datum
    var high = [209, 98, 46]; // color of largest datum

    // delta represents where the value sits between the min and max
    //var delta = 0.9;
    var delta = (magnitude - percentMin) / (100);
    var color = [];
    for (var i = 0; i < 3; i++) {
        // calculate an integer color based on the delta
        color[i] = (high[i] - low[i]) * delta + low[i];
    }
    return {
        path: google.maps.SymbolPath.CIRCLE,
        fillColor: "hsl(" + color[0] + "," + color[1] + "%," + color[2] + "%)",
        fillOpacity: 0.2,
        scale: 64 + (magnitude-64)*0.5,
        strokeColor: "grey",
        strokeWeight: 0.1,
        strokeOpacity: 1.0,
    };
}

// Load the info window with necessary infomation
function showInfoWindow(e) {
    var contentString = "Good day";

    /* var contentString =
        "<b> Name: </b>" +
        e.feature.getProperty("name") +
        "<br><b> Percent: </b>" +
        //getRndInteger(0, 100).toLocaleString() +
        e.feature.getProperty("percent_variable").toLocaleString() +
        "%<br>" +
        '<a href = "/city/' +
        e.feature.getProperty("city_id") +
        '" class = "click_a" >More info</a>'; */
    
    var contentString =
        "<div style ='font-size:15; line-height: 1'> " +
        "<p class='font-weight-bold'> Name: " +
        e.feature.getProperty("name") +
        "</p>" +
        "<br><p class='font-weight-bold'> Percent: " +
        //getRndInteger(0, 100).toLocaleString() +
        e.feature.getProperty("percent_variable").toLocaleString() +
        "%</p>" +
        "<br>" +
        "<button type='button' class='btn btn-primary btn-sm btn-block' " +
        "data-toggle='modal' data-target='#exampleModal'" +
        "data-whatever='" +
        e.feature.getProperty("name") +
        "'>More Info</button>" +
        "</div>";
        /* '<a href = "/city/' +
        e.feature.getProperty("city_id") +
        '" class = "click_a" >More info</a>'; */

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
    //var delta = 0.9;
    var delta = (feature.getProperty('percent_variable') - percentMin) / (100);

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
    var magnitude = feature.getProperty('percent_variable');
    return {
        strokeWeight: outlineWeight,
        //strokeColor: "#fff",
        strokeColor: "grey",
        strokeOpacity: 0.5,
        zIndex: zIndex,
        fillColor: "hsl(" + color[0] + "," + color[1] + "%," + color[2] + "%)",
        fillOpacity: 0.15,
        icon: getCircle(magnitude),
        //visible: showRow
    };
}

// Responds to the mouse-in event on a map shape (library).
// type of 'e': google.maps.MouseEvent
function mouseInToRegion(e) {
    // set the hover library so the setStyle function can change the border
    e.feature.setProperty("state", "hover");
    var percent = e.feature.getProperty("percent_variable");

    // update the label
    /* document.getElementById("data-label").textContent = e.feature.getProperty(
        "vic_lga__3"
    ); */
    document.getElementById("data-label").textContent = e.feature.getProperty(
        "name"
    ); 
    document.getElementById("data-value").textContent = percent;
    document.getElementById("data-box").style.display = "block";
    document.getElementById("data-caret").style.display = "block";
    document.getElementById("data-caret").style.paddingLeft = percent + "%";
}

// Responds to the mouse-out event on a map shape (library).
// type of 'e': google.maps.MouseEvent
function mouseOutOfRegion(e) {
    // reset the hover library, returning the border to normal
    e.feature.setProperty("state", "normal");
    // close info window display
    //infoWindow.close();
}

function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}
