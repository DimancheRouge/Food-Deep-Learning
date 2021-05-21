from keras.preprocessing import image
from keras.models import Sequential, load_model
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as K
import numpy as np
import pathlib

#Train DL model for given food images
def train(epochs, modelNum, train, validate): #Epoch count, model ID #, training image # PER CLASS, validation image # PER CLASS

    #Image diemensions
    img_width, img_height = 224, 224

    #Model parameters
    train_data_dir = "train"     #Directory for training image folder
    validation_data_dir = "test"     #Directory for validation image folder
    nb_train_samples = train #Training image count
    nb_validation_samples = validate #Validation image count
    batch_size = 16

    #Image validation
    if K.image_data_format() == "channels_first":
        input_shape = (3, img_width, img_height)
    else:
        input_shape = (img_width, img_height, 3)

    #Model layers
    model = Sequential()
    model.add(Conv2D(32, (2, 2), input_shape = input_shape))
    model.add(Activation("relu"))
    model.add(Dropout(0.3))
    model.add(MaxPooling2D(pool_size = (2, 2)))

    model.add(Conv2D(32, (2, 2)))
    model.add(Activation("relu"))
    model.add(Dropout(0.3))
    model.add(MaxPooling2D(pool_size = (2, 2)))

    model.add(Conv2D(64, (2, 2)))
    model.add(Activation("relu"))
    model.add(Dropout(0.3))
    model.add(MaxPooling2D(pool_size = (2, 2)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation("relu"))
    model.add(Dropout(0.3))
    model.add(Dense(1))
    model.add(Activation("sigmoid"))

    #Model conifguration for compilation
    model.compile(loss = "binary_crossentropy", optimizer = "rmsprop", metrics = ["accuracy"])

    #Image generation
    train_datagen = image.ImageDataGenerator(rescale = 1. / 255, shear_range = 0.2, zoom_range = 0.2, horizontal_flip = True)
    test_datagen = image.ImageDataGenerator(rescale = 1. / 255)
    train_generator = train_datagen.flow_from_directory(train_data_dir, target_size = (img_width, img_height), batch_size = batch_size, class_mode = "binary")
    validation_generator = test_datagen.flow_from_directory(validation_data_dir, target_size = (img_width, img_height), batch_size = batch_size, class_mode = "binary")

    #Model fitting
    model.fit_generator(train_generator, steps_per_epoch = nb_train_samples // batch_size, epochs = epochs, validation_data = validation_generator, validation_steps = nb_validation_samples // batch_size)

    #Model saving
    model.save("model-{}-epochs-{}.h5".format(modelNum, epochs)) #Format: model-[model #]-epochs-[epoch #].h5
    print("Model Saved")

#Identify given image via DL model
def identify(imgName, modelName): #Image file name INCLUDING EXTENSIONS, model file name INCLUDING EXTENSIONS
    imgPath = pathlib.Path.cwd().joinpath(imgName)
    modelPath = pathlib.Path.cwd().joinpath(modelName)

    #image diemensions
    img_width, img_height = 224, 224

    #load saved model
    model = load_model(modelPath)
    model.compile(loss = "binary_crossentropy", optimizer = "rmsprop", metrics = ["accuracy"])

    #image preperation
    img = image.load_img(imgPath, target_size = (img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)

    #image prediction
    images = np.vstack([x])
    classes = model.predict_classes(images, batch_size = 10)

    prediction = model.predict(images)
    percentage = prediction[0]

    #return results
    if classes == 0:
        return "Apple"
    elif classes == 1:
        return "Banana"
