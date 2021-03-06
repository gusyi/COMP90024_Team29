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



// Load the info window with necessary infomation
function showInfoWindow(e) {


    var contentString =
        "<div style ='font-size:15; line-height: 1'> " +
        "<h3 class='font-weight-bold'>" +
        e.feature.getProperty("name") +
        "</h3>" +
        "<br><p class='font-weight-bold'> Realtime Approval Rate: " +
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


    infoWindow_exist = true;
    // Replace the info window's content and position.
    infoWindow.setContent(contentString);
    infoWindow.setPosition(e.latLng);
    infoWindow.open(map);
}