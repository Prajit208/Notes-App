const API="http://127.0.0.1:8000/notes"
const displayNotesEl=document.getElementById('notes')

async function loadNotes(){
    const response=await fetch(API+"/")
    const notes= await response.json()
    console.log(notes.length)
    displayNotesEl.textContent=''

    for(const n in notes){//n is index
        const noteEl=document.createElement('div');
        noteEl.className='note';
        const titleEl=document.createElement('input');
        const contentEl=document.createElement('textarea');

        titleEl.id='title'+notes[n].id
        contentEl.id='content'+notes[n].id
        
        const deleteEl=document.createElement('button');
        deleteEl.textContent='Delete';
        deleteEl.className='delete-btn';
        deleteEl.addEventListener('click',function(){
            deleteNote(notes[n].id)
        })

    
        //auto save feature
        let timer;
        titleEl.addEventListener('input',function(){
            clearTimeout(timer);
            timer=setTimeout(function(){
                editNote(notes[n].id)
            },2000)
        })
        contentEl.addEventListener('input',function(){
            clearTimeout(timer);
            timer=setTimeout(function(){
                editNote(notes[n].id)
            },2000)
        })

        titleEl.value=notes[n].title;
        contentEl.value=notes[n].content
        noteEl.appendChild(titleEl)
        noteEl.appendChild(contentEl)
        noteEl.appendChild(deleteEl)
        displayNotesEl.appendChild(noteEl)
    }
}
loadNotes()

async function writeNotes(){
    const titleEl=document.getElementById('title')
    const contentEl=document.getElementById('content')
    const title=titleEl.value
    const content=contentEl.value

    
    try{
        const response=await fetch(API+"/",{
        method:"POST",
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({title:title,content:content})})

        if(!response.ok){
            throw new Error(`HTTP error! Status: ${response.status}`)
        }
        const newNote=await response.json()
        loadNotes()
        titleEl.value=''
        contentEl.value=''
        console.log(`success:`,newNote)
    }
    catch(error){
        console.log('error: ', error)
    }
    
}
const form=document.getElementById('write-note')
form.addEventListener('submit',function(event){
    event.preventDefault();
    writeNotes()
});

async function deleteNote(note_id){
    try{
    const response=await fetch(API+"/"+note_id,{
        method:`DELETE`
    });
    if(!response.ok){
        throw new Error(`HTTP error! Status: ${response.status}`)

    }
    loadNotes()
}
    catch(error){
        console.log('error: ', error)
    }
}

async function editNote(note_id){
    const titleEl=document.getElementById('title'+note_id)
    const contentEl=document.getElementById('content'+note_id)
    const title=titleEl.value;
    const content=contentEl.value;

    try{
        const response=await fetch(API+"/"+note_id,{
            method:"PUT",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({title:title,content:content})
        });
        if(!response.ok){
            throw new Error(`HTTP error! Status: ${response.status}`)
        }
        const edited_note= await response.json()
        console.log(`success:`,edited_note)
        
    }
    catch(error){
        console.log("Error: ",error)
    };
    
}
    
