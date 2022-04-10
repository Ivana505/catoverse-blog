# TESTING 

Return to the [README.md](README.md)

## Validator testing and browser compatibility
- I have tested Python code with - [PEP8 validator](http://pep8online.com/), first testing showed errors.

![validation_settings](documents/testing/pep8_settings.png)

![validation_urls](documents/testing/pep8_urls.png)

- All errors have been corrected

![validation_settings](documents/testing/pep8_errors_resolved.png)


- HTML Validation was made with ![W3 validator](https://validator.w3.org/)

![validation_settings](documents/testing/html_validator_base.png)
![validation_settings](documents/testing/html_validator_index.png)
![validation_settings](documents/testing/html_validator_blog_post.png)

- CSS Validation was made with Jigsaw ![W3 validator](https://jigsaw.w3.org/)

![validation_css](documents/testing/css_validation.png)


## Accessibility
- I have confirmed that the Website is accessible by inspecting it in Lighthouse on the [Google Chrome](https://www.google.com/chrome/?brand=FKPE&gclid=EAIaIQobChMIqOPWwuu69AIVFeDtCh1CEgKGEAAYASAAEgKvwvD_BwE&gclsrc=aw.ds) Dev tools.
    
Result for desktop 
 - Performance for the desktop version 

![desktop](documents/testing/lighthouse_desktop.png)

Result for mobile devices
- Performance for mobile devices 

![mobile](documents/testing/lighthouse_mobile.png)

## Bugs

### Solved
- All problems from [Gitpod](https://www.gitpod.io/) from the image have been resolved. Most of them were indentation bugs and lines of code too long.

![solved bugs](documents/testing/python_errors.png)

- Bad Request (400) on [Herokuapp](https://dashboard.heroku.com/) was resolved by adding CSRF.

![solved bugs](documents/testing/herokuapp_error.png)

![solved bugs](documents/testing/csrf_added.png)


- Error "GET / HTTP/1.1" 500 98967 on [Gitpod](https://www.gitpod.io/) was resolved by moving file in the correct folder.

![solved bugs](documents/testing/error_index_page.png)

- Error Improperly Configured was resolved by adding space to settings.DATABASES.

![solved bugs](documents/testing/improperly_configured.png)

- Error Invalid Host Error was corrected by adding allowed host on settings.py.

![solved bugs](documents/testing/invalid_host_error.png)

### Unsolved bugs
- Unsolved problem which relates to ms-toolsai.jupyter extension not bein synched and not added in .gitpod.yml. I have checked Slack community and this is known issue which we can ignore.
- This is also part of the repository cloned for the project that should not be touched.

![unsolved bug](documents/testing/unsolved_bugs.png)

- Unsolved bugs which I could not resolve are the HTML validation errors 

