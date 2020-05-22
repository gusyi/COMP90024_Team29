// Load the info window with necessary infomation
function showInfoWindow(e) {
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

    infoWindow_exist = true;
    // Replace the info window's content and position.
    infoWindow.setContent(contentString);
    infoWindow.setPosition(e.latLng);
    infoWindow.open(map);
}