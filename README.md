<H1 align="center">
  Veeam Software
</H1>

<p align="center">
  <img src="https://bomitsolutions.co.uk/wp-content/uploads/veeam-partner-logo.png" alt="logo veeam" width="300">
</p>

## Introduction
Developed in Python, this program synchronizes two folders, source and replica, ensuring that the replica folder is an exact copy of the source folder. Synchronization is unidirectional, updating the replica folder to exactly match the contents of the source folder. It runs periodically, copying new or updated files from the source and removing files in the replica that no longer exist in the source. All synchronization operations, such as creating, updating, and removing files, are recorded both in the console and in a log file.

## Usage
**Dependencies**


The program is developed using Python's standard libraries and does not require any external dependencies. It can be run in any Python 3 environment.

**Usage**

Run the program from the command line, providing the paths to the source folder, replica folder, log file, and synchronization interval (in seconds):

         $ .py <source_directory> <replica_directory> <log_file> <interval>
Example:

         $ ./synchronization /path/to/source /path/to/replica /path/to/log.txt 10

**Arguments:**

* source_directory: Path to the source folder to be synchronized.
* replica_directory: Path to the folder that will store the synchronized copy (replica).
* log_file: Path to the log file where synchronization operations will be recorded.
* interval: Interval in seconds between each synchronization.

## Running the Application

Ensure the source and replica folders exist.
Provide a valid path for the log file.
Run the command above in the terminal. The program will enter a continuous synchronization loop, logging operations and keeping the replica folder identical to the source.

## Future code improvements
* Support for multiple folders: Enable synchronization of multiple folders in a single run.
* Safe shutdown option: Provide a way to stop the synchronization loop gracefully without abruptly closing the terminal.
* Bidirectional synchronization: Optionally allow changes in replica to be synchronized back to source.
* Reports and statistics: Implement periodic reports on synchronization status and detailed logging statistics.
