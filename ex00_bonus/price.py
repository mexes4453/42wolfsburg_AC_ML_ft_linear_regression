import pandas as pd
import utils


def get_user_input():
    mileage = input("Enter mileage: ")
    # must be numeric and not float
    mileage = int(mileage)
    return mileage




def normalize_input(x):
    x_mean, x_std = utils.get_stats()
    return ( (x - x_mean) / x_std )




def compute_price(mileage):
    """
    estimatePrice(mileage) = θ0 + (θ1 * mileage)
    1. Normalise the user input (x:mileage)
    """
    mileage = normalize_input(mileage)  

    # 2. Retreive the computed constants  
    theta0, theta1 = utils.get_constants()

    # 3. Compute predicted price
    price = theta0 + (theta1 * mileage)

    # 4. Return price to user.
    print("price: %.2f" %float(price))




if __name__ == "__main__":
    try:
        mileage = get_user_input()
        compute_price(mileage)
    except (KeyboardInterrupt):
        print("\nExiting...\n")
    except (FileNotFoundError):
        print(utils.err_msg_fileNoExist)
    except (ModuleNotFoundError):
        print(utils.err_msg_modNotFound)
    except (ValueError):
        print(utils.err_msg_invalidUsrInput)

    






