# aquareport-cdm
AquaReport CDM - Water Fault Reporting System for Capricorn District Municipality
# AquaReport CDM

## Water Fault Reporting System for Capricorn District Municipality

###  Overview
AquaReport CDM is a user-centred interactive system that enables residents of Blouberg, Molemole, and Lepelle-Nkumpi to report water infrastructure failures directly to municipal authorities with full tracking and accountability.

### The Problem
Capricorn District Municipality faces a severe water crisis:
- **R213 million** spent on bulk water projects with no delivery
- **95%** of infrastructure breakdowns ignored by contractors
- **R24 million** operations budget exhausted in 3 months
- **24+ months** since Silvermine village had piped water

###  Features
| Feature | Description |
|---------|-------------|
|  User Authentication | Sign up, Login, Logout functionality |
|  Report Submission | Interactive map with Sepedi mock data examples |
|  Live Statistics | Real-time dashboard of all reports |
|  Community Personas | User profiles from submitted reports |
| Admin Dashboard | Full CRUD operations (update status, add feedback, delete) |
|  Responsive Design | Works on mobile, tablet, and desktop |
|  CDM YouTube Integration | Auto-playing video content |
|  Social Media Links | Official CDM Facebook, X, YouTube, Instagram |

###  Technology Stack
- **Backend:** Django 6.0.3
- **Database:** SQLite3
- **Frontend:** HTML5, CSS3, JavaScript
- **Maps:** Leaflet.js
- **Fonts:** Google Fonts (Inter, Bebas Neue, DM Sans)

###  Project Structure

mysite/
├── myapp/ # Main application (auth, reports, personas)
├── tracker/ # Statistics and admin dashboard
├── templates/ # HTML templates for all pages
├── static/ # Images, CSS, JavaScript
├── manage.py # Django management script
└── db.sqlite3 # SQLite database


###  Installation & Setup

```bash
# Clone the repository
git clone https://github.com/SetatiPhillipine/aquareport-cdm.git
cd aquareport-cdm

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install django

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Run the server
python manage.py runserver

 Access the Application:
Page	URL
Home	http://127.0.0.1:8000/
Report a Fault	http://127.0.0.1:8000/report/
My Reports	http://127.0.0.1:8000/my-reports/
Admin Dashboard	http://127.0.0.1:8000/admin-dashboard/
Personas	http://127.0.0.1:8000/personas/
Statistics	http://127.0.0.1:8000/stats/

N.B!!  Screenshots
[Add your screenshots here after taking them]

 Academic Context:
Developed for NHCI63110 - Human-Computer Interaction at Sol Plaatje University

Course Examiner: Mrs. K.E. Mamabolo

Moderator: Dr. Silas Verkijika

Submitted: 02 April 2026

 Author:
Setati Phuti Molepeledi Phillipine

GitHub: @SetatiPhillipine

Email: setatiphillipine@icloud.com

License
Academic Project - Sol Plaatje University

Acknowledgments
Capricorn District Municipality for source information

Sol Plaatje University ICT Department

Community members who provided insights

Re šoma le setšhaba — Working with the community!!


