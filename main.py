import choose_input_type
'''
possible instructions!
add int<apartment> str<type> int<amount>
remove int<apartment>
remove int<start apartment> to int<end apartment>
remove str<type>
replace int<apartment> str<type> with int<amount>
list
list int<apartment>
list str[ < | = | > ] int<amount>
sum str<type>
max int<apartment>
sort int<apartment
sort str<type
filter str<type>
filter int<value>
undo int<steps>
'''

if __name__ == '__main__':
    choose_input_type.choose_input()
