// Responds to the mouse-in event on a map shape (library).
// type of 'e': google.maps.MouseEvent
function mouseInToRegion(e) {
    // set the hover library so the setStyle function can change the border
    e.feature.setProperty("state", "hover");
    var percent = e.feature.getProperty("percent_variable");
    showInfoWindow(e);

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