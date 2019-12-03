import {Component, EventEmitter, OnInit} from '@angular/core';
import {FileUploader} from 'ng2-file-upload';
import {HeaderAnalyticsServiceService} from '../header-analytics-service.service';

const URL = 'http://localhost:4000/api/upload';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  constructor(private headerAnalyticsServiceService: HeaderAnalyticsServiceService) { }

  public uploader: FileUploader = new FileUploader({ url: URL, itemAlias: 'file' });
  public onClick = new EventEmitter();

  ngOnInit() {
    this.uploader.onAfterAddingFile = (file) => { file.withCredentials = false; };
    this.uploader.onCompleteItem = (item: any, response: any, status: any, headers: any) => {
      console.log('fileUpload:uploaded:', item, status, response);
      alert('File uploaded successfully');
    };
  }

  onUpload(){
    this.uploader.uploadAll();
    this.headerAnalyticsServiceService.onUpload$.emit(true);
  }

}
