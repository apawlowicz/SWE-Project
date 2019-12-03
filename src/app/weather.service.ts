import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import 'rxjs/add/operator/map';

@Injectable({
  providedIn: 'root'
})
export class WeatherService {

  constructor(private http: HttpClient) { }

  dailyForecast() {
    return this.http.get("http://localhost:5002/frequencies/data.csv")
        .map(result => result);
  }

}

