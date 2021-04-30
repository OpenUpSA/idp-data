document.addEventListener('DOMContentLoaded', () => {
    const ctx = document.getElementById('myChart').getContext('2d');

    chartData.forEach((d) => {
        d.x = new Date(d.date);
    });

    allChartData.forEach((d) => {
        d.x = new Date(d.date);
    });

    let datasets = [{
        label: 'All submissions',
        data: allChartData,
        backgroundColor: 'rgba(200,200,200,1)'
    }];

    if (chartData.length !== allChartData.length) {
        datasets.push({
            label: 'Filtered submissions',
            data: chartData,
            backgroundColor: 'rgba(20,20,220,1)'
        });
    }

    const chart = new Chart(ctx, {
        type: 'bar',
        data: {
            datasets: datasets
        },
        options: {
            responsive: false,
            scales: {
                xAxes: [
                    {
                        type: 'time',
                        time: {
                            unit: 'day',
                            round: 'day',
                            displayFormats: {
                                day: 'MMM D',
                            },
                        },
                    },
                ],
                yAxes: [
                    {
                        ticks: {
                            beginAtZero: true,
                        },
                    },
                ],
            },
        },
    });
});