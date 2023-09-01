# ================== git clone ==================== # 
!git clone 'https://github.com/leekyuyoung20230313/1.team.git'


# ================== 디렉토리 설정 ================ # 
%cd '/content/1.team/TimsNet'

# ========== train, val, test 디렉토리 경로; lr, epochs, batch_sizes 설정 ======== #
## sample data 사용 
!python 'times_traintest.py' \
--train_path '/content/1.team/TimsNet/sample_data/s_train1.csv'\
'/content/1.team/TimsNet/sample_data/s_train2.csv'\ 
--val_path '/content/1.team/TimsNet/sample_data/s_val1.csv'\
'/content/1.team/TimsNet/sample_data/s_val2.csv'\ 
--test_path '/content/1.team/TimsNet/sample_data/s_test1.csv'\
'/content/1.team/TimsNet/sample_data/s_test2.csv'\ 
--lr 0.001\ 
--epochs 1\ 
--batch_sizes 2

# ============= 예측한 data points는 현재경로에 results.csv 형태로 저장됨 =========== #
import pandas as pd
result = pd.read_csv('/content/1.team/TimsNet/results.csv')
result
