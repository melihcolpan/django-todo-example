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
        console.log(getVal);
        if (getVal === '') {
            alert("Plase add a new todo!");
            return
        }

        var xhr = new XMLHttpRequest();
        xhr.open("POST", 'http://3.9.39.158:8000/', true);
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

    $(".delete-btn").click(function () {
        todo_id = $(this).attr('about');
        console.log(todo_id);

        var xhr = new XMLHttpRequest();
        xhr.open("DELETE", 'http://3.9.39.158:8000/', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({
            todo_id: todo_id
        }));
        xhr.onload = function () {
            console.log(this.responseText);
            var data = JSON.parse(this.responseText);
            console.log(data);
            location.reload();
        };
    });

    $("#inputValue").keypress(function (event) {
        if (event.keyCode === 13) {
            $("#add-todo").click();
        }
    });

    $(".edited-input").keypress(function (event) {
        if (event.keyCode === 13) {
            var v = $(this).parent().parent().children('div:nth-child(4)')
                .children('div:nth-child(1)')
                .children('h5:nth-child(1)')
                .children('i:nth-child(1)');
            v.click();
        }
    });

    $(".edit-btn").click(function () {
        todo_id = $(this).attr('about');

        var row_input = $(this).parent().eq(3).children('div:nth-child(2)').children('input');
        row_input.attr("readonly", false);
        var len = row_input.val().length;
        row_input[0].focus();
        row_input[0].setSelectionRange(len, len);
    });

    $(".save-btn").click(function () {
        console.log("save");
        todo_id = $(this).attr('about');

        var row_input = $(this).parent().eq(3).children('div:nth-child(2)').children('input');
        row_input.attr("readonly", true);

        var xhr = new XMLHttpRequest();
        xhr.open("PUT", 'http://3.9.39.158:8000/', true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({
            todo_id: todo_id,
            title: row_input.val()
        }));
        xhr.onload = function () {
            console.log(this.responseText);
            var data = JSON.parse(this.responseText);
            console.log(data);
            location.reload();
        };

    });

};
