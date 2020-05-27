var city_apex;
var approval_rate_array=[];
$(document).ready(function () {
    $("#exampleModal").on("show.bs.modal", function (event) {
        // Button that triggered the modal
        var button = $(event.relatedTarget); 

         // Extract info from data-* attributes
        var recipient = button.data("whatever");

        // Update the modal's content. We'll use jQuery here, 
        //   but you could use a data binding library or other methods instead.
        var modal = $(this);

        // extract information relate to this city from local 
        for (let item of city_info) {
            if (item.name == recipient) {
                var average_income = item.average_income;
                //var education_level = "{{ collection.city.education_level|escapejs }}";
                var postgraduate_percentage = item.postgraduate_percentage;
                var migration_percentage = item.migration_percentage;
                var migration_number = item.migration_number;
                city_apex = item.city_id;
                //console.log(city_apex);
                //console.log(approval_rate_matrix[city_apex]);      

                // Put all the approval rates to the array for display
                approval_rate_array = [];
                for (let i = 0; i < approval_rate_matrix[city_apex].length; i++) {
                    const element = approval_rate_matrix[city_apex][i];
                    if (element["y"] != 100 && element["y"] != 0) {
                        approval_rate_array.push({
                        x: element["x"],
                        y: Number(element["y"]),
                        });
                    }
                    
                }
                //console.log(approval_rate_array);
                
            }
        }

        // Display financial, educational data to the header of the modal
        modal.find(".modal-title").text(recipient);
        document.getElementById("Average Income:").innerHTML = "$"+ average_income;
        document.getElementById("Postgraduate Percentage: ").innerHTML =
            parseFloat(postgraduate_percentage).toFixed(2) + "%";
        document.getElementById("Migration Percentage: ").innerHTML =
            parseFloat(migration_percentage).toFixed(2) + "%";
        document.getElementById("Migration Number: ").innerHTML = migration_number;
        infoWindow.close();
        options.series[0].data = approval_rate_array;
        //console.log(options.series[0].data);

        // Draw the ApexChart
        var chart = new ApexCharts(document.querySelector("#chart"), options);
        chart.render();
    });
});


$(document).ready(function () {
    $(".vertical").on("click", function () {
        button_value = $(this).val();
    });
});