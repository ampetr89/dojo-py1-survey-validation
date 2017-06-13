# Form with validation

## About
The landing page has a form, which upon submission checks that the name and comment fields are populated. If they are you are redirected to the results page. If not, you are redirected back to the form, where error message(s) will be displayed.

The data you enter in the form is sent via a POST request, and is routed to a process function. If the processing is successful, the form values are copied into the session variable, and then you are redirected to the results route, which renders the result.html template using the session variable for data. If the processing show errors for either the name and/or comment field, flash messages are added, and then the user is redirected to the survey entry page. The index.html file has some Jinga code to check for any error messages and display them if found.

## Screenshots
### Form entry page
![Form entry](/doc/index.png?raw=true "form entry")

### Form Errors
![Form errors](/doc/index-errors.png?raw=true "form with errors")

### Results page
![Form result](/doc/result.png?raw=true "result.html")
