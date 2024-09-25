import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-view-destinations',
  standalone: true,
  imports: [],
  templateUrl: './view-destinations.component.html',
  styleUrl: './view-destinations.component.css'
})
export class ViewDestinationsComponent implements OnInit {

  // destinations: any [] | undefined
  destinations = new Array<any>();

  constructor(private http: HttpClient){

  }
  ngOnInit(): void {

    console.log('Initial');
    
    this.http.get('http://localhost:8000/api/v1/destinations')
    .subscribe((data: any) => {
      console.log(data)
      // this.destinations = data
      this.destinations = data
    })
  }

}
