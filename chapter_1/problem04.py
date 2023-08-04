# numerical derivatives

import numpy as np
import matplotlib.pyplot as plt

def forward_difference_method(x, h, f):
    x0 = x
    f1 = f(x)
    x = x0 + h
    f2 = f(x)
    return (f2 - f1)/h
def central_difference_method(x, h, f):
    x0 = x
    x = x0 - h/2
    f1 = f(x)
    x = x0 + h/2
    f2 = f(x)
    return (f2 - f1)/h
def central_difference_method_d2(x, h, f):
    x0 = x
    x = x0 + h
    f1 = f(x)
    x = x0 - h
    f2 = f(x)
    x = x0
    f3 = f(x)
    return (f1 + f2 - 2*f3)/h**2
# create derivativeDict
# analytic derivation
def getDerAn(func, x):
    der = {
        "1" : func(x[0]),
        "2" : func(x[1]),
        "3" : func(x[2]),
    }
    return der
# numerical derivation
def getDerNum(vfunc, func, x, h):
    der = {
        "1" : vfunc(x[0], h, func),
        "2" : vfunc(x[1], h, func),
        "3" : vfunc(x[2], h, func),
    }
    return der
def getError(der_num, der_an):
    error = {
        "1" : np.absolute(der_num["1"] - der_an["1"]),
        "2" : np.absolute(der_num["2"] - der_an["2"]),
        "3" : np.absolute(der_num["3"] - der_an["3"]),
    }
    return error
def getLogError(error):
    log_error = {
        "1" : np.log10(np.absolute(error["1"])),
        "2" : np.log10(np.absolute(error["2"])),
        "3" : np.log10(np.absolute(error["3"]))
    }
    return log_error
def plotError(h=0.1, error1=None, error2=None, title="Hey", x_label="x", y_label="y", color=["r","b"], legend=None):
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.plot(h, error1, color[0])
    if error2 != None:
        plt.plot(h, error2, color[1])
        plt.legend(legend)
    plt.show()
def printResult(method, x, der_cos, der_exp, error_cos, error_exp):
    print(f"{method} difference method")
    print("-------------------------")
    print("function = cos(x)")
    print(f"der(cos)(x = {x[0]}) = ", der_cos["1"])
    print("error = ", error_cos["1"])
    print(f"der(cos)(x = {x[1]}) = ", der_cos["2"])
    print("error = ", error_cos["2"])
    print(f"der(cos)(x = {x[2]}) = ", der_cos["3"])
    print("error = ", error_cos["3"])
    print("function = exp(x)")
    print(f"der(exp)(x = {x[0]}) = ", der_exp["1"])
    print("error = ", error_exp["1"])
    print(f"der(exp)(x = {x[1]}) = ", der_exp["2"])
    print("error = ", error_exp["2"])
    print(f"der(exp)(x = {x[2]}) = ", der_exp["3"])
    print("error = ", error_exp["3"])
