$(document).ready(function () {
    $("#exampleModal").on("show.bs.modal", function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var recipient = button.data("whatever"); // Extract info from data-* attributes
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        var modal = $(this);
        for (let item of city_info) {
            if (item.name == recipient) {
                var average_income = item.average_income;
                //var education_level = "{{ collection.city.education_level|escapejs }}";
                var postgraduate_percentage = item.postgraduate_percentage;
                var migration_percentage = item.migration_percentage;
                var migration_number = item.migration_number;
            }
        }
        modal.find(".modal-title").text(recipient);
        document.getElementById("Average Income:").innerHTML = "$"+ average_income;
        document.getElementById("Postgraduate Percentage: ").innerHTML =
            parseFloat(postgraduate_percentage).toFixed(2) + "%";
        document.getElementById("Migration Percentage: ").innerHTML =
            parseFloat(migration_percentage).toFixed(2) + "%";
        document.getElementById("Migration Number: ").innerHTML = migration_number;
        infoWindow.close();
    });
});
