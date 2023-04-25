# 🌍 Trash2Treasure

Trash2Treasure is a sustainability-focused game designed to promote eco-friendly practices in an engaging and interactive way. The game utilises a web application and a location-based adventure to involve users in sustainability activities on the University of Exeter's campus.

## 📋 Table of Contents

- [🌐 Overview](#overview)
- [⚙️ Features](#features) 
- [👥 Authors](#authors) 
- [📦 Requirements](#requirements)
- [🌲 Project Structure](#project-structure) 
- [🧪 Executing Test Suites](#running-the-tests)
- [🌱 Configuring the Virtual Environment](#running-the-virtual-environment)
- [☁️ Deployment and Hosting](#the-cloud) 
- [🚀 Launching the Application](#running-the-program)
- [📚 Additional Resources](#additional-resources)
- [📝 License](#license) 


## 🌐 Overview

Players embark on an exciting journey around their campus, collecting virtual rubbish and answering sustainability-related questions to accumulate points. The game introduces a competitive element, as only one user can collect each generated piece of rubbish. As players gather more trash, they earn points that can be spent on items in the in-game store.

To collect rubbish, players must scan a QR code at the event building's location and correctly answer three sustainability-based multiple-choice questions. Correct answers award points and remove the rubbish from the location. Players can view their virtual environmental impact within their personal rubbish bin, which stores their collected trash.

The game also offers a section featuring sustainable resources, such as articles and videos, that provide information on eco-friendly practices and links to University of Exeter resources. Gamekeepers have the ability to add, configure, edit, and delete resources, gamekeepers, store items, questions, and rubbish collection events.

A leaderboard showcases the top scorers in virtual rubbish collection, fostering healthy competition among players. In-game purchases are available exclusively within the proximity of the forum building on Streatham Campus.

## ⚙️ Features

- Interactive map with location-based virtual rubbish collection events
- QR code scanning for easy event participation
- Engaging sustainability-themed multiple-choice questions
- Personal rubbish bins to monitor individual environmental impact
- Competitive leaderboard showcasing top scorers
- In-game store with purchasable items and rewards
- Comprehensive sustainable resources section with educational content
- Robust gamekeeper management tools for content and event administration

## 👥 Authors

- [@joshfinney](https://github.com/joshfinney)
- [@jarljreg](https://github.com/jarljreg)
- [@sixtifever](https://github.com/sixtifever)
- [@stefancourt](https://github.com/stefancourt)
- [@jamesbarkes](https://github.com/jamesbarkes)
- [@sangeethsohan100](https://github.com/sangeethsohan100)
- Version: 10.1

## 📦 Requirements

The following libraries and packages are required to run the Trash2Treasure application. Ensure that you have the correct versions installed in your development environment.

- [Babel Core](https://babeljs.io/docs/en/babel-core) 7.2.0: A JavaScript compiler that enables the use of the latest JavaScript features, ensuring compatibility with older browsers and environments.
- [Parcel Bundler](https://parceljs.org/) 1.6.1: A fast, zero-configuration web application bundler, responsible for bundling and optimising assets like JavaScript, CSS, and images.
- [Django](https://www.djangoproject.com/) 4.1.7: A high-level Python web framework that promotes rapid development and clean, pragmatic design, used for building the backend of the Trash2Treasure application.
- [Pillow](https://pillow.readthedocs.io/en/stable/) 9.4.0: A powerful Python Imaging Library (PIL) fork that adds image processing capabilities to the application, such as image resizing and format conversions.
- [Pytest](https://docs.pytest.org/en/latest/) 7.2.2: A mature, feature-rich testing framework for Python, enabling efficient and reliable testing of the application's functionality.
- [Pytest-django](https://pytest-django.readthedocs.io/en/latest/) 4.5.2: A plugin that facilitates Django integration with the Pytest testing framework, simplifying the testing process for Django applications.

## 🌲 Project Structure

```plaintext
Trash2Treasure/
├── Process-Documents/
│   ├── Database/
│   │   ├── Dependencies.md
│   │   ├── Relational-Schema.md
│   │   ├── ERD-v1.pdf
│   │   ├── ERD-v2.pdf
│   │   ├── ERD-v3.pdf
│   │   ├── ERD-v4.pdf
│   │   ├── ERD-draft.png
│   │   └── ERD-final.png
│   ├── Game/
│   │   ├── Initial-Ideas.md
│   │   ├── MoSCoW-Matrix.md
│   │   └── User-Stories/Epics-Diagram.jpg
│   ├── Location/
│   │   ├── QR-Generator.py
│   │   ├── Location-Report-Log.md
│   │   ├── qrPic/
│   │   │   └── ...
│   │   └── QR-Scanner/
│   │       └── ...
│   ├── Design/
│   │   ├── Wireflow-Diagram.jpg
│   │   └── Wireflow.mov
│   └── Kanban-Snapshots.pdf
├── Product-Documents/
│   ├── API-Specification.json
│   ├── Architecture-and-Design.md
│   ├── Codebase-Documentation.md
│   ├── Deployment-Documentation.md
│   ├── Project-Resources.md
│   ├── Testing-Documentation.md
│   └── User-Documentation.md
├── Technical-Documents/
│   ├── Source/
│   │   └── ...
│   └── venv/
│       └── ...
├── LICENSE
└── README.md
```

## 🧪 Executing Test Suites

To execute the test suites for the Trash2Treasure application, follow these steps:

1. Ensure you are within the application's virtual environment.
2. Locate the tests using the **pytest** framework within each separate app, including backend, frontend, and database tests.
3. Run the tests for a specific app by entering the following command in the terminal:

```bash
pytest <app>
```

Replace `<app>` with the name of the app whose tests you want to run. For example:

```bash
pytest bin
```

The output, including test results and any error messages, will be displayed in the terminal.

## 🌱 Configuring the Virtual Environment

To configure the virtual environment for the Trash2Treasure application, follow these steps:

1. Navigate to the **Technical Documents/Source directory**.
2. Run the following command to activate the virtual environment:

```bash
source venv/bin/activate
```

After activating the virtual environment, you can cd into the website directory and perform various development tasks, such as installing packages or running the application.

## ☁️ Deployment and Hosting

The Trash2Treasure application is deployed and hosted on the domain [trash2treasure.info](http://trash2treasure.info). The deployment process ensures that the application is available to users across different devices and platforms.

## 🚀 Launching the Application

To launch the Trash2Treasure application, follow the steps below:

1. Navigate to the **Technical Documents/Source/website** directory.
2. Execute the following command:

```bash
python3 manage.py runserver
```

This command starts the server and runs the application on a localhost. To run the server on a mobile device, add `0.0.0.0:8000` at the end of the command:

```bash
python3 manage.py runserver 0.0.0.0:8000
```

3. On the mobile device's browser, enter the IP address of the network to access the application.

QR codes for the application can be found in the **Technical Documents/Source/website** directory. These QR codes facilitate navigation to specific sections of the application, enhancing the user experience.

## 📚 Additional Resources

- [Sustainable Living Tips](https://www.sustainablelivingtips.org/): An extensive collection of practical tips and ideas for adopting a more sustainable lifestyle, including information on energy efficiency, waste reduction, and eco-friendly travel.
- [Green Living Ideas](https://www.greenlivingideas.com/): A comprehensive resource for green living, offering articles on various topics such as sustainable food, eco-friendly products, and renewable energy sources.
- [University of Exeter Sustainability](https://www.exeter.ac.uk/sustainability/): The official sustainability page for the University of Exeter, featuring information on the university's sustainability initiatives, strategies, and campus-wide projects.

## 📝 License

Trash2Treasure is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

Copyright (c) 2023 Joshua Finney, Jarl J Reg, Sixti Fever, Stefan Court, James Barkes, Sangeeth Sohan 100.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
