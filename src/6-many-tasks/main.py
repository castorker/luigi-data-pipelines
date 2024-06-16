import luigi
from luigi import Task, LocalTarget, WrapperTask


# sales summaries


class DownloadSalesData(Task):
    def output(self):
        return LocalTarget('all_sales.csv')

    def run(self):
        with self.output().open('w') as f:
            print('Portugal,May,500', file=f)
            print('Netherlands,May,620', file=f)
            print('Portugal,June,750', file=f)
            print('Netherlands,June,380', file=f)


class GetPortugalSales(Task):
    def requires(self):
        return DownloadSalesData()

    def output(self):
        return LocalTarget('portugal_sales.csv')

    def run(self):
        with self.output().open('w') as out:
            with self.input().open() as f:
                for line in f:
                    if line.startswith('Portugal'):
                        out.write(line)


class SummarizePortugalSales(Task):
    def requires(self):
        return GetPortugalSales()

    def output(self):
        return LocalTarget('summary_portugal_sales.csv')

    def run(self):
        total = 0
        with self.input().open() as f:
            for line in f:
                aa = line.split(',')
                total += float(aa[2])

        with self.output().open('w') as out:
            out.write(str(total))


class GetNetherlandsSales(Task):
    def requires(self):
        return DownloadSalesData()

    def output(self):
        return LocalTarget('netherlands_sales.csv')

    def run(self):
        with self.output().open('w') as out:
            with self.input().open() as f:
                for line in f:
                    if line.startswith('Netherlands'):
                        out.write(line)


class SummarizeNetherlandsSales(Task):
    def requires(self):
        return GetNetherlandsSales()

    def output(self):
        return LocalTarget('summary_netherlands_sales.csv')

    def run(self):
        total = 0
        with self.input().open() as f:
            for line in f:
                aa = line.split(',')
                total += float(aa[2])

        with self.output().open('w') as out:
            out.write(str(total))


class Final(WrapperTask):
    def requires(self):
        return [SummarizePortugalSales(),
                SummarizeNetherlandsSales()]


if __name__ == '__main__':
    luigi.run(['Final'])
    
    