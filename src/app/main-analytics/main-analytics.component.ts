import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgModule } from '@angular/core';
import 'rxjs/add/operator/map';
import { Chart } from 'chart.js';
import { WeatherService } from '../weather.service';
import {FormGroup, ReactiveFormsModule} from '@angular/forms';
import { FormControl, Validators} from '@angular/forms';
import {HeaderAnalyticsServiceService} from '../header-analytics-service.service';

@Component({
  selector: 'app-main-analytics',
  templateUrl: './main-analytics.component.html',
  styleUrls: ['./main-analytics.component.css']
})
export class MainAnalyticsComponent implements OnInit {

  columns = [];
  analyticsForm = new FormGroup({
      column_selected : new FormControl('', Validators.required),
      chart_type_selected : new FormControl('Bar chart', Validators.required),
      num_examples : new FormControl(10, Validators.required)
  });
  chart : Chart;
  frequencies = [];
  indices = [];
  response = {};
  chart_types = ['Bar chart','Pie chart', 'Polar Area Chart', 'Radar Chart']

  ngOnInit() {
  }

    constructor(private weather: WeatherService, private httpClient: HttpClient, private headerAnalyticsServiceService:HeaderAnalyticsServiceService) {
        this.headerAnalyticsServiceService.onUpload$.subscribe(res => {
            this.getResults();
    });
    }

  getResults() {
    this.weather.dailyForecast()
        .subscribe(res => {
            this.response = res;
            this.columns = Object.keys(res);
            this.analyticsForm.get('column_selected').setValue(this.columns[0]); //default
        });
  }

  getChartType(){
      if(this.analyticsForm.get('chart_type_selected').value == 'Bar chart'){
          return 'horizontalBar';
      }
      else if(this.analyticsForm.get('chart_type_selected').value == 'Pie chart'){
          return 'pie';
      }
      else if(this.analyticsForm.get('chart_type_selected').value == 'Polar Area Chart'){
          return 'polarArea';
      }
      else if(this.analyticsForm.get('chart_type_selected').value == 'Radar Chart'){
          return 'radar';
      }
      return 'horizontalBar'; //default
  }

  buildChart(){

      this.frequencies = this.response[this.analyticsForm.get('column_selected').value][0].slice(0,this.analyticsForm.get('num_examples').value);
      this.indices = this.response[this.analyticsForm.get('column_selected').value][1].slice(0,this.analyticsForm.get('num_examples').value);
      if(this.chart) {
          this.chart.destroy();
      }

      this.chart = new Chart(document.getElementById("chart"), {
          type: this.getChartType(),
          data: {
              labels: this.indices,
              datasets: [
                  {
                      label: "Elements of " + this.analyticsForm.get('column_selected').value,
                      backgroundColor: "#3e95cd",
                      borderWidth: 25,
                      data: this.frequencies
                  }
              ]
          },
          options: {
              legend: { display: false },
              title: {
                  display: true,
                  text: 'Frequencies of each element of ' + this.analyticsForm.get('column_selected').value
              }
          }
      });
  }

}
