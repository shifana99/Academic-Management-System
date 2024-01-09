
    function delete_row(row,id,url){
        
        var box = $("#mb-remove-row");
        box.addClass("open");
        
        box.find(".mb-control-yes").on("click",function(){
            box.removeClass("open");
            $.ajax({
                type: "GET",
                url: url,
                data: {
                    'eid': id
                },
                datatype: "json",
                success: function (data){
                //   alert(data.name)
                $("#"+row).hide("slow",function(){
                    $(this).remove();
                    alert(data.message)
                });
                
                  
                },
                error: function (error){
                    console.log(error);
                }
            });

            
        });
        
    }
    // -----department--------
    function deppop(id){
        document.getElementById("depeditid").value=id;
        document.getElementById("spinner"+id).className="fa fa-spinner";
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/depedit",
            data: {
                'eid': id
            },
            datatype: "json",
            success: function (data){
            //   alert(data.name)
            
              document.getElementById("depname").value=data.deptname;
              document.getElementById("depcode").value=data.deptcode;
              document.getElementById("depstatus").value=data.deptstatus;
              $("#modal_basic").modal('show');
              document.getElementById("spinner"+id).className="fa fa-pencil";
            },
            error: function (error){
                console.log(error);
            }
        });
    }

    //----department update-----
    function updatedep(){
        var id= document.getElementById("depeditid").value;
        var name=document.getElementById("depname").value;
        var code=document.getElementById("depcode").value;
        var status=document.getElementById("depstatus").value
        console.log(id);
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/depupdate",
            data: {
                'eid': id,
                'depname':name,
                'depcode':code,
                'depstatus':status
            },
            datatype: "json",
            success: function (data){
              //alert(data.name)
              alert(data.message)
              location.reload(true)  //refresh code
            },
            error: function (error){
                console.log(error);
                 
            }
        });
    }
    

    // -------designation edit------
    function despop(id){
        document.getElementById("editid").value=id;
        document.getElementById("spinner"+id).className="fa fa-spinner";
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/desedit",
            data: {
                'eid': id
            },
            datatype: "json",
            success: function (data){
            //   alert(data.name)
            
              document.getElementById("desname").value=data.desiname;
              document.getElementById("descode").value=data.desicode;
              document.getElementById("desstatus").value=data.desistatus;
              $("#modal_basic").modal('show');
              document.getElementById("spinner"+id).className="fa fa-pencil";
            },
            error: function (error){
                console.log(error);
            }
        });
    }


// ------designation update-------
function updatedes(){
    var id= document.getElementById("editid").value;
    var name=document.getElementById("desname").value;
    var code=document.getElementById("descode").value;
    var status=document.getElementById("desstatus").value
    console.log(id);
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/desupdate",
        data: {
            'eid': id,
            'desname':name,
            'descode':code,
            'desstatus':status
        },
        datatype: "json",
        success: function (data){
          //alert(data.name)
          alert(data.message)
          location.reload(true)  //refresh code
        },
        error: function (error){
            console.log(error);
             
        }
    });
}

// -----qualification edit------
function qualpop(id){
    document.getElementById("editid").value=id
    document.getElementById("spinner"+id).className="fa fa-spinner";
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/qualedit",
        data: {
            'eid': id
        },
        datatype: "json",
        success: function (data){
          //alert(data.name)
          document.getElementById("qualname").value=data.qname;
          document.getElementById("qualstatus").value=data.qstatus;
          $("#modal_basic").modal('show');
          document.getElementById("spinner"+id).className="fa fa-pencil";
        },
        error: function (error){
            console.log(error);
        }
    });
}

// -----qualification update------
function updatequal(){
    var id= document.getElementById("editid").value;
    var name=document.getElementById("qualname").value;
    var status=document.getElementById("qualstatus").value
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/qualupdate",
        data: {
            'eid': id,
            'qualname':name,
            'qualstatus':status
        },
        datatype: "json",
        success: function (data){
          //alert(data.name)
          alert(data.message)
          location.reload(true)  //refresh code
        },
        error: function (error){
            console.log(error);
             
        }
    });
}


// --------class edit-------
function classpop(id){
    document.getElementById("editid").value=id
    document.getElementById("spinner"+id).className="fa fa-spinner";
    
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/classedit",
        data: {
            'eid': id
        },
        datatype: "json",
        success: function (data){
          //alert(data.name)
          document.getElementById("clsname").value=data.cname;
          document.getElementById("clsstatus").value=data.cstatus;
          $("#modal_basic").modal('show');
          document.getElementById("spinner"+id).className="fa fa-pencil";
        },
        error: function (error){
            console.log(error);
        }
    });
}










    // -------division-----------
    function divpop(id){
        document.getElementById("editid").value=id
        document.getElementById("spinner"+id).className="fa fa-spinner";
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/divget",
            data: {
                'eid': id
            },
            datatype: "json",
            success: function (data){
              //alert(data.name)
              document.getElementById("divname").value=data.name;
              document.getElementById("divstatus").value=data.status;
              $("#modal_basic").modal('show');
              document.getElementById("spinner"+id).className="fa fa-pencil";
            },
            error: function (error){
                console.log(error);
            }
        });
    }


    function updateclass(){
        var id= document.getElementById("editid").value;
        var name=document.getElementById("clsname").value;
        var status=document.getElementById("clsstatus").value
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/classupdate",
            data: {
                'eid': id,
                'classname':name,
                'classstatus':status
            },
            datatype: "json",
            success: function (data){
              //alert(data.name)
              alert(data.message)
              location.reload(true)  //refresh code
            },
            error: function (error){
                console.log(error);
                 
            }
        });
    }
        


    function updatediv(){
        var id= document.getElementById("editid").value;
        var name=document.getElementById("divname").value;
        var status=document.getElementById("divstatus").value
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/divupdate",
            data: {
                'eid': id,
                'divname':name,
                'divstatus':status
            },
            datatype: "json",
            success: function (data){
              //alert(data.name)
              alert(data.message)
              location.reload(true)  //refresh code
            },
            error: function (error){
                console.log(error);
                 
            }
        });
    }
        

    // ----------------Employeeee------------
    function emppop(id){
        document.getElementById("editid").value=id;
        document.getElementById("spinner"+id).className="fa fa-spinner";
        $.ajax({
            type: "GET",
            url: "http://127.0.0.1:8000/empedit",
            data: {
                'eid': id
                
            },
            datatype: "json",
            success: function (data){
            //   alert(data.name)
            
              document.getElementById("empname").value=data.ename;
              document.getElementById("emparea").value=data.earea;
              document.getElementById("empstatus").value=data.estatus;
              $("#modal_basic").modal('show');
              document.getElementById("spinner"+id).className="fa fa-pencil";
            },
            error: function (error){
                console.log(error);
            }
        });
    }

// ----------employee update-------------
function updateemp(){
    var id= document.getElementById("editid").value;
    var name=document.getElementById("empname").value;
    var area=document.getElementById("emparea").value;
    var status=document.getElementById("empstatus").value
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8000/empupdate",
        data: {
            'eid': id,
            'empname':name,
            'emparea':area,
            'empstatus':status
        },
        datatype: "json",
        success: function (data){
          //alert(data.name)
          alert(data.message)
          location.reload(true)  //refresh code
        },
        error: function (error){
            console.log(error);
             
        }
    });
}

