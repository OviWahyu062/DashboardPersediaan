import os
import json
import webbrowser
from threading import Timer
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static')

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data_requests.json')

DEFAULT_DUMMY_DATA = [
    {
        "id": "REQ-2026-001",
        "namaPemohon": "Budi Santoso",
        "tanggal": "2026-03-01",
        "area": "Area 1",
        "site": "5H01 - Site TPK Belawan Domestik",
        "items": [
            {
                "namaBarang": "BEARING BALL 6205-2RS",
                "merk": "SKF",
                "partNumber": "6205-2RS-C3",
                "materialType": "1011 Spare Parts Teknik",
                "materialGroup": "99-111 Bearing,Roller",
                "uom": "PC",
                "kodePlant": "5H01",
                "profitCenter": "53101 - Site TPK Belawan Domestik",
                "storageLocation": "0001",
                "valuationClass": "1103 Suku Cadang Alat Faspel",
                "tkdn": 42.5,
                "dokumentasiUrl": "https://drive.google.com/spec-bearing",
                "dokGambar": ""
            }
        ],
        "status": "APPROVED",
        "approvalL1": {"status": "APPROVED", "by": "Admin Peralatan Area L1", "date": "2026-03-01 10:15", "notes": "Setuju, kebutuhan perbaikan rutin"},
        "approvalL2": {"status": "APPROVED", "by": "Manper Area L2", "date": "2026-03-01 11:00", "notes": "Master data terverifikasi SAP"},
        "approvalL3": {"status": "APPROVED", "by": "Manager Akuntansi L3", "date": "2026-03-01 13:30", "notes": "Akun & valuation class sesuai"},
        "approvalL4": {"status": "APPROVED", "by": "Manager Persediaan L4", "date": "2026-03-01 15:00", "notes": "Kode SAP siap di-generate"}
    },
    {
        "id": "REQ-2026-002",
        "namaPemohon": "Siti Rahmawati",
        "tanggal": "2026-03-05",
        "area": "Area 2",
        "site": "5I03 - Site Pelabuhan Jakarta 1",
        "items": [
            {
                "namaBarang": "CIRCUIT BREAKER 3P 63A",
                "merk": "Schneider",
                "partNumber": "NSX630N",
                "materialType": "1019 Sparepart Electrical",
                "materialGroup": "99-128 MCB,Fuse,Protect Dev",
                "uom": "EA",
                "kodePlant": "5I03",
                "profitCenter": "53203 - Site Pelabuhan Jakarta 1",
                "storageLocation": "0001",
                "valuationClass": "1102 Suku Cadang Inst. Faspel",
                "tkdn": 35.0,
                "dokumentasiUrl": "",
                "dokGambar": ""
            }
        ],
        "status": "PENDING_L2",
        "approvalL1": {"status": "APPROVED", "by": "Admin Peralatan Area L1", "date": "2026-03-05 09:30", "notes": "Sesuai WO maintenance panel"},
        "approvalL2": {"status": "PENDING", "by": "-", "date": "-", "notes": ""},
        "approvalL3": {"status": "PENDING", "by": "-", "date": "-", "notes": ""},
        "approvalL4": {"status": "PENDING", "by": "-", "date": "-", "notes": ""}
    },
    {
        "id": "REQ-2026-003",
        "namaPemohon": "Ahmad Fauzi",
        "tanggal": "2026-03-08",
        "area": "Area 3",
        "site": "5J02 - Site Perak",
        "items": [
            {
                "namaBarang": "OIL FILTER CAT 1R-1808",
                "merk": "Caterpillar",
                "partNumber": "1R-1808",
                "materialType": "1018 Sparepart Mechanical",
                "materialGroup": "99-141 Oil Filter",
                "uom": "PC",
                "kodePlant": "5J02",
                "profitCenter": "53302 - BIMA Site Perak",
                "storageLocation": "0001",
                "valuationClass": "1103 Suku Cadang Alat Faspel",
                "tkdn": 15.0,
                "dokumentasiUrl": "",
                "dokGambar": ""
            },
            {
                "namaBarang": "FUEL FILTER CAT 1R-0750",
                "merk": "Caterpillar",
                "partNumber": "1R-0750",
                "materialType": "1018 Sparepart Mechanical",
                "materialGroup": "99-138 Fuel Filter",
                "uom": "PC",
                "kodePlant": "5J02",
                "profitCenter": "53302 - BIMA Site Perak",
                "storageLocation": "0001",
                "valuationClass": "1103 Suku Cadang Alat Faspel",
                "tkdn": 15.0,
                "dokumentasiUrl": "",
                "dokGambar": ""
            }
        ],
        "status": "PENDING_L1",
        "approvalL1": {"status": "PENDING", "by": "-", "date": "-", "notes": ""},
        "approvalL2": {"status": "PENDING", "by": "-", "date": "-", "notes": ""},
        "approvalL3": {"status": "PENDING", "by": "-", "date": "-", "notes": ""},
        "approvalL4": {"status": "PENDING", "by": "-", "date": "-", "notes": ""}
    }
]

def load_data():
    if not os.path.exists(DATA_FILE):
        save_data(DEFAULT_DUMMY_DATA)
        return DEFAULT_DUMMY_DATA
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return DEFAULT_DUMMY_DATA

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/requests', methods=['GET'])
def get_requests():
    return jsonify(load_data())

@app.route('/api/requests', methods=['POST'])
def create_request():
    req_data = request.json
    data = load_data()
    data.insert(0, req_data)
    save_data(data)
    return jsonify({"success": True, "message": "Request berhasil disimpan", "data": req_data}), 201

@app.route('/api/requests/<req_id>', methods=['PUT'])
def update_request(req_id):
    updated_info = request.json
    data = load_data()
    found = False
    for i, r in enumerate(data):
        if r.get('id') == req_id:
            data[i] = updated_info
            found = True
            break
    if found:
        save_data(data)
        return jsonify({"success": True, "message": f"Request {req_id} berhasil diperbarui"})
    return jsonify({"success": False, "message": "Request ID tidak ditemukan"}), 404

def open_browser():
    webbrowser.open_new_tab('http://127.0.0.1:5000')

if __name__ == '__main__':
    # Membuka browser secara otomatis setelah server menyala
    Timer(1.2, open_browser).start()
    print("=" * 60)
    print("  SISTEM PERMINTAAN MASTER MATERIAL & APPROVAL (PELINDO) ")
    print("  Server berjalan di: http://127.0.0.1:5000")
    print("  Tekan Ctrl+C di terminal VS Code untuk menghentikan server")
    print("=" * 60)
    app.run(debug=True, port=5000, use_reloader=False)
