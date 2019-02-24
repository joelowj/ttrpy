## Code of Conduct

Everyone participating in the ttrpy community, and in particular in our
issue tracker, and pull requests, is expected to treat other people with respect
and more generally to follow the guidelines articulated in the [Python Community Code of
Conduct](https://www.python.org/psf/codeofconduct/).

First Time Contributors
-----------------------

ttrpy appreciates your contribution! If you are interested in helping improve
ttrpy, there are several ways to get started:

* Contributing to [typeshed](https://github.com/python/typeshed/issues) is a great way to
become familiar with Python's type syntax.
* Ask on [the issue tracker](https://github.com/joelowj/ttrpy/issues) about good beginner issues.

Submitting Changes
------------------

Even more excellent than a good bug report is a fix for a bug, or the
implementation of a much-needed new feature. (*)  We'd love to have
your contributions.

(*) If your new feature will be a lot of work, we recommend talking to
    us early -- see below.

We use the usual GitHub pull-request flow, which may be familiar to
you if you've contributed to other projects on GitHub.  For the mechanics,
see [GitHub's own documentation](https://help.github.com/articles/using-pull-requests/).

Anyone interested in ttrpy may review your code.  One of the ttrpy core
developers will merge your pull request when they think it's ready.
For every pull request, we aim to promptly either merge it or say why
it's not yet ready; if you go a few days without a reply, please feel
free to ping the thread by adding a new comment.

Preparing Changes
-----------------

Before you begin: if your change will be a significant amount of work
to write, we highly recommend starting by opening an issue laying out
what you want to do.  That lets a conversation happen early in case
other contributors disagree with what you'd like to do or have ideas
that will help you do it.

The best pull requests are focused, clearly describe what they're for
and why they're correct, and contain tests for whatever changes they
make to the code's behavior.  As a bonus these are easiest for someone
to review, which helps your pull request get merged quickly!

Also, do not squash your commits after you have submitted a pull request, as this
erases context during review. We will squash commits when the pull request is merged.


Core developer guidelines
-------------------------

Core developers should follow these rules when processing pull requests:

* Always wait for tests to pass before merging PRs.
* Use "[Squash and merge](https://github.com/blog/2141-squash-your-commits)"
  to merge PRs.
* Delete branches for merged PRs (by core devs pushing to the main repo).
* Edit the final commit message before merging to conform to the following
  style (we wish to have a clean `git log` output):
  * When merging a multi-commit PR make sure that the commit message doesn't
    contain the local history from the committer and the review history from
    the PR. Edit the message to only describe the end state of the PR.
  * Make sure there is a *single* newline at the end of the commit message.
    This way there is a single empty line between commits in `git log`
    output.
  * Split lines as needed so that the maximum line length of the commit
    message is under 80 characters, including the subject line.
  * Capitalize the subject and each paragraph.
  * Make sure that the subject of the commit message has no trailing dot.
  * Use the imperative mood in the subject line (e.g. "Fix typo in README").
  * If the PR fixes an issue, make sure something like "Fixes #xxx." occurs
    in the body of the message (not in the subject).
  * Use Markdown for formatting.
