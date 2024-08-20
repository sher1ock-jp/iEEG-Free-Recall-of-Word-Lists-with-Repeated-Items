# Free Recall of Word Lists with Repeated Items

## Table of Contents
- [Dataset Description](#DatasetDescription)
- [Notes](#Notes)
- [Dataset Exploring](#features)

### Description
This dataset contains behavioral events and intracranial electrophysiological recordings from a repated item free recall task.  The experiment consists of participants studying a list of words, presented visually one at a time, and then freely recalling the words from the just-presented list in any order. On each list, there is a 7-second delay period between the encoding and recall phases.  The data were collected at clinical sites across the country as part of a collaboration with the Computational Memory Lab at the University of Pennsylvania.

The main manipulation in this paradigm is the repetition of items in the studied list. In total, each list contains 27 encoding events, but only 12 unique words: 3 are presented one time, 3 are presented two times, and 6 are presented three times.  


### Notes
* The duration of the encoding events (i.e., length of word presentation) varies among sessions.  For some sessions, the words remained on screen from 750 ms, while in other sessions presentation lasted for 1600 ms. The `duration` column of the events tsv files contains this information.
* The iEEG recordings are labeled either "monopolar" or "bipolar."  The monopolar recordings are referenced (typically a mastoid reference), but should always be re-referenced before analysis.  The bipolar recordings are referenced according to a paired scheme indicated by the accompanying bipolar channels tables.
* Each subject has a unique montage of electrode locations.  MNI and Talairach coordinates are provided when available.
* Recordings done with the Blackrock system are in units of 250 nV, while recordings done with the Medtronic system are estimated through testing to have units of 0.1 uV.  We have completed the scaling to provide values in V.

### Dataset Exploring

#### What is Events Data
| Onset   | Duration | Sample | Trial Type  | Response Time | Stim File                  | Item Name | Serial Pos | Repeats | List | Experiment | Session | Subject |
|---------|----------|--------|-------------|---------------|----------------------------|-----------|------------|---------|------|------------|---------|---------|
| 0.0     | 0.008    | 11048  | START       | n/a           | n/a                        | n/a       | -999       | -999    | 0    | RepFR1     | 0       | R1204T  |
| 0.008   | 232.234  | 11056  | SESS_START  | n/a           | n/a                        | n/a       | -999       | -999    | 0    | RepFR1     | 0       | R1204T  |
| 232.242 | 13.752   | 243290 | TRIAL_START | n/a           | n/a                        | n/a       | -999       | -999    | 0    | RepFR1     | 0       | R1204T  |
| 245.994 | 3.0      | 257042 | COUNTDOWN   | n/a           | n/a                        | n/a       | -999       | -999    | 0    | RepFR1     | 0       | R1204T  |
| 250.127 | 1.6      | 261175 | WORD        | n/a           | wordpools/wordpool_EN.txt  | HORN      | 0          | 3       | 0    | RepFR1     | 0       | R1204T  |
| 252.544 | 1.6      | 263592 | WORD        | n/a           | wordpools/wordpool_EN.txt  | ARCH      | 1          | 1       | 0    | RepFR1     | 0       | R1204T  |
| 255.095 | 1.6      | 266143 | WORD        | n/a           | wordpools/wordpool_EN.txt  | SPONGE    | 2          | 3       | 0    | RepFR1     | 0       | R1204T  |
| 257.562 | 1.6      | 268610 | WORD        | n/a           | wordpools/wordpool_EN.txt  | ROCK      | 3          | 3       | 0    | RepFR1     | 0       | R1204T  |
| 260.046 | 1.6      | 271094 | WORD        | n/a           | wordpools/wordpool_EN.txt  | THREAD    | 4          | 3       | 0    | RepFR1     | 0       | R1204T  |

![behavioral_events_over_time](output/behavioral_events_over_time.png)