#!/usr/bin/env python3
import os
import shutil
import time
import argparse
import logging

#Sets up logging configuration to output log messages to both a file and the console
def initialize_logging(log):
	logging.basicConfig(filename=log, level=logging.INFO, format='%(asctime)s - %(message)s')
	logging.getLogger().addHandler(logging.StreamHandler()) 

#Validates the existence of source and replica directories, access to the log file, 
#and ensures that the interval is a valid positive number
def validation(source, replica, log, interval):
	if not os.path.exists(source):
		raise ValueError(f"Source directory does not exist: {source}")
	if not os.path.exists(replica):
		raise ValueError(f"Replica directory does not exist: {replica}")
	try:
		with open(log, 'a'):
			pass
	except IOError:
		raise ValueError(f"Log file cannot be accessed: {log}")
	if interval < 0:
		raise ValueError(f"Interval must be a positive number: {interval}")
	
#Synchronizes the source and replica directories at the specified interval
def synchronization(source, replica, interval):
	while True:
		for root, _, files in os.walk(source):
			for file in files:
				source_file = os.path.join(root, file)
				replica_file = os.path.join(replica, os.path.relpath(root, source), file)
				
				#Copy or update files in the replica if they're new or modified
				if not os.path.exists(replica_file) or \
				   os.path.getmtime(source_file) > os.path.getmtime(replica_file):
					shutil.copy2(source_file, replica_file)
					logging.info(f"Updated: {replica_file}")
		
		#Remove files from replica that no longer exist in the source
		for root, _, files in os.walk(replica):
			for file in files:
				replica_file = os.path.join(root, file)
				source_file = os.path.join(source, os.path.relpath(root, replica), file)
				
				if not os.path.exists(source_file):
					os.remove(replica_file)
					logging.info(f"Removed: {replica_file}")
		time.sleep(interval)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Folder Synchronization')
	parser.add_argument('source', type=str, help='Source folder')
	parser.add_argument('replica', type=str, help='Replica folder')
	parser.add_argument('log', type=str, help='Log file')
	parser.add_argument('interval', type=int, help='Interval in seconds')
	args = parser.parse_args()

	try:
		validation(args.source, args.replica, args.log, args.interval)
		initialize_logging(args.log)
		synchronization(args.source, args.replica, args.interval)
	except ValueError as e:
		print(f"Error: {e}")
