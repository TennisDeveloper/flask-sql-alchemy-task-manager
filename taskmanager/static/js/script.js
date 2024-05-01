  document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    
    //datepicker initialization, code copied from https://materializecss.com/pickers.html, 
    //adjusted and instead of options we set the format of the date
    ////instead of done I will have there select. This is the internalization option from the materialize documentation
    let datepicker = document.querySelectorAll(".datepicker");
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {done: "Select"}
    });

    // select initialization
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);
});
