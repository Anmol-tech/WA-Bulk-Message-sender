import pandas as pd



def CSVloadNumbers(path):
    try:
        df = pd.read_csv(path)
        print('Loading File '+ str(path))
        mobileNumbers = []
        
        for i in df['Mobile Numbers']:
            mobileNumbers.append(str(i))
        status = []
        for i in range(len(mobileNumbers)):
            status.append('Pending...')
        timeList = []
        for i in range(len(mobileNumbers)):
            timeList.append('')
        tableData = {'Mobile Number' : mobileNumbers,
                    'Status' : status,
                    'Time' : timeList
                    }
        return tableData
    except KeyError as e:
        print(e)
        return 'Wrong File Format'
    except FileNotFoundError as e:
        print(e)
        return 'File Not Found Error !'
    



