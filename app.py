from flask import Flask, request, jsonify
import pandas as pd
app = Flask(__name__)

data = {}

@app.route('/upload',methods=['GET', 'POST'])
def upload_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    if file:
        # Читаем CSV-файл с помощью Pandas
        df = pd.read_csv(file)
        
        data[file.filename] = df
        
        return jsonify({'message': 'CSV file uploaded successfully'})

@app.route('/files', methods=['GET'])
def get_file_list():
    file_list = list(data.keys())
    return jsonify({'files': file_list})

@app.route('/data/<filename>', methods=['GET'])
def get_data(filename):
    if filename in data:
        df = data[filename]
        
        filter_column = request.args.get('filter_column')
        filter_value = request.args.get('filter_value')
        sort_by = request.args.getlist('sort_by')
        
        if filter_column and filter_value:
            df = df[df[filter_column] == filter_value]
        
        if sort_by:
            df = df.sort_values(by=sort_by)
        
        result = df.to_dict(orient='records')
        
        return jsonify(result)
    else:
        return jsonify({'error': 'File not found'})
    
@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    if filename in data:
        del data[filename]
        return jsonify({'message': f'File {filename} deleted successfully'})
    else:
        return jsonify({'error': 'File not found'})


if __name__ == '__main__':
    app.run(debug=True)

