本資料夾包含以下程式：
- concatenate.py: 將training與public合併為新的training data
- add_time.py: 新增時間相關feature: hour, minute, second, hour
- add_myf.py: 新增fequc, fequ0兩個features
- add_cano.py: 新增cano相關feature: cano_all_combined, cano_5, cano_20
- add_more_features.py: 新增cano_locdt, cano_locdt_freq, cano_locdt_sigma三個features
- add_conam.py: 新增cano_locdt_conam_max, cano_locdt_conam_min兩個features
- fill_null_train: 填入train data的null value
- fill_null_test: 填入test data的null value
- group.py: 將類別型資料使用target encoding填入該類別盜刷的比例