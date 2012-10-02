# CSScomb for Sublime Text 2

## About

Tool for sorting CSS properties in specific order.

* Sorting CSS properties. The order of properties in the help of professionals
* Setting the order of CSS properties. Use the order to which you are accustomed to
* Parsing CSS in the tags ```<style>```, ```style="..."``` attribute. CSScomb find a CSS-code to other languages and will sort it
* Formatting style sheets does not change. Work as a singleline and multiline CSS
* Separation of CSS properties for the group. Separate groups of empty string if you want
* Full support CSS2/CSS2.1/CSS3/CSS4 ;) CSScomb ready for the advanced CSS-code

The algorithm of CSScomb simulates web-technologists actions upon working with
CSS-code to the limit. Usually to re-order code you move lines over each other
considering comments in the code, multilines records of property values, hacks
and everything that could be found in the real file. CSScomb reproduces these
actions for you. This means that the parser "thinks" as a person editing the
text, not as a blind robot parsing CSS.

For more info, online demo and tests see [http://csscomb.com/](csscomb.com)


## The Requirements

CSScomb is written in pure PHP, without any external libraries or dependencies.
See details at [wiki](https://github.com/miripiruni/CSScomb/wiki/Requirements).


##Plugin usage

Select code and press ```ctrl+shift+c```


## Issues & bugs

[CSScomb tracker](https://github.com/miripiruni/CSSComb/issues)


## Authors

CSScomb core: [miripiruni](mailto:mail@csscomb.ru)

Sublime plugin: [i-akhmadullin](https://github.com/i-akhmadullin)
