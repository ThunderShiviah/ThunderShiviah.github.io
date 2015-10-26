# Shuffling, symmetric difference, and other GNU tools fun
# 11 Oct 2015

Today I was working on the [Springleaf Marketing Response data science
competition](https://www.kaggle.com/c/springleaf-marketing-response) on kaggle
and was having a problem loading the training data (921M) into memory.

The data itself is almost a thousand features (columns) and about 150k lines.

Before I could even start doing any exploratory analysis with the data I needed
a way to make some smaller samples that I could quickly load into memory and
run some test algorithms and visualizations on.

I decided a good first step to looking at the data would be to randomly sample
lines using the ```shuf``` command (available on linux), which shuffles the
lines of a file.

Before I could shuffle the file, I needed to remove the first line containing
the column names. Later, after I shuffle the file, I would then add the column
names back on.

There are a lot of ways to remove the head (a reasonable way would to just use
the ```tail -n +2``` command which outputs everything from the second line
onward) but for fun I decided to do it
using symmetric (set) difference. Symmetric difference is equivalent to the
union minus the intersection, so all elements contained in one set or the other
but not both.

One way we can take the set difference of two files is by [sorting both files
and then filtering based on unique
lines](https://unix.stackexchange.com/questions/11343/linux-tools-to-treat-files-as-sets-and-perform-set-operations-on-them). The sorting step is necessary so that
we can use the ```uniq``` command. 

Hence, set difference of two files can be achieved using

```
sort file1 file2 | uniq -u
```

(The u flag is for displaying only unique lines.)

Before we can apply this set difference, we still have a few more problems,
namely:

1. It's inelegant to make a temporary file of just the first line of the data
   so we can have two files.

In order to get around making a temp file, I can use parentheses (which
generates a sub-shell).

Ex.
```
cmd 2 <(cmd 1 file1) file2 
```
means run cmd 2 on file2 and the result of cmd 1 and file1.

So to get the main file stripped of the head we use

```
sort <(head -1 datafile) datafile | uniq -u | head -n 1000
```
which translates to "sort the data file and the first line of the data file and
then filter out all duplicates (symmetric difference). Finally, take the first
1000 lines of the shuffled data".

Now I just need to concatenate the column titles  with the first thousand lines of
the shuffled data. I can do this with another parenthesis subshell.

Ex.
```
cat <(cmd1 file1; cmd2 file2)
```

means "concatenate the result of cmd1 on file1 and the result of cmd2 on file2
(parallel streams)"

Hence, a command for stripping the first line off a dataset, randomly sampling
1000 lines and appending the first line back on is

cat <(head -1 data.csv; sort <(head -1
data.csv) data.csv | uniq -u
| shuf| head -n 1000) > raw_short.csv

To confirm that my command did what I wanted I first checked the number of
lines

```
wc -l raw_short.csv
```
(this should return 1001 lines since we had 1000 lines and we concatenated the
head).

Next I checked that the IDs (in column 1) were actually shuffled:
```
cut -f1 -d"," raw_short.csv | head -n 5
```
This says "take the first column (f stands for field) deliminated with ',' and
display the first five lines". This makes sense because the original ids were
in numeric order.

I then ran this command on my file which was about a gigabyte in size and it
finished in less than three seconds. Not bad!


