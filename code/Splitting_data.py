'''Splitting a data into training and testing set

The data is saved in a folder in which the subfolder represent the classes
'''



from sklearn.model_selection import train_test_split
import os
import shutil

# Path to the directory containing your full dataset
full_dataset_dir = '/home/aimsgh-02/Music/cancer'

# Path to the directory where the train and test splits will be saved
train_dir = '/home/aimsgh-02/Music/split_data/train'
test_dir = '/home/aimsgh-02/Music/split_data/test'

# Ratio of data to be used for testing (e.g., 0.2 for 20%)
test_size = 0.2

# Get the list of class directories in the full dataset directory
class_dirs = os.listdir(full_dataset_dir)

# Iterate over each class directory
for class_dir in class_dirs:
    # Path to the class directory in the full dataset
    class_dir_path = os.path.join(full_dataset_dir, class_dir)
    
    # Split the data into train and test sets
    train_files, test_files = train_test_split(os.listdir(class_dir_path), test_size=test_size)
    
    # Create the train and test directories for the current class
    train_class_dir = os.path.join(train_dir, class_dir)
    test_class_dir = os.path.join(test_dir, class_dir)
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(test_class_dir, exist_ok=True)
    
    # Move the train files to the train directory
    for train_file in train_files:
        shutil.move(os.path.join(class_dir_path, train_file), os.path.join(train_class_dir, train_file))
    
    # Move the test files to the test directory
    for test_file in test_files:
        shutil.move(os.path.join(class_dir_path, test_file), os.path.join(test_class_dir, test_file))


        
        
        
        
        
        
'''Splitting a data into training, validation and testing set

The data is saved in a folder in which the subfolder represent the classes
'''


from sklearn.model_selection import train_test_split
import os
import shutil

# Path to the directory containing your full dataset
full_dataset_dir = '/home/aimsgh-02/Music/cancer'

# Path to the directory where the train, validation, and test splits will be saved
train_dir = '/home/aimsgh-02/Music/split_data/with_val/train'
test_dir = '/home/aimsgh-02/Music/split_data/with_val/test'
valid_dir = '/home/aimsgh-02/Music/split_data/with_val/valid'



# Ratios of data to be used for validation and testing (e.g., 0.15 for 15% each)
valid_size = 0.15
test_size = 0.15

# Get the list of class directories in the full dataset directory
class_dirs = os.listdir(full_dataset_dir)

# Iterate over each class directory
for class_dir in class_dirs:
    # Path to the class directory in the full dataset
    class_dir_path = os.path.join(full_dataset_dir, class_dir)
    
    # Split the data into train, validation, and test sets
    train_files, test_valid_files = train_test_split(os.listdir(class_dir_path), test_size=(valid_size + test_size))
    valid_files, test_files = train_test_split(test_valid_files, test_size=(test_size / (valid_size + test_size)))
    
    # Create the train, validation, and test directories for the current class
    train_class_dir = os.path.join(train_dir, class_dir)
    valid_class_dir = os.path.join(valid_dir, class_dir)
    test_class_dir = os.path.join(test_dir, class_dir)
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(valid_class_dir, exist_ok=True)
    os.makedirs(test_class_dir, exist_ok=True)
    
    # Move the train files to the train directory
    for train_file in train_files:
        shutil.move(os.path.join(class_dir_path, train_file), os.path.join(train_class_dir, train_file))
    
    # Move the validation files to the validation directory
    for valid_file in valid_files:
        shutil.move(os.path.join(class_dir_path, valid_file), os.path.join(valid_class_dir, valid_file))
    
    # Move the test files to the test directory
    for test_file in test_files:
        shutil.move(os.path.join(class_dir_path, test_file), os.path.join(test_class_dir, test_file))

