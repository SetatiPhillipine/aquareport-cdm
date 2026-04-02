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
