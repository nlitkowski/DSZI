def main():
     import Augmentor

     p = [Augmentor.Pipeline("Images/TrainingImages/glass"),
          Augmentor.Pipeline("Images/TrainingImages/metal"),
          Augmentor.Pipeline("Images/TrainingImages/paper"),
          Augmentor.Pipeline("Images/TrainingImages/plastic")]

     for i in range(len(p)):
          # Setting the operations to perform on image set
          p[i].rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
          p[i].zoom(probability=0.5, min_factor=1.1, max_factor=1.5)
          p[i].flip_random(probability=0.6)
          p[i].skew(probability=0.7, magnitude=0.7)
     
          # Size of training sample
          p[i].sample(2000)

          p[i].process()

if __name__ == "__main__":
    main()

