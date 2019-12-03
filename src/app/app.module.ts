import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import { HeaderComponent } from './header/header.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { MainAnalyticsComponent } from './main-analytics/main-analytics.component';
import { TopButtonsComponent } from './top-buttons/top-buttons.component';
import { DropdownComponent } from './util/dropdown/dropdown.component';
import { FileUploadComponent } from './util/file-upload/file-upload.component';
import { FileSelectDirective } from 'ng2-file-upload';
import { HttpClientModule } from '@angular/common/http';

import { WeatherService } from './weather.service';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    SidebarComponent,
    MainAnalyticsComponent,
    TopButtonsComponent,
    DropdownComponent,
    FileUploadComponent,
    FileSelectDirective
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    FormsModule,
    AppRoutingModule,
    ReactiveFormsModule
  ],
  providers: [WeatherService],
  bootstrap: [AppComponent]
})
export class AppModule { }