# 1
def questionSet1():
    # vectorize functions
    v_forward_difference_method = np.vectorize(forward_difference_method)
    v_central_difference_method = np.vectorize(central_difference_method)

    h = np.linspace(1e-14, 100, 5000)
    x = [0.1, 1, 100]
    # cos analytical derivative
    der_cos = getDerAn(func=np.sin, x=x)
    # exp analytical derivative
    der_exp = getDerAn(func=np.exp, x=x)
    # cosine derivative forward difference method
    derF_cos = getDerNum(vfunc=v_forward_difference_method, func=np.cos, x=x, h=h)
    derF_cos_error = getError(der_num=derF_cos, der_an=der_cos)
    # exp derivative forward difference method
    derF_exp = getDerNum(vfunc=v_forward_difference_method, func=np.exp, x=x, h=h)
    derF_exp_error = getError(der_num=derF_exp, der_an=der_exp)
    # cosine derivative central difference method
    derC_cos = getDerNum(vfunc=v_central_difference_method, func=np.cos, x=x, h=h)
    derC_cos_error = getError(der_num=derC_cos, der_an=der_cos)
    # exp derivative cerntral difference method
    derC_exp = getDerNum(vfunc=v_central_difference_method, func=np.exp, x=x, h=h)
    derC_exp_error = getError(der_num=derC_exp, der_an=der_exp)

    # plotdata

    # cos(x)
    plot_data = {
        "title" : f"d/dx[cos(x)] at x = {x[0]}", "x_label" : "h", "y_label" : "error",
        "color" : ["r", "b"] , "legend" : ['forward-cos-error', 'central-cos-error']
    }
    plotError(h=h, error1=derF_cos_error["1"], error2=derC_cos_error["1"], **plot_data)
    plot_data["title"] = f"d/dx[cos(x)] at x = {x[1]}"
    plotError(h=h, error1=derF_cos_error["2"], error2=derC_cos_error["2"], **plot_data)
    plot_data["title"] = f"d/dx[cos(x)] at x = {x[2]}"
    plotError(h=h, error1=derF_cos_error["3"], error2=derC_cos_error["3"], **plot_data)

    # exp(x)
    plot_data["title"] = f"d/dx[exp(x)] at x = {x[0]}"
    plotError(h=h, error1=derF_exp_error["1"], error2=derC_exp_error["1"], **plot_data)
    plot_data["title"] = f"d/dx[exp(x)] at x = {x[1]}"
    plotError(h=h, error1=derF_exp_error["2"], error2=derC_exp_error["2"], **plot_data)
    plot_data["title"] = f"d/dx[exp(x)] at x = {x[2]}"
    plotError(h=h, error1=derF_exp_error["3"], error2=derC_exp_error["3"], **plot_data)

    # log data
    log_h = np.log10(h)
    log_derF_cos_error = getLogError(derF_cos_error)
    log_derC_cos_error = getLogError(derC_cos_error)
    log_derF_exp_error = getLogError(derF_exp_error)
    log_derC_exp_error = getLogError(derC_exp_error)

    # cos(x) log
    plot_data = {
        "title" : f"d/dx[cos(x)] at x = {x[0]}", "x_label" : "log(h)", "y_label" : "log(error)",
        "color" : ["r", "b"] , "legend" : ['log forward-cos-error', 'log central-cos-error']
    }
    plotError(h=log_h, error1=log_derF_cos_error["1"], error2=log_derC_cos_error["1"], **plot_data)
    plot_data["title"] = f"d/dx[cos(x)] at x = {x[1]}"
    plotError(h=log_h, error1=log_derF_cos_error["2"], error2=log_derC_cos_error["2"], **plot_data)
    plot_data["title"] = f"d/dx[cos(x)] at x = {x[2]}"
    plotError(h=log_h, error1=log_derF_cos_error["3"], error2=log_derC_cos_error["3"], **plot_data)

    # exp(x)
    plot_data["title"] = f"d/dx[exp(x)] at x = {x[0]}"
    plotError(h=log_h, error1=log_derF_exp_error["1"], error2=log_derC_exp_error["1"], **plot_data)
    plot_data["title"] = f"d/dx[exp(x)] at x = {x[1]}"
    plotError(h=log_h, error1=log_derF_exp_error["2"], error2=log_derC_exp_error["2"], **plot_data)
    plot_data["title"] = f"d/dx[exp(x)] at x = {x[2]}"
    plotError(h=log_h, error1=log_derF_exp_error["3"], error2=log_derC_exp_error["3"], **plot_data)

    # print result
    printResult(method="Forward", x=x, der_cos=derF_cos, der_exp=derF_exp, error_cos=derF_cos_error, error_exp=derF_exp_error)
    printResult(method="Central", x=x, der_cos=derC_cos, der_exp=derC_exp, error_cos=derC_cos_error, error_exp=derC_exp_error)
# 2
def questionSet2():
    # vectorize functions
    v_central_difference_method_d2 = np.vectorize(central_difference_method_d2)

    h = np.linspace(1e-14, np.pi/10, 100)
    x = [0.1, 1, 100]
    # cos analytical derivative
    der_cos_d2 = getDerAn(func=np.cos, x=x)
    # cosine derivative Central difference method
    derC_cos_d2 = getDerNum(vfunc=v_central_difference_method_d2, func=np.cos, x=x, h=h)
    derC_cos_error = getError(der_num=derC_cos_d2, der_an=der_cos_d2)
    plot_data = {
        "title" : f"Central Differece d2/dx2[cos(x)] at x = {x[0]}", "x_label" : "h", "y_label" : "error",
    }
    plotError(h=h, error1=derC_cos_error["1"], **plot_data)
    plot_data["title"] = f"Central Differece d2/dx2[cos(x)] at x = {x[1]}"
    plotError(h=h, error1=derC_cos_error["2"], **plot_data)
    plot_data["title"] = f"Central Differece d2/dx2[cos(x)] at x = {x[2]}"
    plotError(h=h, error1=derC_cos_error["3"], **plot_data)

def main():
    # questionSet1()
    questionSet2()

if __name__ == "__main__":
    main()