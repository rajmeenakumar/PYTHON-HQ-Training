import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ViewDestinationsComponent } from "./view-destinations/view-destinations.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, ViewDestinationsComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'my-first-project';
}
