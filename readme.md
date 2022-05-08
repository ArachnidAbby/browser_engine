# PYOBE

`PYthon Open Browser Engine`

PYOBE is browser engine I'm developing for fun that simply handles rendering a page as an image as well as running javascript and python within the `<script>` tag.

Yes, python is supported by default and will have access to **everything** javascript has access to.
*currently we are the design phases..... so don't expect everything to be done yet*

## What we do differently than others

- Completely open source
- Customizable functionality, styling, etc
- not locked down to anything. You don't even need a UI. You could be single-threaded, multithreaded, async. Do whatever you like
- Built-in python support with access to the DOM and CCSOM. This is used just like JS normally.... but now you wont need stuff like pyodide.
- Ability to add custom tags
- It's made in python, who doesn't love python? Well... in all seriousness.... this *could* be an innapropriate use of python lol...

## Our values

- we will always try to keep this project opensource
- Trying to keep up-to-date with modern practices in project management/organization
- Ensure the web stays an open standard. We are open to all forms of crazy ideas as long as they make sense.
- depend on as little as possible. We want to keep this light-weight and completely open to all forms of projects.
- Ensure that the package can be used in a variety of different ways, regardless of the way someone sets up their own browser project.

# Open-Source Infomation

## What rules do I need to follow to get my pull request accepted?

- Type annotations in your code!
- basic doc-strings explaining the functionality of your functions, classes, etc!
- Documentation via Sphinx for any new user-facing classes, functions, globals, etc.
- use of ABC for anything that will likely be extended/overloaded by user-made classes.
- use of `__slots__` if possible. This increases class performance.
- Added files, classes, functions, etc make sense where you placed them in the code.
- Following PEP8 conventions.
- If you can, use bite-sized names for functions, classes, modules. This makes things less wordy.
- Don't excessively use the Factory Pattern or I will send you to OOP jail.
- use of underscores at the beginning of 'private' class attributes. `ex: self._id = 0`
- doc-strings in modules that explains the functionality of a module. This helps users and developers.
- use of comments where it may not be completely clear why you are doing something
- add your name to module `__authors__` list if you make a significant change. Also update the `__version__`

- A clear reason to make the specified change.
- Having patience for a slow review process.
- The ability to explain yourself and take criticism.


## Rules for reviewing other people's pull-requests

- Don't be a dick, be constructive!
- If the request doesn't follow the previoulsy mentioned rules then point the requester in the right direction to fix it. If they have good reasoning to break the above rules, wait for a trusted community member to handle it.
- Must be able to take criticism.
- Don't be a snob, you are not better than anyone else.
- Be beginner friendly and be willing to explain ***anything***
- Don't be childish if your decision isn't the one the community ends up with.

## Modifications to PEP8 that will be made or are acceptable to make

- Indintation does not need to align with opening delimiter; an extra 4 spaces is sufficient.

- No Maximum line length, just use your own judgement here.

- use `__authors__ = []` instead of `__author__ = ''`

- `__version__` wil be incrimented using semantic versioning.

