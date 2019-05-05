import Augmentor

p = [Augmentor.Pipeline("Images/TrainingImages/glass"),
     Augmentor.Pipeline("Images/TrainingImages/metal"),
     Augmentor.Pipeline("Images/TrainingImages/paper"),
     Augmentor.Pipeline("Images/TrainingImages/plastic")]


for i in range(len(p)):
    p[i].rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
    p[i].zoom(probability=0.5, min_factor=1.1, max_factor=1.5)

    p[i].sample(1000)

    p[i].process()

