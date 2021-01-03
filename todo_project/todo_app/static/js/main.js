window.onload = function () {
    bootlint.showLintReportForCurrentDocument([], {
        hasProblems: false,
        problemFree: false
    });

    $('[data-toggle="tooltip"]').tooltip();

    function formatDate(date) {
        return (
            date.getDate() +
            "/" +
            (date.getMonth() + 1) +
            "/" +
            date.getFullYear()
        );
    }

    var currentDate = formatDate(new Date());

    $(".due-date-button").datepicker({
        format: "dd/mm/yyyy",
        autoclose: true,
        todayHighlight: true,
        startDate: currentDate,
        orientation: "bottom right"
    });

    $(".due-date-button").on("click", function (event) {
        $(".due-date-button")
            .datepicker("show")
            .on("changeDate", function (dateChangeEvent) {
                $(".due-date-button").datepicker("hide");
                $(".due-date-label").text(formatDate(dateChangeEvent.date));
            });
    });

    $("#add-todo").click(function () {
        var getVal = $("#inputValue").val();
        console.log(getVal)

        var xhr = new XMLHttpRequest();
        xhr.open("POST", 'http://localhost:8000/todo_app/todos/', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({
            title: getVal,
            content: "Test todo content."
        }));
        xhr.onload = function () {
            console.log(this.responseText);
            var data = JSON.parse(this.responseText);
            console.log(data);
            location.reload();
        };

    });
};
