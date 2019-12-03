import {EventEmitter, Injectable} from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class HeaderAnalyticsServiceService {

  public onUpload$ = new EventEmitter<boolean>();

}
