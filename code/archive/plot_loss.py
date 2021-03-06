from __future__ import division

import matplotlib.pyplot as plt
import numpy as np
import re


log_file = open("./log/log_26_lrn_0p02_data_AwA_match_1_adagrad.txt")

epoch = []
epoch_acc = []
train_gen_loss = []
train_disc_loss = []
#val_gen_loss = []
#val_disc_loss = []
test_top_1_accuracy = []
test_top_5_accuracy = []

for line in log_file:
	if line[0] == "T":
		pass
	else:
		#_epoch, _train_gen_loss, _train_disc_loss, _val_gen_loss, _val_disc_loss, _test_top_1_accuracy, _test_top_5_accuracy, _, _ = re.split("\t", line)
		_epoch, _train_gen_loss, _train_disc_loss, _test_top_1_accuracy, _test_top_5_accuracy, _, _ = re.split("\t", line)
		epoch.append(int(_epoch))
		train_gen_loss.append(float(_train_gen_loss))
		train_disc_loss.append(float(_train_disc_loss))
		#val_gen_loss.append(float(_val_gen_loss))
		#val_disc_loss.append(float(_val_disc_loss))
		if _test_top_1_accuracy == "N/A":
			pass
		else:
			epoch_acc.append(int(_epoch))
			test_top_1_accuracy.append(float(_test_top_1_accuracy))
			test_top_5_accuracy.append(float(_test_top_5_accuracy))


plt.figure(1)
plt.plot(epoch, train_gen_loss, "k-", label = "train gen loss")
plt.plot(epoch, train_disc_loss, "r-", label = "train disc loss")
#plt.plot(epoch, val_gen_loss, "k--", label = "val gen loss")
#plt.plot(epoch, val_gen_loss, "r--", label = "val disc loss")
#plt.xlim([-1, 50])
#plt.ylim([-0.5, 1.5])
plt.legend()
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.savefig('./log/fig_26_lrn_0p02_data_AwA_match_1_adagrad.pdf')

"""
plt.figure(2)
plt.plot(epoch, train_gen_loss, "k-", label = "train gen loss")
plt.plot(epoch, train_disc_loss, "r-", label = "train disc loss")
#plt.plot(epoch, val_gen_loss, "k--", label = "val gen loss")
#plt.plot(epoch, val_gen_loss, "r--", label = "val disc loss")
#plt.xlim([-1, 50])
plt.ylim([-0.5, 1.5])
plt.legend()
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.savefig('./log/fig_10_lrn_0p02_data_1202.pdf')


plt.figure(3)
#plt.plot(epoch, train_gen_loss, "k-", label = "train gen loss")
#plt.plot(epoch, train_disc_loss, "r-", label = "train disc loss")
plt.plot(epoch, val_gen_loss, "k-", label = "val gen loss")
plt.plot(epoch, val_disc_loss, "r-", label = "val disc loss")
#plt.xlim([-1, 50])
plt.ylim([-0.5, 1.5])
plt.legend()
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.savefig('./log/fig_10_lrn_0p02_data_1202_val.pdf')
"""


plt.figure(2)
plt.plot(epoch_acc, test_top_1_accuracy, "k-", label = "test accuracy")
#plt.plot(epoch, val_gen_loss, "k--", label = "val gen loss")
#plt.plot(epoch, val_gen_loss, "r--", label = "val disc loss")
#plt.xlim([-1, 50])
#plt.ylim([-0.5, 1.5])
plt.legend(loc = 'lower right')
plt.xlabel("Epoch")
plt.ylabel("Test accuracy")
plt.savefig('./log/fig_26_lrn_0p02_data_AwA_match_1_adagrad_accuracy.pdf')


