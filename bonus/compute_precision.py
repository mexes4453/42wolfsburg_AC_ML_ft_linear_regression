import utils


def compute_rSquared():
    mileage_orig, price = utils.GetDataSet()
    theta0, theta1 = utils.get_constants()
    mileage_norm = utils.normalize_dataset(mileage_orig)
    price_pred = utils.estimate_price(mileage_norm, theta0, theta1)
    price_mean = price.mean()
    num = sum((price_pred - price_mean)**2)
    den = sum((price - price_mean)**2)
    return (num/den)
    




# Start Program execution
if __name__ == "__main__":
    try:
       print("Precision: %6.4f\n" %(compute_rSquared()))
    except (KeyboardInterrupt):
        print("\nExiting...\n")
    except (FileNotFoundError):
        print(utils.err_msg_fileNoExist)
