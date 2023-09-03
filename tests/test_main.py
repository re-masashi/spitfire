import spitfire, pathlib, pprint

def test_main():
    env = spitfire.Environment('.')
    errored = []
    for p in pathlib.Path('.').glob('*'):
        if not p.is_dir() and not str(p).endswith('py') and not str(p).startswith('requirements'):
            v = env.render(str(p), [ {
                    'test_x': 'x var',
                    'test_y': 'y var','test_z': 'z var',
                    'test_empty_list': [],
                    'test_number_list': [1, 2, 3, 4, 5],
                    'test_object_list': [{'id': 1, 'name': 'o1'},
                             {'id': 2, 'name': 'o2'},
                             {'id': 3, 'name': 'o3'},
                    ],
                    'test_dict': {'key1': 1},
                    'test_nested_dict': {'key1': 1, 'd2': {'key1': 1}},
                    'test_range': range,
                    'test_unwebsafe': '<bad tag>',
                    'content_type': 'text/html',
                    'test_str_function':str,
                    'test_whitespaced_dict': {'key 1':1}
                    }], 
                template_name=str(p).split('.')[0])
            assert v == pathlib.Path(
                './output-preserve-whitespace/'+str(p)\
                .split('.')[0].replace('-','_')\
                +'.txt'
            ).open().read()
