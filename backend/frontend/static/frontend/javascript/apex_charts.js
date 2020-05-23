var options = {
    series: [
        {
            name: "Approval Rate",
            //data: [approval_rate_matrix[city_apex]],
            //data: [approval_rate_array],
            data: [{ x: '05/06/2014', y: 54 }, { x: '05/08/2014', y: 17 } , { x: '05/28/2014', y: 26 }],
        },
    ],
    chart: {
        type: "area",
        stacked: false,
        height: 350,
        zoom: {
            type: "x",
            enabled: true,
            autoScaleYaxis: true,
        },
        toolbar: {
            autoSelected: "zoom",
        },
    },
    dataLabels: {
        enabled: false,
    },
    markers: {
        size: 0,
    },
    title: {
        text: "Approval Rate Movement",
        align: "left",
    },
    fill: {
        type: "gradient",
        gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.5,
            opacityTo: 0,
            stops: [0, 90, 100],
        },
    },
    yaxis: {
        labels: {
            formatter: function (val) {
                return (val).toFixed(0);
            },
        },
        title: {
            text: "Percentage",
        },
    },
    xaxis: {
        type: "datetime",
    },
    tooltip: {
        shared: false,
        y: {
            formatter: function (val) {
                return (val).toFixed(0);
            },
        },
    },
};

/* var options = {
    series: [
        {
            name: "XYZ MOTORS",
            data: [{ x: '05/06/2014', y: 54 }, { x: '05/08/2014', y: 17 } , { x: '05/28/2014', y: 26 }],
        },
    ],
    chart: {
        type: "area",
        stacked: false,
        height: 350,
        zoom: {
            type: "x",
            enabled: true,
            autoScaleYaxis: true,
        },
        toolbar: {
            autoSelected: "zoom",
        },
    },
    dataLabels: {
        enabled: false,
    },
    markers: {
        size: 0,
    },
    title: {
        text: "Stock Price Movement",
        align: "left",
    },
    fill: {
        type: "gradient",
        gradient: {
            shadeIntensity: 1,
            inverseColors: false,
            opacityFrom: 0.5,
            opacityTo: 0,
            stops: [0, 90, 100],
        },
    },
    yaxis: {
        labels: {
            formatter: function (val) {
                return (val / 1000000).toFixed(0);
            },
        },
        title: {
            text: "Price",
        },
    },
    xaxis: {
        type: "datetime",
    },
    tooltip: {
        shared: false,
        y: {
            formatter: function (val) {
                return (val / 1000000).toFixed(0);
            },
        },
    },
}; */

/* var options = {
    series: [
        {
            name: "Desktops",
            data: [10, 41, 35, 51, 49, 62, 69, 91, 148],
        },
    ],
    chart: {
        height: 350,
        type: "line",
        zoom: {
            enabled: false,
        },
    },
    dataLabels: {
        enabled: false,
    },
    stroke: {
        curve: "straight",
    },
    title: {
        text: "Product Trends by Month",
        align: "left",
    },
    grid: {
        row: {
            colors: ["#f3f3f3", "transparent"], // takes an array which will be repeated on columns
            opacity: 0.5,
        },
    },
    xaxis: {
        categories: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
        ],
    },
}; */