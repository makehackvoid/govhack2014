#Contributing to govhack2014

Please make your own fork the repository and use pull requests to submit changes. This lets [TravisCi](https://travis-ci.org/makehackvoid/govhack2014) check for errors before the changes are committed to master.

## Use issues to organise work

So that other people know what you are working on, either assign an existing issue to yourself or create a new issue and then assign it. Ask if you don't have access or need help doing this. Reference the issue number #nn in the pull request when you have something ready to share (this lets Github link back to the issue automatically).

## GitHub Flow

We have chosen to use the Github Flow workflow as descibed here: (http://scottchacon.com/2011/08/31/github-flow.html).

* Anything in the master branch is deployable
* To work on something new, create a descriptively named branch off of master (ie: new-oauth2-scopes)
* Commit to that branch locally and regularly push your work to the same named branch on the server
* When you need feedback or help, or you think the branch is ready for merging, open a pull request
* After someone else has reviewed and signed off on the feature, you can merge it into master
* Once it is merged and pushed to ‘master’, you can and should deploy immediately

## Unit tests

We are using [TravisCi](https://travis-ci.org/makehackvoid/govhack2014) to run tests whenever a pull request is submitted or a commit is made.

##Git remotes for testing

Fork the repository to your own account so that you can make pull requests. Clone it to your computer. 

On your computer add a new remote 'upstream' so you can update your fork from the original makehackvoid project. If you want to be able to see (fetch) and pull down pull requests from the original makehackvoid project for testing, add a second fetch line to .git/config
```fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*```

In .git/config I have:

```
[remote "upstream"]
    url = https://github.com/makehackvoid/govhack2014.git
    fetch = +refs/heads/*:refs/remotes/upstream/*
    fetch = +refs/pull/*/head:refs/remotes/upstream/pr/*
```
