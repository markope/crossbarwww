`wpadlab` is an application which

* visualizes the current raw values received from a weighing pad component (such as the [Arduino Yun Weighing Pad](Arduino Yun Weighing Pad))
* helps in generating training data for determination of user-defined units
* shows a current number of user-defined units based on a model derived from a set of training data

--- screenshot of the entire wpadlab ---

## Setup

`wpadlab` consist of a Web frontend and a (Python) backend component which stores training data for further use. 

You need [Crossbar.io installed](../docs/Local-Installation).

The code for wpadlab can be found in the [crossbarexamples GitHub repository](https://github.com/crossbario/crossbarexamples) under `iotcookbook`. You need to clone this (or [download it as a ZIP file](https://github.com/crossbario/crossbarexamples/archive/master.zip)).

Once you've done so, start Crossbar.io in the app directory (`iotcookbook/app/weight/wpadlab`) by doing 

```shell
crossbar start
```

In addition to starting the WAMP router through which components connect, this automatically runs the Python backend component and serves the Web frontend.

Go to the Web frontend at 

```
http://localhost:8080
```

To generate a model and to derive the parameters for the model [IPython](http://ipython.org/). IPython provides browser-based notebooks with support for code, rich text, mathematical expressions, inline plots and other rich media.

We provide an IPython notebook with a model for a three-sensor weighing platform. We'll go through using this, and how to adapt it for use with more sensors, further on.


## Configuration

The frontend as a default receives data from the [Arduino Yun Weighing Pad component](Arduino Yun Weighing Pad) and expects sensor values from 3 pads.

You can adjust this in the respective fields in the UI:

--- screenshot of URL entry field ---

--- screenshot of the # pad fields

(In case more pad values are sent, then these are discared for display and other processing.)


## Raw Visualization

The frontend creates bar displays based on the number of pads.

-- screenshot of some data being displayed ---

## Creating a Training Set

A training set contains groups of sensor values along with the unit value this group corresponds to.

Let's say we want to measure how many creates are on a weighing platform. The process for creating a training set is:

* set the value for which you want to add a group to the set (leave unchanged if you want to add an additional set to a value)
* put the respective number of crates on the platform
* store the group of values
* repeat

Naturally you start off with zero crates. Since the sensors have some noise, and placement of the crates on the platform matters for the readings, you should create several groups of values for each number of crates you want to measure, e.g. placing them in different positions on the platform for each new group.

Once you have enough values to cover the range of states well, save the set. This sends the set to the Python backend component which then stores it on disk. You then see the name of the saved set in the title bar.

## Using the IPython notebook

You need to create a model and parametrize this in order to use the mechanism in the frontend.

To help with this we provide an IPython notebook. This can load training sets and save paramters for a model.

Once you have installed IPython ("pip install 'ipython[notebook]'" should do the trick), go to the `notebook` subdirectory in the app directory and start the IPython notebook server by doing

```shell
ipython notebook
```

This should automatically open a page with the directory of available notbooks in your default browser. (Otherwise you can access this at `localhost:8888/tree`). Select the notebook `estimate_model.ipynb`.

The documentation for what to do in this notebook is part of the notebook itself.

## Using a Parametrized Model

Once you've used the IPython notebook to derive the correct parameters for your use case you can load this model into wpadlab and test its output. Just as with the saving of training sets, the loading of parameters is done via a WAMP call to the Python backend component. You need to enter the name of the parameter set you wish to use, as it was displayed in the IPython notebook when storing it.

Once you've loaded the model, you'll receive numeric output for the predicted value. 

### Using and adapting the model code

The model code itself is contained in the function `model_predict`. There are comments directly preceding this in the code which list the variables this requires to be set in order to work.

If you're using more than three sensors you need to add additional variables (e.g. "a1", "a7") and add the processing for these.