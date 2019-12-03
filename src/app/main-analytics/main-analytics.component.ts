import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgModule } from '@angular/core';
import 'rxjs/add/operator/map';
import { Chart } from 'chart.js';
import { WeatherService } from '../weather.service';

@Component({
  selector: 'app-main-analytics',
  templateUrl: './main-analytics.component.html',
  styleUrls: ['./main-analytics.component.css']
})
export class MainAnalyticsComponent implements OnInit {

  response: JSON;

  chart = [];

  constructor(private weather: WeatherService, private httpClient: HttpClient) {
  }

  ngOnInit() {
  }

  getResults() {
    this.weather.dailyForecast()
        .subscribe(res => {
          let frequencies = res['CDC_DESC'][0];
          let indices = res['CDC_DESC'][1];
          console.log(frequencies);
          console.log(indices);

          this.chart = new Chart(document.getElementById("bar-chart-horizontal"), {
            type: 'horizontalBar',
            data: {
              labels: indices,
              datasets: [
                {
                  label: "Elements of " + "CDC_DESC",
                  backgroundColor: "#3e95cd",
                  borderWidth: 25,
                  data: frequencies
                }
              ]
            },
            options: {
              legend: { display: false },
              title: {
                display: true,
                text: 'Frequencies of each element of ' + "CDC_DESC"
              }
            }
          });


        });
  }

}
