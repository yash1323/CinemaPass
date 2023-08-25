# Cinemapass

 -------------------------------------------------------------------------------------------
				CinemaPass
-------------------------------------------------------------------------------------------

+INDEX+
-Description
-File Structure
-Usage

-------------------------------------------------------------------------------------------

-Description:
    CinemaPass is a program that allows users to book tickets for movies.
The program is stored in the dist folder, which contains all the necessary files 
for the program to run.

-File Structure:
    Here is a breakdown of the file structure
    dist
    ├── CinemaPass.exe
    ├── icon-high.png
    ├── icon-low.ico
    ├── Films
    │   ├── KGF-2
    │   │   ├── Movie-info.json
    │   │   └── Poster.jpeg
    │   ├── Varisu
    │   │   ├── Movie-info.json
    │   │   └── Poster.jpeg
    │   └── Vikram-Vedha
    │       ├── Movie-info.json
    │       └── Poster.jpeg
    ├── Screens
    │   ├── 1
    │   │   ├── 1000.json
    │   │   └── 1200.json
    │   ├── 2
    │   │   ├── 1000.json
    │   │   └── 1200.json
    │   └── 3
    │       ├── 1000.json
    │       └── 1200.json
    └── Tickets
        └── (empty)


-Usage:
1.Navigate to the dist directory and run CinemaPass.exe.
2.Once launched, enter your name and phone number when prompted.
 Make sure to enter your phone number accurately as it will be used to generate a 
 unique JSON file in the Tickets folder.
3.After entering your details, you will be presented with a list of available films.
4.Select your desired film from the list.
5.Choose your preferred showtime for the selected film.
6.Select your seats for the chosen showtime.
7.After selecting your seats, click the "Book" button to confirm your booking.
8.Your booking details will be saved in a JSON file in the Tickets folder with the
 phone number you provided.
9.Enjoy your movie with CinemaPass!

Thank you for using CinemaPass, and enjoy your movie!
