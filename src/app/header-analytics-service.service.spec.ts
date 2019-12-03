import { TestBed } from '@angular/core/testing';

import { HeaderAnalyticsServiceService } from './header-analytics-service.service';

describe('HeaderAnalyticsServiceService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: HeaderAnalyticsServiceService = TestBed.get(HeaderAnalyticsServiceService);
    expect(service).toBeTruthy();
  });
});
