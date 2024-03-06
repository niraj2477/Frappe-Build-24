This repository contains two Frappe apps for demonstrating how Doc Events and Document Class Override works.

## Installation

To install the apps, follow the steps.

1. Clone the repository, and change the directory.
   ```bash
    git clone https://github.com/niraj2477/Frappe-Build-24.git
   ```
2. Install the apps via `bench get-app <path>`.
    ```bash
    bench get-app /path/to/app
    ```
    example:
    ```bash
    bench get-app /frappe_docevent
    ```
3. Install the app on site.
    ```bash
    bench --site <sitename> install-app frappe_docevent
    ```

## Overview
######  Doc Events
are the life cycle methods which are available on every DocType within the frapp, which allow the custom scripts/apps to add their add on functionality on top of the Existing document.

###### Document class override
is a pythonic way to change the implementation of class method or the whole class by providing specific implementation according to requirements.

## Reference Links

- [Controller hooks](https://frappeframework.com/docs/user/en/basics/doctypes/controllers#controller-hooks)

- [Document class override](https://frappeframework.com/docs/user/en/python-api/hooks#override-doctype-class)

- [Frappe framework](https://frappeframework.com/)

- [Presentation](https://docs.google.com/presentation/d/1xOzb2LV3KdmlvkPgLiTUbGvw5W_JG4K5PBbuIQrj4fY)