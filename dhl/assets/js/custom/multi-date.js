  function createMultiDateSelection(jQuerySelector, multi, str){
    var date = [];

    if(multi) {
      var arr = str.split(', ');
      if(arr.length == 1){
        date[0] = new Date(str);
      } else {

        for (var i = arr.length - 1; i >= 0; i--) {
          date[i] = new Date(arr[i]);
        }
      }

    } else{
      var today = new Date();
      var dd = String(today.getDate()).padStart(2, '0');
      var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
      var yyyy = today.getFullYear();

      today = yyyy + '-' + mm + '-' + dd;
        date[0] = new Date(today);
    }

    $("#date-m").multiDatesPicker({
        dateFormat: "yy-mm-dd",
        addDates: date,
      }
    );
  }