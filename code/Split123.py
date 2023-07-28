from sklearn.model_selection import train_test_split
import os
import random
import shutil

# Path to the directory containing your full dataset
full_dataset_dir = '/home/aimsgh-02/Music/cancer'

# Path to the directory where the train, validation, and test splits will be saved
train_dir = '/home/aimsgh-02/AIMS/DATA/train'
test_dir = '/home/aimsgh-02/AIMS/DATA/test'
valid_dir = '/home/aimsgh-02/AIMS/DATA/valid'

# Ratios for the first split
train_size = 0.8
test_size = 0.2

# Get the list of class directories in the full dataset directory
class_dirs = os.listdir(full_dataset_dir)

# Iterate over each class directory
for class_dir in class_dirs:
    # Path to the class directory in the full dataset
    class_dir_path = os.path.join(full_dataset_dir, class_dir)
    
    # Get the list of files in the class directory
    file_list = os.listdir(class_dir_path)
    
    # Take 10% of the files randomly
    file_sample = random.sample(file_list, int(len(file_list) * 0.1))
    
    # Split the sampled files into train, validation, and test sets
    train_files, test_files = train_test_split(file_sample, test_size = test_size, train_size=train_size)
    #valid_files, test_files = train_test_split(valid_test_files, test_size=(test_size / (valid_size + test_size)))
    
    # Create the train, validation, and test directories for the current class
    train_class_dir = os.path.join(train_dir, class_dir)
    #valid_class_dir = os.path.join(valid_dir, class_dir)
    test_class_dir = os.path.join(test_dir, class_dir)
    os.makedirs(train_class_dir, exist_ok=True)
    #os.makedirs(valid_class_dir, exist_ok=True)
    os.makedirs(test_class_dir, exist_ok=True)
    
    # Move the train files to the train directory
    for train_file in train_files:
        shutil.copy(os.path.join(class_dir_path, train_file), os.path.join(train_class_dir, train_file))
    
    # Move the validation files to the validation directory
   # for valid_file in valid_files:
       # shutil.copy(os.path.join(class_dir_path, valid_file), os.path.join(valid_class_dir, valid_file))
    
    # Move the test files to the test directory
    for test_file in test_files:
        shutil.copy(os.path.join(class_dir_path, test_file), os.path.join(test_class_dir, test_file))

