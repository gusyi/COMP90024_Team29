/* # ====================================
# COMP90024 Cluster and Cloud Computing - Assignment 2
# Group 29
# Hongwei Yin 901012
# Cheng Sun 900806
# Xinyi Xu 900966
# Yiran Yao 1144268
# Xiaotao Tan 1032950
# ====================================
 */



var map;
var infoWindow;

// value of the buttons on the upper right corner menu
var button_value = document.getElementById("dropdown");
var percent_array = ["0", "0", "0", "0", "0"];
var percentMin = Number.MAX_VALUE,
    percentMax = -Number.MAX_VALUE,
    variableMin = Number.MAX_VALUE,
    variableMax = -Number.MAX_VALUE;
var input_variable; 
var flag = 0; 

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

    map.data.addListener("mouseover", mouseInToRegion);
    map.data.addListener("mouseout", mouseOutOfRegion);

    // initialize the info window
    infoWindow = new google.maps.InfoWindow();
    map.data.addListener("click", showInfoWindow);

    // close the info window when clicked outside of the circle
    google.maps.event.addListener(map, "click", function (event) {
        if (infoWindow_exist == true) {
            infoWindow_exist == false;
            infoWindow.close();
        }
    });

    // wire up the button
    // when clicking the buttons on the menu, display new set of data
    google.maps.event.addDomListener(button_value, "click", function () {
        flag = 1;     
        //console.log(button_value);
        clearData();
        loadData();
    });

    // load data of the map 
    loadData();
}

/** Removes data from each shape on the map and resets the UI. */
function clearData() {
    percentMin = Number.MAX_VALUE;
    percentMax = -Number.MAX_VALUE;
    variableMin = Number.MAX_VALUE;
    variableMax = -Number.MAX_VALUE;
    document.getElementById("data-box").style.display = "none";
    document.getElementById("data-caret").style.display = "none";
}

// load data of the map 
async function loadData() {


    for (let item of city_info) {
        var percentVariable = parseInt(item.percent);
        var city_id = item.city_id;

        // the default value of the map 
        if (flag == 0) {
            input_variable = Math.sqrt(parseInt(item.tweet_counts));
        } 

        // depending on the menu button pressed, replace data 
        switch (button_value) {
            case "tweet_counts":
                input_variable = Math.sqrt(parseInt(item.tweet_counts));
                break;
            case "average_income":
                input_variable = parseInt(item.average_income);
                break;
            case "postgraduate_percentage":
                input_variable = parseInt(parseFloat(item.postgraduate_percentage) * 100);
                break;
            case "migration_percentage":
                input_variable = parseInt(parseFloat(item.migration_percentage) * 100);
                break;
            case "migration_number":
                input_variable = parseInt(item.migration_number);
                break;
        }

        //console.log(item.name+"   " + input_variable);    
        //console.log("tweets:" + tweet_counts + "  " + Math.sqrt(tweet_counts));

        // keep track of min and max values
        if (percentVariable < percentMin) {
            percentMin = percentVariable;
        }
        if (percentVariable > percentMax) {
            percentMax = percentVariable;
        }

        // keep track of min and max values
        if (input_variable < variableMin) {
            variableMin = input_variable;
        }
        if (input_variable > variableMax) {
            variableMax = input_variable;
        }

        // update the existing row with the new data
        map.data
            .getFeatureById(city_id)
            .setProperty("percent_variable", "" + percentVariable);
        map.data
            .getFeatureById(city_id)
            .setProperty("input_variable", "" + input_variable);
    }

    // update and display the legend
    document.getElementById("census-min").textContent = percentMin.toLocaleString();
    document.getElementById("census-max").textContent = percentMax.toLocaleString();
}

// set the style feature of hte circle
function getCircle(approval_rate, magnitude) {
    var low = [204, 49, 87]; // color of smallest datum
    var high = [209, 98, 46]; // color of largest datum


    var delta = (approval_rate - percentMin) / (percentMax - percentMin);
    var color = [];
    for (var i = 0; i < 3; i++) {
        // calculate an integer color based on the delta
        color[i] = (high[i] - low[i]) * delta + low[i];
    }

    return {
        path: google.maps.SymbolPath.CIRCLE,
        fillColor: "hsl(" + color[0] + "," + color[1] + "%," + color[2] + "%)",
        fillOpacity: 0.7,
        scale:
            50 + ((magnitude - (variableMin*0.9)) / (variableMax * 1.1 - variableMin)) * 50,
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

    var outlineWeight = 0.5,
        zIndex = 1;
    if (feature.getProperty("state") === "hover") {
        outlineWeight = zIndex = 2;
    }
    var approval_rate = feature.getProperty('percent_variable');
    var magnitude = feature.getProperty('input_variable');
    return {
        strokeWeight: outlineWeight,
        //strokeColor: "#fff",
        strokeColor: "grey",
        strokeOpacity: 0.5,
        zIndex: zIndex,
        fillColor: "hsl(" + color[0] + "," + color[1] + "%," + color[2] + "%)",
        fillOpacity: 0.15,
        icon: getCircle(approval_rate, magnitude),
        //visible: showRow
    };
}