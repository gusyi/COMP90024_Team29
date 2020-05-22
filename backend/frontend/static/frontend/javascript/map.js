var map;
var infoWindow;
var percent_array = ["0", "0", "0", "0", "0"];
var percentMin = Number.MAX_VALUE,
    percentMax = -Number.MAX_VALUE;

var infoWindow_exist = false; 
function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: {
            lat: -37.327732,
            lng: 144.317647,
        },
        zoom: 8.5,
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

    google.maps.event.addListener(map, "click", function (event) {
        if (infoWindow_exist == true) {
            infoWindow_exist == false;
            infoWindow.close();
        }
    });

    // wire up the button
    var selectBox = document.getElementById("census-variable");
    google.maps.event.addDomListener(selectBox, "change", function () {
        clearData();
        loadCensusData(selectBox.options[selectBox.selectedIndex].value);
    });

    // load data for the
    loadPercentData();
}

/** Removes data from each shape on the map and resets the UI. */
function clearData() {
    percentMin = Number.MAX_VALUE;
    percentMax = -Number.MAX_VALUE;
    map.data.forEach(function (row) {
        row.setProperty("percent_variable", undefined);
    });
    document.getElementById("data-box").style.display = "none";
    document.getElementById("data-caret").style.display = "none";
}

async function loadPercentData() {

    //await updatePercent();
    for (let item of city_info) {
        var percentVariable = parseInt(item.percent);
        var city_id = item.city_id;

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

    /* for (var i = 0; i < 5; i++) {
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
    } */

    // update and display the legend
    document.getElementById("census-min").textContent = percentMin.toLocaleString();
    document.getElementById("census-max").textContent = percentMax.toLocaleString();
}

/* async function updatePercent() {
    for (i = 0; i < 5; i++) {
        if (percent_array[i] == "0")
            percent_array[i] = getRndInteger(0, 100);
    }
} */

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
        fillOpacity: 0.7,
        scale: 100 + (magnitude-66)*0.5,
        strokeColor: "grey",
        strokeWeight: 0.1,
        strokeOpacity: 1.0,
    };
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

