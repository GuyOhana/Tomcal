
function all_book_lent() {
    alert("אי-אפשר להשאיל: כל העותקים הושאלו");
  }

function confirmDelete(person_id){
    if(confirm("האם אתה בטוח שברצונך למחוק?"))
      window.location.assign("delete_person/"+ person_id);

}
  