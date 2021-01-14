# Lab-Check-In

## How to set up development enviornment

00. Install python 3.8.5 and pipenv
01. Clone repo
02. Run `pipenv install`
03. Select new virtual env as python interpreter.

## How to activate development enviornment and run app

01. Navigate to the debug menu on the left side of the screen
02. Click the green play botton at the top

## To-Do

* Implement and test Methods
* Create GUI
* Test Database

## List of methods to implement

* [ ] Extract student data from excel sheet and add it to database
* [x] Extract data from card
  * This is currently done with an HTML form
* [x] Parse extracted data
  * utilities.parse_card()
* [x] Check to see if they are checked in (Active User List)
  * This is currently done by querying transactions with no out_time
* [x] Search for User In Master Database
* [ ] Determine the available seat types
* [ ] Render the popup that shows the available seat types
* [ ] Extract data from Geek selection on seating type popup
* [ ] Use priority system and preference to determine optimal student placement
* [ ] Update seat in the array
* [ ] Render new seating chart based off array of seats
* [ ] Query active users database for number of active students
* [ ] Update the lab counter visually
* [ ] Remove user from the Active Users List
* [ ] Extract data from Geek interaction (changing state in the gui)
* [ ] Re-render gui
