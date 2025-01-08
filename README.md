# TextToRegionalEmoji
Just a silly py file to convert a given input text in it's respective regional indicator emojis. 
Great for being annoying in a Discord server.

*Usage*:
```python(3) main.py```

If you want to have the text be in multiple lines such as:

```
Multi
Line
Test
```
You need to split your input via | in the text string.
```
Multi|Line|Test
```
Which transforms into:
```
:regional_indicator_m::regional_indicator_u::regional_indicator_l::regional_indicator_t::regional_indicator_i:
:regional_indicator_l::regional_indicator_i::regional_indicator_n::regional_indicator_e:
:regional_indicator_t::regional_indicator_e::regional_indicator_s::regional_indicator_t:
```
