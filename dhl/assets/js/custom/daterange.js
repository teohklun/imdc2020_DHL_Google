
  function createDateRangePickeR(jQuerySelector, startDate, endDate){
    $(jQuerySelector).daterangepicker({
      startDate: startDate,
      endDate: endDate,
      // singleDatePicker: true,
      multidate: true,
      showDropdowns: true,
      locale: {
        format: 'YYYY-MM-DD'
      },
      ranges: {
          'Today': [moment(), moment()],
          'Yesterday': [moment().subtract(1, 'days'), moment().subtract(1, 'days')],
          'Last 7 Days': [moment().subtract(6, 'days'), moment()],
          'Last 30 Days': [moment().subtract(29, 'days'), moment()],
          'This Month': [moment().startOf('month'), moment().endOf('month')],
          'Last Month': [moment().subtract(1, 'month').startOf('month'), moment().subtract(1, 'month').endOf('month')]
      },
    }, function(start, end, label) {
        console.log('New date range selected: ' + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD') + ' (predefined range: ' + label + ')');
      });
  }