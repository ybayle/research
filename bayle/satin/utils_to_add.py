
def compare_results(groundtruths_file, dir_pred):
    """Description of compare_results

    groundtruths_file: path to file containing the ground truths and identifiers
    dir_pred: directory containing one prediction file per algorithm
    """
    utils.print_success("Comparing results")
    predictions_files = os.listdir(dir_pred)
    gts = read_item_tag(groundtruths_file)
    for pred_file in predictions_files:
        algo_name = pred_file.split("/")[-1][:-4]
        utils.print_info(algo_name)
        test_groundtruths = []
        predictions = []
        with open(dir_pred + pred_file, "r") as filep:
            for line in filep:
                row = line[:-1].split(",")
                isrc_id = row[0]
                if isrc_id in gts:
                    test_groundtruths.append(gts[isrc_id])
                    predictions.append(float(row[1]))

        print("Accuracy : " + str(accuracy_score(test_groundtruths, predictions)))
        print("F-score  : " + str(f1_score(test_groundtruths, predictions, average="weighted")))
        print("Precision: " + str(precision_score(test_groundtruths, predictions, average=None)))
        print("Recall   : " + str(recall_score(test_groundtruths, predictions, average=None)))
        print("F-score " + str(f1_score(test_groundtruths, predictions, average=None)))
