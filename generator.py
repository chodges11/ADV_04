sample_list = ['Potty', 'Cat', 'Potty', 'Dog', 'Friend', 'House']

def test_generator(generator_list):
    for number in generator_list:
        i = (yield number)
        print(f"Value is {i}")
