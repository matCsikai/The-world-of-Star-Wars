$(document).ready(function(){
    $("#residents").click(function(){
        $("#myModal").modal("toggle");
        $.ajax({
            dataType: "json",
            url: "http://swapi.co/api/planets/",
            success: function(planetData) {
                var planetResidents = (planetData["results"])[0].residents;
                $.each( planetResidents, function(index, value) {
                    console.log(value)
                    $.ajax({
                        dataType: "json",
                        url: value,
                        success: function(residentData) {
                            debugger;
                            var attributes = residentData
                            console.log(attributes);
                            $("#name").append(attributes["name"]);
                            $("#height").append(attributes["height"]);
                            
                        },
                    });
                });
        
            },
        });
    });
});
