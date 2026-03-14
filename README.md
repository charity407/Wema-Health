
# 🌺 Wema Health: Afrocentric Women's Health Navigator

Wema Health is a dedicated health navigation platform tailored specifically for the African woman. Designed with a fully Afrocentric UI/UX, the platform empowers women to take charge of their health through daily symptom tracking, access to verified medical information, and a vibrant community support network. 

By bridging the gap between patients and healthcare providers, Wema Health ensures that health data is tracked accurately, easing the diagnostic process for doctors while providing a culturally resonant experience.

---

## ✨ Key Features

* **Daily Symptom Tracker:** Allows users to manually enter and track their symptoms daily. This generates comprehensive health logs that can be easily shared with doctors to facilitate better, faster diagnoses.
* **Disease Information Hub ("Learn More"):** An educational section providing accurate, real-world data and verified information about diseases and health conditions, specifically focusing on those that affect women.
* **Community Support Groups:** A built-in safe space and support network for users to connect, share experiences, and find solidarity on their health journeys.
* **Afrocentric UI/UX:** An intuitive, culturally relevant design built from the ground up to reflect the identity, experiences, and specific needs of the African woman.

## 🛠 Tech Stack

* **Backend / API:** Python (FastAPI) powered by `app.py` for high-performance endpoints and custom logic.
* **Data Integration:** Medical logic mapping utilizing real-world datasets (such as ICD-11 or SNOMED CT) for accurate symptom-to-condition mapping.
* **Database Integration:** Designed to integrate with robust relational databases like PostgreSQL (e.g., via Supabase) for secure user and health data management.

## 🚀 Getting Started

### Prerequisites

* Python 3.8+
* `pip` (Python package installer)
* Virtual Environment (recommended)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/charity407/Wema-Health.git](https://github.com/charity407/Wema-Health.git)
    cd Wema-Health
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    *(Assuming a `requirements.txt` is present; if not, you will need to install FastAPI and Uvicorn manually).*
    ```bash
    pip install fastapi uvicorn
    # Or pip install -r requirements.txt
    ```

### Running the Application

To start the Wema Health backend server locally, run the `app.py` entry point:

```bash
uvicorn app:app --reload

```

The API will be available at `http://127.0.0.1:8000`. You can view the interactive API documentation (Swagger UI) by navigating to `http://127.0.0.1:8000/docs`.

## 📂 Project Structure

```text
Wema-Health/
│
├── app.py                 # Main application entry point and FastAPI routing
├── requirements.txt       # Project dependencies (ensure this is added)
├── core/                  # Core logic (symptom mapping, data models)
├── api/                   # API endpoints (users, tracking, education)
└── README.md              # Project documentation

```

## 🤝 Contributing

Wema Health is built on the vision of empowering women in technology and healthcare. Contributions are highly encouraged! If you have suggestions for improving the Afrocentric UI, adding new real-world health datasets, or optimizing the backend logic:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🛡 License

Distributed under the MIT License. See `LICENSE` for more information.

---

*Built with passion to empower, educate, and elevate African women's health.*

```

