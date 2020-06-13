  function drawSeriesGraph(jquerySelector,chartDataLabel, chartDataSeries){
    new Chartist.Line(jquerySelector, {
        labels: chartDataLabel,
        series: [chartDataSeries]
      }, {
      plugins: [
        Chartist.plugins.ctPointLabels({
          textAnchor: 'middle',
            labelInterpolationFnc: function(value) {
              if(value === undefined){
                return 0;
              }
              return value;
            }

        })
      ]
    });
  }