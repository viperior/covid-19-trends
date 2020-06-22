import subprocess

print('Reloading data...')
import reload_data
print('Reloaded data!')

print('Getting repo status...')
subprocess.call(["git", "status"])

print('Adding updated data files...')
subprocess.call(["git", "add", "data/"])
print('Data files added!')

print('Adding updated chart files...')
subprocess.call(["git", "add", "docs/charts/"])
print('Chart files added!')

print('Adding commit message...')
subprocess.call(["git", "commit", "-m", 'Reload data.'])
print('Commit message added!')

print('Pushing changes...')
subprocess.call(["git", "push"])
print('Changes successfully pushed!')

print('Verifying repo status...')
subprocess.call(["git", "status"])
print('Repo status verified!')
print('Git repository updated!')
print('Reload process completed successfully!')
