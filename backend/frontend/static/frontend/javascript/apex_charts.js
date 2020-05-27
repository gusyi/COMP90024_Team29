// configuration for ApexChart
var options = {
    series: [
        {
            name: "Approval Rate",
            //data: [approval_rate_matrix[city_apex]],
            //data: [approval_rate_array],
            //data: [{ x: '05/06/2014', y: 54 }, { x: '05/08/2014', y: 17 } , { x: '05/28/2014', y: 26 }],
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
                return val.toFixed(0);
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
                return val.toFixed(0);
            },
        },
    },
    annotations: {
        xaxis: [
            {
                x: new Date("20 Dec 2019").getTime(),
                x2: new Date('27 Dec 2019').getTime(),
                borderColor: "#000",
                fillColor: "#FEB019",
                label: {
                    text: "Hawaii Holiday",
                },
            },
        ],
    },
    stroke: {
        width: 1.5,
    },
};