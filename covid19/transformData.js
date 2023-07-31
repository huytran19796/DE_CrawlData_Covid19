// Load data to Province collection MongoDB
function loadProvince(){
    const bulkInsert = db.province.initializeUnorderedBulkOp();
    const documents = db.raw_data.find({});
  
    // Kiểm tra xem có tài liệu nào để xử lý hay không
    if (documents.count() === 0) {
        print('Không có tài liệu nào để xử lý.');
        return false;
    }
  
    documents.forEach(function (doc) {
        const details = doc.detail;
        details.forEach(function(pro)
        {
            const element = {province : pro.province};
            bulkInsert.find(element).upsert().replaceOne(element);
        })
    });
    bulkInsert.execute();
    return true;
}

// Load data to Detail collection MongoDB
function loadDetail() {
	const bulkInsert = db.detail.initializeUnorderedBulkOp();
	// Get all Documents in 'raw_data' Collection
	const documents = db.raw_data.find({});
	// Process each document
	documents.forEach(function (doc) {
        const details = doc.detail;
        details.forEach(function(pro)
        {
            const province = db.province.findOne({
                province : pro.province
            });
            if (province) {
                pro.province_id = province._id
            }
        })
        const element = {
			date: doc.date,
			month: doc.month,
			year: doc.year,
			sum: doc.sum,
            detail: details
		};
		
		// Upsert into user collection
		bulkInsert.find(element).upsert().replaceOne(element);
	});
	bulkInsert.execute();
	return true;
}

// update Province collection MongoDB
db.detail.updateMany({}, {
    $unset: { "detail.$[].province": "" }
  });
  