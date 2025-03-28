
import utils
# Note that for this application
# y     = (m      * x)       + c
# price = (theta1 * mileage) + theta0
# theta0  -> c
# theta1  -> m
# price   -> y
# mileage -> x

theta0 = 0
theta1 = 0
iteration = 2000
learning_rate = 0.01
mse_curr = 0
mse_prev = 0


def PerformGradientDescend():
    global theta0
    global theta1
    global mse_curr
    global mse_prev
    mileage_orig, price = utils.GetDataSet()
    mileage_norm = utils.normalize_dataset(mileage_orig)

    # Number of rows in dataset
    m = (len(mileage_norm))
    
    
    #utils.show_stats_header()
    for iter_step in range(iteration):
        # compute the predicted price.
        price_p = utils.estimate_price(mileage_norm, theta0, theta1)

        tmp_theta0 = (1.0/m) * learning_rate * sum((price_p - price))
        tmp_theta1 = (1.0/m) * learning_rate * sum((price_p - price) * mileage_norm)

        # update cost 
        mse_prev = mse_curr
        mse_curr = utils.compute_mse(m, mileage_norm, price, theta0, theta1)
        if (utils.halt_descent(mse_curr, mse_prev)): break
        #utils.show_iteration_stats(iter_step, tmp_theta0, tmp_theta1, theta0, theta1, mse_curr)

        #next theta for descend step 
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    
    # Plot data
    utils.show_plot(mileage_orig, price, theta0, theta1)





# Start Program execution
if __name__ == "__main__":
    try:
       PerformGradientDescend()
       utils.save_constants(theta0,theta1)
    except (KeyboardInterrupt):
        print("\nExiting...\n")
    except (FileNotFoundError):
        print(utils.err_msg_fileNoExist)
    except (ModuleNotFoundError):
        print(utils.err_msg_modNotFound)
