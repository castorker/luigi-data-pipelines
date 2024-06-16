import luigi
from luigi import Task, LocalTarget
from luigi.contrib.s3 import S3Target


# parallel downloads


class DownloadOrders(Task):
    def output(self):
        return LocalTarget('orders.csv')

    def run(self):
        with self.output().open('w') as f:
            f.write('Target created - Task done!')


class DownloadSales(Task):
    def output(self):
        return LocalTarget('sales.csv')

    def run(self):
        with self.output().open('w') as f:
            f.write('Target created - Task done!')


class DownloadInventory(Task):
    def output(self):
        return LocalTarget('inventory.csv')

    def run(self):
        with self.output().open('w') as f:
            f.write('Target created - Task done!')


class UploadToAwsS3(Task):
    def requires(self):
        return [DownloadOrders(),
                DownloadSales(),
                DownloadInventory()]

    def output(self):
        return S3Target('s3://luigiawsbucket/data-pipelines-output/upload.txt')

    def run(self):
        with self.output().open('w') as f:
            f.write('Target created - Task done!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    luigi.run(['UploadToAwsS3', '--local-scheduler'])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/