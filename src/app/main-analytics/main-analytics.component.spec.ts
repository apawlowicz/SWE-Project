import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MainAnalyticsComponent } from './main-analytics.component';

describe('MainAnalyticsComponent', () => {
  let component: MainAnalyticsComponent;
  let fixture: ComponentFixture<MainAnalyticsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MainAnalyticsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MainAnalyticsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
