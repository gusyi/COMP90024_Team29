//map
function(doc){
    if(doc.created_at){
        emit(doc.created_at, 1);
    }
}

//reduce
function(keys, values, rereduce){
    return sum(values);
}