# Flask Emotion Detection Project

[![License](https://img.shields.io/badge/License-Apache-yellow.svg)](https://opensource.org/license/apache-2-0)

This is the final project of the course "Developing AI Applications with Python and Flask" by IBM as part of the IBM DevOps Certificate.

### Description

This project consists of building a Python web app using Flask and integrating Embeddable Watson AI libraries. The application of this project is basically an emotion detection program, which performs analytics on customer feedback.

### Usage

To use IBM Watson API it's necessary to import these libraries. This differs from the original project done on the Cloud IDE server offered by IBM.

To call the application on Python shell:

```python
$ python3
>>> from emotion_detection.emotion_detection import emotion_detector
>>> emotion_detector("I'm enjoying to play with ibm watson")
```


### License

Copyright (c) 2024, Guilherme Oliveira. All rights reserved.

Licensed under the Apache License. See [LICENSE](LICENSE)
