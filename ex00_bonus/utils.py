# utils entities used within both programs.
import pandas as pd
import matplotlib.pyplot as plt

filename_contants = "constants.csv"
filename_dataset = "data.csv"
header_col0 = "theta0"
header_col1 = "theta1"


err_msg_fileNoExist = "Error! File (constant.csv or data.csv) is missing"
err_msg_modNotFound = "Error! Missing modules (pandas)"
err_msg_invalidUsrInput = "Error! Invalid input. Enter numbers only."

def GetDataSet():
    df = pd.read_csv(filename_dataset)
    return ((df['km']), (df['price']))




def get_stats():
    mileage, price = GetDataSet()
    return mileage.mean(), mileage.std()




def estimate_price(mileage, theta0, theta1):
    """
    estimatePrice(mileage) = θ0 + (θ1 * mileage)
    """
    price = theta0 + (theta1 * mileage)
    return price




def normalize_dataset(data):
    """
    Normalise the dataset (x - x_mean)/x_std
    """
    mean = data.mean()
    std  = data.std()
    data = (data - mean) / std
    return data




def denormalize_dataset(data):
    """
    Normalise the dataset (x - x_mean)/x_std
    """
    mean = data.mean()
    std  = data.std()
    data = (data * std) + mean
    return data
    



def halt_descent(curr_mse, prev_mse):
    retcode = False
    
    if (curr_mse > 0 and prev_mse > 0):
        if (curr_mse > prev_mse):
            retcode = True
    return retcode




def compute_mse(m,mileage, price, theta0, theta1):
    return ((1/m)) * sum((estimate_price(mileage, theta0, theta1) - price)**2)




def save_constants(theta0, theta1):
    fileObj = open(filename_contants, 'w')
    fileObj.write("%s,%s" %(header_col0, header_col1))
    fileObj.write("\n%f,%f" %(theta0, theta1))




def show_stats_header():
    print("%15s; %15s; %15s; %15s; %25s" %("tmp_t0", "tmp_t1", "t0", "t1", "mse"))




def show_iteration_stats(iter_idx, t_t0, t_t1, t0, t1, mse):
    print("iteration(%d): %15.4e; %15.4e; %15.4e; %15.4e; %25.5e" 
           %(iter_idx, t_t0, t_t1, t0, t1, mse))




def get_constants():
    df = pd.read_csv(filename_contants)
    theta0 = (df['theta0'][0])
    theta1 = (df['theta1'][0])
    return theta0, theta1



def show_plot(mileage, price, theta0, theta1):
    # normalise the mileage
    norm_mileage = normalize_dataset(mileage)
    plt.scatter(mileage, price)

    # note that the normalised mileage is used to compute the predicted price
    plt.plot(mileage, estimate_price(norm_mileage, theta0, theta1), color='red')
    plt.show()
