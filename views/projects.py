"""
  @author Victor I. Afolabi
  A.I. engineer/researcher & Software engineer
  javafolabi@gmail.com
  
  Created on 04 January, 2018 @ 7:28 PM.
  
  Copyright © 2018. Victor. All rights reserved.
"""
from flask import render_template

from models.projects.image_classification import *
from views import app, back


@app.route('/projects/')
@back.anchor
def projects():
    return render_template('projects/index.html')


@app.route('/projects/image-classification/', methods=['GET', 'POST'])
@back.anchor
def image_classification():
    data = dict()
    # TODO: Image classification UI/UX
    # Retrieve all available image datasets
    data['datasets'] = all_datasets(full_path=False)
    data['datasets_full'] = all_datasets(full_path=True)
    # Options for next dataset upload
    # Verify uploaded dataset [At least 2 classes]
    # Process selection on the UI for the requested dataset
    # Room for training and testing a new dataset
    # Retrieve dataset classes and one random image for each class
    data['class_n_image'] = classes_and_image(dataset_dir=data['datasets_full'][0])
    # Write a JavaScript snippet to show training progress
    # And testing in case of  delay
    return render_template('projects/image-classification.html', data=data)


@app.route('/projects/generative-models/')
@back.anchor
def generative_models():
    return render_template('projects/generative-models.html')


@app.route('/projects/image-search/')
@back.anchor
def image_search():
    return render_template('projects/image-search.html')


@app.route('/projects/ai-articles/')
@back.anchor
def ai_articles():
    return render_template('projects/ai-articles.html')


@app.route('/projects/auto-encoding/')
def auto_encoding():
    return render_template('projects/auto-encoding.html')


@app.route('/projects/reinforcement-learning/')
@back.anchor
def reinforcement_learning():
    return render_template('projects/reinforcement-learning.html')
