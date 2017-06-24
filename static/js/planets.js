$(document).ready(function(){
    $(".residents").click(function(){
        $("#attributes").empty();
        $("#myModal").modal("toggle");
        var residentURL = $(this).attr("data-resident-url").split(",")
        $.each(residentURL, function(index, value){
            $.ajax({
                dataType: "json",
                url: value,
                success: function(residentData) {
                    var attributes = residentData
                    var personalData = "<tr>";
                    $.each(attributes, function (key, value) {
                        if (key === "homeworld") {
                            return false;
                        }
                        personalData += '<td>' + value + '</td>';
                    });
                    $("#attributes").append(personalData + '</tr>');
                },
            });
        });
    });
});



