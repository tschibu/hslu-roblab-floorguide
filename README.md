_Cognitive Robotics Lab HS2018 - Team 10_

# FloorGuide

## Team
* Remo Schwarzentruber
* Michael Nebroj
* Serge Hauri
* Steve Ineichen

## Usage
### Prerequisites
* Choreograph installed ([http://doc.aldebaran.com/2-4/dev/community_software.html](http://doc.aldebaran.com/2-4/dev/community_software.html))
    * We expect that you know how to install an existing behavior onto a robot
* Working NAOqi Python SDK ([http://doc.aldebaran.com/2-4/dev/python/intro_python.html](http://doc.aldebaran.com/2-4/dev/python/intro_python.html))
    * **Note:** for MacOS follow [these instructions](https://github.com/tschibu/pepper-nao-python-installation-mac)
* All Python packages installed
    * Example with '[pip](https://pypi.org/project/pip/)' Pacakge Manager
        ```cmd
        pip install -r requirements.txt
        ```

### Clone this repository
```cmd
git clone https://gitlab.enterpriselab.ch/RobLab/RobLab-18HS/roblab-18hs-g10
```

### Register for Cloud Vision API
Register for [Cloud Vision API](https://cloud.google.com/docs/authentication/api-keys?hl=de&visit_id=636803038076480516-667118898&rd=1)

Afterwards the 'google_vision_config.json' within the 'res' directory has to be filled with the correct data (private key, project name, email, etc.)

### Install Webapps with Choreograph
* Load & Install 'webapp_map/choreograph/map.pml'
* Load & Install 'webapp_room_selection/choreograph/room_selection.pml'

### Start ControlFlow
* Navigate the the root folder of roblab-18hs-g10
* Check in [controlflow.py](controlflow.py) if the correct roboter is selected
    * You may have to adjust [configuration.py](configuration.py) according to your robot configuration
* Execute
    ```cmd
    python controlflow.py
    ```

## Last Updated
13. December 2018