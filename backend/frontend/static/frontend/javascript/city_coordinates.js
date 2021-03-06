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



// coordinates of cities
var city_coordinates = {
    type: "FeatureCollection",
    features: [
        {
            type: "Feature",
            geometry: {
                type: "Point",
                coordinates: [144.960958, -37.799748],
            },
            properties: {
                name: "Melbourne",
                city_id: "0",
            },
        },
        {
            type: "Feature",
            geometry: {
                type: "Point",
                coordinates: [144.361733, -38.149988],
            },
            properties: {
                name: "Geelong",
                city_id: "1",
            },
        },
        {
            type: "Feature",
            geometry: {
                type: "Point",
                coordinates: [143.850336, -37.561172],
            },
            properties: {
                name: "Ballarat",
                city_id: "2",
            },
        },
        {
            type: "Feature",
            geometry: {
                type: "Point",
                coordinates: [144.279946, -36.756719],
            },
            properties: {
                name: "Bendigo",
                city_id: "3",
            },
        },
       /*  {
            type: "Feature",
            geometry: {
                type: "Point",
                coordinates: [144.577877, -37.680519],
            },
            properties: {
                name: "Melton",
                city_id: "4",
            },
        }, */
    ],
};

// information structure of the local info matrix 
var city_info = [
    {
        name: "Melbourne",
        city_id: "0",
        percent: "0",
        average_income: "0",
        education_level: "0",
        postgraduate_percentage: "0",
        migration_percentage: "0",
        migration_number: "0",
        flag: "0",
        tweet_counts: "0",
    },
    {
        name: "Geelong",
        city_id: "1",
        percent: "0",
        average_income: "0",
        education_level: "0",
        postgraduate_percentage: "0",
        migration_percentage: "0",
        migration_number: "0",
        flag: "0",
        tweet_counts: "0",
    },
    {
        name: "Ballarat",
        city_id: "2",
        percent: "0",
        average_income: "0",
        education_level: "0",
        postgraduate_percentage: "0",
        migration_percentage: "0",
        migration_number: "0",
        flag: "0",
        tweet_counts: "0",
    },
    {
        name: "Bendigo",
        city_id: "3",
        percent: "0",
        average_income: "0",
        education_level: "0",
        postgraduate_percentage: "0",
        migration_percentage: "0",
        migration_number: "0",
        flag: "0",
        tweet_counts: "0",
    },
];

var city_names = ["Melbourne", "Geelong", "Ballarat", "Bendigo"];

// stores days of approval rates for cities
var approval_rate_matrix = [[], [], [], []];

// Transform date info to the correct format
function formatCourseDate(date) {
    const dateObj = new Date(date + "T00:00:00");
    return new Intl.DateTimeFormat("en-US").format(dateObj);
}

var week_day = [0, 0, 0, 0]; 
var weekly_total = [0, 0, 0, 0];